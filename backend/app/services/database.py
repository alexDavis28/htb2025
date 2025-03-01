from threading import Lock
import sqlite3 as sql
from typing import Optional, Tuple, Any, List
from os import path

try: ## support file testing
    from ..conf import CONFIG 
    from ..main import log
except ImportError:
    CONFIG = {'db': 'htb25.testing.db'} # type: ignore
    import logs
    log = logs.Logger()

class DB:
    FILE_TABLE_CREATION: str = """
    CREATE TABLE files (
        file_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        hash TEXT NOT NULL
    )
    """
    
    USERS_TABLE_CREATION: str = """
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT NOT NULL UNIQUE
    )
    """
    
    USER_FILE_SYSTEM_TABLE_CREATION: str = """
    CREATE TABLE user_file_system (
        user_id INTEGER, 
        file_id INTEGER, 
        PRIMARY KEY(user_id, file_id), 
        FOREIGN KEY(user_id) REFERENCES users(user_id), 
        FOREIGN KEY(file_id) REFERENCES files(file_id)
    )
    """

    def __init__(self):
        self.__db_path = CONFIG['db']
        self.__lock = Lock()

        if not self.create_db_file(self.__db_path):
            raise Exception("Failed to create DB file")
        
        self.__conn = sql.connect(self.__db_path, check_same_thread=False)  

        if not self.setup_db():
            raise Exception("Failed to setup DB")


    def __del__(self):
        try : self.__conn.close()
        except: pass # Ce'st la vie 

    @staticmethod
    def create_db_file(db_path:str) -> bool:
        if path.isfile(db_path): return True
        else : 
            try: 
                with open(db_path, 'w') as _: pass
                return True
            except Exception as e:
                log.error("DB INIT", e)
                return False

    def setup_db(self) -> bool:
        return self.create_user_table() and \
            self.create_file_table() and \
            self.create_user_file_system_table()

    def __execute_for_one(self, query:str, params: Tuple[(Any | None), ... ] | None = None) -> Tuple[Optional[bool], Any]:
        if params is None: params = ()  # type: ignore

        with self.__lock:
            try:
                cursor = self.__conn.cursor()
                cursor.execute(query, params) # type: ignore
                ret = cursor.fetchone()
                cursor.close()
                self.__conn.commit()
                
                if ret is not None:
                    return (True, ret)
                else:
                    return (False, ret)
                
            except Exception as e:
                log.error("DB", e)
                return (None, None) 
    
    def __execute_for_all(self, query:str, params: Tuple[(Any | None), ... ] | None = None) -> List[Any] | None:
        if params is None: params = ()
        with self.__lock:
            try:
                cursor = self.__conn.cursor()
                cursor.execute(query, params) # type: ignore
                ret = cursor.fetchall()
                cursor.close()
                self.__conn.commit()
                
                return ret
                
            except Exception as e:
                log.error("DB", e)
                return None

    def table_exists(self, table_name:str) -> bool:
        _, value =  self.__execute_for_one("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return len(value) != 0 if value is not None else False

    ### === USER TABLE === ###
    def create_user_table(self) -> bool:
        if self.table_exists("users"): return True

        return_indicator, _ =  self.__execute_for_one(self.USERS_TABLE_CREATION)
        ret = return_indicator is not None
        if not ret: log.warn("DB", "Failed to create users table")
        return  ret 
    
    def create_user_file_system_table(self) -> bool:
        if self.table_exists("user_file_system"): return True

        return_indicator, _ =  self.__execute_for_one(self.USER_FILE_SYSTEM_TABLE_CREATION)

        ret = return_indicator is not None
        if not ret: log.warn("DB", "Failed to create user_file_system table")
        return ret
    
    def add_user(self, username:str) -> bool:
        suc, _ = self.__execute_for_one("INSERT INTO users (username) VALUES (?)", (username,))

        ret = suc == True
        if not ret: log.warn("DB", f"Failed to add user {username}")
        return ret
    
    def get_user_id(self, username:str) -> Optional[int]:
        suc, result = self.__execute_for_one("SELECT user_id FROM users WHERE username=?", (username,))
        if suc: return int(result[0])

        log.warn("DB", f"Failed to get user_id for {username}")
        return None
    
    def get_user_name(self, user_id:int) -> Optional[str]:
        suc, result = self.__execute_for_one("SELECT username FROM users WHERE user_id=?", (user_id,))
        log.debug("DB", f"get_user_name {(suc, result)}")

        if suc: return result[0]
        return None
    
    def add_user_file(self, user_id:int, file_id:int) -> bool:
        suc, _ = self.__execute_for_one("INSERT INTO user_file_system (user_id, file_id) VALUES (?, ?)", (user_id, file_id))
        return suc is not None

    ### === FILE TABLE === ###
    def create_file_table(self) -> bool:
        if self.table_exists("files"): return True

        return_indicator, _ =  self.__execute_for_one(self.FILE_TABLE_CREATION)

        ret = return_indicator is not None
        if not ret: log.warn("DB", "Failed to create files table")
        return ret

    def add_file_record(self, file_name:str, file_hash:str) -> bool:
        log.debug("DB", f"Adding file record {file_name} {file_hash}")
        
        returnValue, _ = self.__execute_for_one(
            "INSERT INTO files (name, hash) VALUES (?, ?)", 
            (file_name, file_hash)
        )
        log.debug("DB", f"Added file record {(returnValue, _)}")
        ret = returnValue is not None 
        if not ret: log.warn("DB", f"Failed to add file record {file_name}")
        return ret 

    def get_file_record(self, file_id:int) -> Optional[Tuple[str, str]]:
        suc, result = self.__execute_for_one("SELECT name, hash FROM files WHERE file_id=?", (file_id,))
        if suc: return (result[0], result[1])
        log.warn("DB", f"Failed to get file record for {file_id}")
        return None
    
    def get_file_id(self, file_hash:str) -> Optional[int]:
        suc, result = self.__execute_for_one("SELECT file_id FROM files WHERE hash=?", (file_hash,))
        if suc: return int(result[0])
        log.warn("DB", f"Failed to get file_id for {file_hash}")
        return None
    
    def get_user_files(self, UID:str) -> Optional[List[Tuple[str, str]]]:
        # check user exists as self.__execute_for_all will return an empty list even if the user doesnt exsists
        if self.get_user_name(int(UID)) is None: return None 

        res: (List[Tuple[str, str]] | None) = self.__execute_for_all( # type: ignore : we know this is what we'll get
            """SELECT f.name, f.hash 
            FROM files f 
            JOIN user_file_system ufs 
            ON f.file_id=ufs.file_id 
            WHERE ufs.user_id=?""", 
            (UID,)
        )
        if res is not None: return [(row[0], row[1]) for row in res]
        
        log.warn("DB", f"Failed to get user files for {UID}")
        return None
         


if __name__ == "__main__":
    db = DB()
    db.add_user("test")
    db.add_user("test2")
    db.add_user("test")

    db.add_file_record("test", "hash")
    db.add_file_record("test2", "hash2")
    db.add_file_record("test", "hash")

    print(db.get_user_id("test"))
    print(db.get_user_id("test2"))
    print(db.get_user_id("test3"))

    print(db.get_user_name(1))
    print(db.get_user_name(2))
    print(db.get_user_name(3))

    print(db.get_file_id("hash"))
    print(db.get_file_id("hash2"))
    print(db.get_file_id("hash3"))

    print(db.get_file_record(1))
    print(db.get_file_record(2))
    print(db.get_file_record(3))

from threading import Lock
from conf import config 
import sqlite3 as sql
from typing import Optional
from ..main import log
from typing import Tuple, Any
from os import path

class DB:
    FILE_TABLE_CREATION: str = """
    CREATE TABLE files (
        file_id INTEGER PRIMARY KEY, 
        name TEXT, 
        hash TEXT
    )
    """
    
    USERS_TABLE_CREATION: str = """
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT
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
        if not self.create_db_file(config['db']):
            raise Exception("Failed to create DB file")
    
        self.__db_path = config['db']
        self.__conn = sql.connect(self.__db_path, check_same_thread=False)  
        self.__lock = Lock()


    def __del__(self):
        try : self.__conn.close()
        except: pass # Ce'st la vie 

    @staticmethod
    def create_db_file(db_path:str) -> bool:
        if path.isfile(db_path): return True
        else : 
            try: 
                with open(db_path, 'w') as f: pass
                return True
            except Exception as e:
                log.error("DB INIT", e)
                return False

    def setup_db(self) -> bool:
        return self.create_user_table() and \
            self.create_file_table() and \
            self.create_user_file_system_table()

    def __execute(self, query:str, params: Tuple[(Any | None), ... ] | None = None) -> Tuple[Optional[bool], Any]:
        if params is None: params = ()  # type: ignore

        with self.__lock:
            try:
                cursor = self.__conn.cursor()
                cursor.execute(query, params) # type: ignore
                ret = cursor.fetchone()
                cursor.close()

                if ret is not None:
                    return (True, ret)
                else:
                    return (False, ret)
            except Exception as e:
                log.error("DB", e)
                return (None, None)

    def table_exists(self, table_name:str) -> bool:
        _, value =  self.__execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return len(value) != 1

    ### === USER TABLE === ###
    def create_user_table(self) -> bool:
        if self.table_exists("users"): return True

        suc, _ =  self.__execute(self.USERS_TABLE_CREATION)
        return suc == True
    
    def create_user_file_system_table(self) -> bool:
        if self.table_exists("user_file_system"): return True

        suc, _ =  self.__execute(self.USER_FILE_SYSTEM_TABLE_CREATION)
        return suc == True
    
    def add_user(self, username:str) -> bool:
        suc, _ = self.__execute("INSERT INTO users (username) VALUES (?)", (username,))
        return suc == True
    
    def get_user_id(self, username:str) -> Optional[int]:
        suc, result = self.__execute("SELECT user_id FROM users WHERE username=?", (username,))
        if suc: return int(result[0])
        return None
    
    def get_user_name(self, user_id:int) -> Optional[str]:
        suc, result = self.__execute("SELECT username FROM users WHERE user_id=?", (user_id,))
        if suc: return result[0]
        return None
    
    def add_user_file(self, user_id:int, file_id:int) -> bool:
        suc, _ = self.__execute("INSERT INTO user_file_system (user_id, file_id) VALUES (?, ?)", (user_id, file_id))
        return suc == True

    ### === FILE TABLE === ###
    def create_file_table(self) -> bool:
        if self.table_exists("files"): return True

        suc, _ =  self.__execute(self.FILE_TABLE_CREATION)
        return suc == True

    def get_number_file_entries(self) -> Optional[int]:
        suc, result = self.__execute("SELECT COUNT(*) FROM files", None)
        if suc: return int(result[0])
        return None

    def add_file_record(self, file_name:str, file_hash:str) -> bool:
        file_id = self.get_number_file_entries()
        if file_id is None: return False

        suc, _ = self.__execute(
            "INSERT INTO files (file_id, name, hash) VALUES (?, ?, ?)", 
            (str(file_id), file_name, file_hash)
        )
        return suc == True

    def get_file_record(self, file_id:int) -> Optional[Tuple[str, str]]:
        suc, result = self.__execute("SELECT name, hash FROM files WHERE file_id=?", (file_id,))
        if suc: return (result[0], result[1])
        return None
    
    def get_file_id(self, file_hash:str) -> Optional[int]:
        suc, result = self.__execute("SELECT file_id FROM files WHERE hash=?", (file_hash,))
        if suc: return int(result[0])
        return None
    

    



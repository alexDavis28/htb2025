from typing import Optional, Tuple
from hashlib import sha256
import os

try: ## support file testing
    from ..conf import CONFIG 
    from .logs import log
except ImportError:
    CONFIG = {'db': 'htb25.testing.db'} # type: ignore
    import logs
    log = logs.Logger()


class FileStore:
    def __init__(self) -> None:
        self.__filestore_path = CONFIG['filestore']

        if not self.create_filestore(self.__filestore_path):
            raise Exception("Failed to create filestore")
        
    def create_filestore(self, filestore_path: str) -> bool:
        if not os.path.exists(filestore_path):
            try:
                os.makedirs(filestore_path)
            except Exception as e:
                log.error("FileStore init", e)
                return False
        return True
    
    def get_file(self, filehash: str) -> Optional[bytes]:
        file_path = os.path.join(self.__filestore_path, filehash)
        log.debug("FileStore get", f"Getting file {filehash}")
        if not os.path.exists(file_path):
            log.warn("FileStore get", f"File {filehash} not found")
            return None
        try : 
            with open(file_path, 'rb') as f:
                return f.read()
        except Exception as e:
            log.error("FileStore get", e)
            return
            
    """
    Save a file to the file store
    - returns
        - bool: if we wrote to the store, to prevent duplicate copys of the same file
        - str | None: if the file was saved, the filehash, else None ie error
    """
    def save_file(self, data: bytes) -> Tuple[bool, (str | None)]:
        filehash:str = sha256(data).hexdigest()
        filehash = filehash.strip().replace("\n", "")

        file_path = os.path.join(self.__filestore_path, filehash)

        if os.path.exists(file_path): return False, filehash # dont need to save the file again
        
        try:
            with open(file_path, 'wb') as f:
                f.write(data)
            return True, filehash
        except Exception as e:
            log.error("FileStore save", e)
            return False, None
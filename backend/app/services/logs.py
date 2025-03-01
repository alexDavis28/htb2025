from threading import Lock


class Logger: 
    def __init__(self) -> None:
        self.__lock = Lock()
    
    def error(self, module: str, e: Exception) -> None: 
        with self.__lock:
            print(f"ERROR: {module} - {e}")

    def info(self, module: str, msg: str) -> None:
        with self.__lock:
            print(f"INFO: {module} - {msg}")
    
    def debug(self, module: str, msg: str) -> None:
        with self.__lock:
            print(f"DEBUG: {module} - {msg}")

    def warning(self, module: str, msg: str) -> None:
        with self.__lock:
            print(f"WARNING: {module} - {msg}")
        
    def critical(self, module: str, msg: str) -> None:
        with self.__lock:
            print(f"CRITICAL: {module} - {msg}")
    
    def success(self, module: str, msg: str) -> None:
        with self.__lock:
            print(f"SUCCESS: {module} - {msg}")
    
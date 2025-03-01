from threading import Lock


class Logger: 
    def __init__(self) -> None:
        self.__lock = Lock()
    
    def error(self, module: str, e: Exception) -> None: 
        with self.__lock:
            print(f"ERROR: {module} - {e}")


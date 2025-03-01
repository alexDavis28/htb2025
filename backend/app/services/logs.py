from threading import Lock
from datetime import datetime


class Logger: 
    def __init__(self) -> None:
        self.__lock = Lock()
    
    def __log(self, level: str, module: str, msg: str) -> None:
        with self.__lock:
            print(f"{datetime.now().strftime(r'%y/%m/%d %H:%M:%S')} [{level}]: {module} - {msg}")

    def error(self, module: str, e: Exception) -> None: 
        self.__log("E", module, e.__str__())

    def info(self, module: str, msg: str) -> None:
        self.__log("I", module, msg)
    
    def warn(self, module: str, msg: str) -> None:
        self.__log("W", module, msg)
    
    def debug(self, module: str, msg: str) -> None:
        self.__log("D", module, msg)

    def critical(self, module: str, msg: str) -> None:
        self.__log("C", module, msg)
from enum import Enum
from .utils import MetaSingleton


class LevelEnum(Enum):
    critical = "CRITICAL"
    info = "INFO"


class Logging(metaclass=MetaSingleton):
    def __init__(self, file_name: str) -> None:
        """initialize the file name"""

        self.file_name = file_name

    def _write_log(self, level: LevelEnum, msg: str) -> None:
        """Write to the log file"""

        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")  # [INFO] message goes here...

    def info(self, msg):
        self._write_log(LevelEnum.info.name, msg)

    # TODO: Add more functions for
    # - critical
    # - error
    # - warning

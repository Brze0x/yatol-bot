from typing import Optional


class YatolBotException(Exception):
    """
    Base yatol bot exception.
    """

    def __init__(self, msg: Optional[str] = None) -> None:
        self.msg = msg

    def __str__(self) -> str:
        exception_msg = "Message: %s\n" % self.msg
        return exception_msg


class ValueOutOfRangeException(YatolBotException):
    """
    Thrown when value is out of range.
    """
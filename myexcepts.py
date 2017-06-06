class MyError(Exception):
    """base custom exception implements Excetion."""

    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class NoDataException(MyError):
    """search es and no data return exception."""
    pass


class ServerException(MyError):
    """search es and no data return exception."""
    pass

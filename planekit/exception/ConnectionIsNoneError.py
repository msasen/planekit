class Error(Exception):
    pass


class ConnectionIsNoneError(Error):
    def __init__(self, connection_string, message="is not connection_string"):
        self.connection_string = connection_string
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'\n\t{self.connection_string} {self.message}'

    def is_connection_none(self):
        if self.connection_string is None:
            raise ConnectionIsNoneError(self.connection_string)

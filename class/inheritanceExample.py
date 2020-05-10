from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.open = False

    @abstractmethod
    def read(self):
        pass

    def Open(self):
        if self.open:
            raise InvalidOperationError("Stream is already open")
        self.open = True

    def Close(self):
        if not self.open:
            raise InvalidOperationError("Stream is already closed")
        self.open = False


class FileStream(Stream):
    def read(self):
        print("reading data from file ")


class NetworkStream(Stream):
    def read(self):
        print("reading data from network ")


class MemoryStream(Stream):
    def read(self):
        print("reading data from memory ")


M = MemoryStream()
M.Open()
M.Close()

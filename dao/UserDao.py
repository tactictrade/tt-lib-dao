from abc import ABC, abstractmethod

class UserDao(ABC):
    @abstractmethod
    def create(self,userDto):
        pass
    @abstractmethod
    def read(self,userDto):
        pass
    @abstractmethod
    def update(self,userDto):
        pass
    @abstractmethod
    def delete(self,userDto):
        pass
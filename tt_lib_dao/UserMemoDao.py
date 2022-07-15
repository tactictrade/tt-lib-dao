from venv import create
from dao.UserDao import UserDao
import uuid

class UserDao(UserDao):
    def __init__(self):
        super().__init__()    
        self.userTable = dict()
    
    def create(self,userDto):
        userDto['id']=uuid.uuid4().hex
        self.userTable[userDto['id']]=userDto
        print('User' +userDto['id']+ ' created in Memo!!!!')
        return userDto
    
    def read(self,userDto):
        user = self.userTable[userDto.id]
        if not user:
            raise Exception("User not found!") #TODO create dictionary
        print(f'User {user.id} readed in Memo!!!!')
        return user
    
    def update(self,userDto):
        if not userDto.id:
            raise Exception("User id not found!") #TODO create dictionary
        self.userTable[userDto.id]=userDto
        print(f'User {userDto.id} update in Memo!!!!')

    def delete(self,userDto):
        del self.userTable[userDto.id]
        print(f'User {userDto.id} deleted in Memo!!!!')



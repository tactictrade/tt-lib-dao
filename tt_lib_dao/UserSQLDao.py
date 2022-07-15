from dao.UserDao import UserDao
class UserDao(UserDao):
    def __init__(self):
        super().__init__()
    
    def create(self,userDto):
        print(f'User {userDto} created in SQL!!!!')
    
    def read(self,userDto):
        print(f'User {userDto} readed in SQL!!!!')
    
    def update(self,userDto):
        print(f'User {userDto} update in SQL!!!!')

    def delete(self,userDto):
        print(f'User {userDto} deleted in SQL!!!!')
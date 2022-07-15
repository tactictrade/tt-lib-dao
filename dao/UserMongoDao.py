from main.dao.UserDao import UserDao
class UserDao(UserDao):
    def __init__(self):
        super().__init__()
    
    def create(self,userDto):
        print(f'User {userDto} created in Mongo!!!!')
    
    def read(self,userDto):
        print(f'User {userDto} readed in Mongo!!!!')
    
    def update(self,userDto):
        print(f'User {userDto} update in Mongo!!!!')

    def delete(self,userDto):
        print(f'User {userDto} deleted in Mongo!!!!')
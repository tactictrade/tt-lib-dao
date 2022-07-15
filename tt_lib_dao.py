from dao.UserDao import UserDao as UserDao
from dao.UserMemoDao import UserDao as UserMemoDao
from dao.UserSQLDao import UserDao as UserSQLDao
from dao.UserMongoDao import UserDao as UserMongoDao


def health():
    print("Hi there!")
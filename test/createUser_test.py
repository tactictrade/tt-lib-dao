# This is one test for create user
# use pytest library 
import json
from dao.UserMongoDao import UserDao
from test.utils.secrets import get_secret

# Get secrets from AWS Secrets Manager
secrets = get_secret()
# Convert string to json
secrets = json.loads(secrets)

# Create user in MongoDB
config = {
        'TT_MONGO_DB_URI': secrets['TT_MONGO_DB_URI'],
    }


userDto = {
        'username': 'francis12',
        'first_name': 'Francis',
        'last_name': 'francis@test.com',
        'is_verified': True,
        'is_active': True,
        'is_staff': False,
        'create_at': '2020-01-01T00:00:00Z',
        'is_public': True,
        'iss': '123123123123123123123'
    }

# Create test for create new user
def test_createUser():

    result = UserDao(config).create(userDto)
    
    assert result is not None


# Create test read one user
def test_readUser():

    result = UserDao(config).find_one(userDto)

    # Check if username is equal to francis12
    assert result['username'] == 'francis12'
    
# Create test read all users

def test_readAllUsers():

    result = UserDao(config).find()

    for user in result:
        # Check if username is equal to francis12
        assert user['username'] == 'francis12'

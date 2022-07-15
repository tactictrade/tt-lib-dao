# Welcome to library tt-lib-dao

    pip install -U pip setuptools

Create file setup.py

    setup(
        name='dao',
        version="0.0.1",
        url='https://github.com/tactictrade/tt-lib-dao.git',
        author='CannavIT',
        author_email='cecilio.cannav@gmail.com',
        py_modules=['dao'],
        description="dao Library for TacticTrade", 
        entry_points={
        'console_scripts': [
            'add=tt_lib_dao:cmd_add',
        ],
        },
    )

Add one Health test function tt_lib_dao.py

    def health():
        print("Hi there!")    

Test it

    python -c "import tt_lib_dao; tt_lib_dao.health()"

## Install library in localhost

Install in local 

    pip install -e .

Check in local

    cd ..
    
    python -c "import tt_lib_dao; tt_lib_dao.UserDao"

    python -c "from tt_lib_dao import UserDao"

    pip install git+https://github.com/tactictrade/tt-lib-dao.git

    python -c "import tt_lib_dao; tt_lib_dao.health()"
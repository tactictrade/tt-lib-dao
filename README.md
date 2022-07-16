# Welcome to library tt-lib-dao

    pip install -U pip setuptools

Create file setup.py

    from setuptools import setup

    setup(
        name='dao',
        version="0.0.1",
        url='https://github.com/tactictrade/tt-lib-dao.git',
        author='CannavIT',
        author_email='cecilio.cannav@gmail.com',
        py_modules=['tt_lib_dao'],
        packages=['dao'],
        description="dao Library for TacticTrade", 
        entry_points={
        'console_scripts': [
            'add=tt_lib_dao:cmd_add',
        ],
        }
        # install_requires=[
        #    "Django >= 1.1.1",
        #    "pytest",
        #  ],
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
    
    python -c "import tt_lib_dao; tt_lib_dao.health()"

    python -c "import tt_lib_dao; tt_lib_dao"

    python -c "from dao.UserDao import UserDao"

## How add install library

Create the file requirement.txt and add this

    git+https://github.com/tactictrade/tt-lib-dao.git#develop


Install from terminal with pip

    pip install git+https://github.com/tactictrade/tt-lib-dao.git#egg=dao

Install from terminal with pipenv

    pipenv install git+https://github.com/tactictrade/tt-lib-dao.git#egg=dao

## Run the test using pytest

    pytest
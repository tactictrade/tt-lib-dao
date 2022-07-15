from setuptools import setup

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
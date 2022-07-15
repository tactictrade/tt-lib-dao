from setuptools import setup

setup(
    name='tt_lib_dao',
    version="0.0.1",
    url='https://github.com/tactictrade/tt-lib-tt_lib_dao.git',
    author='CannavIT',
    author_email='cecilio.cannav@gmail.com',
    py_modules=['tt_lib_dao'],
    description="tt_lib_dao Library for TacticTrade",
    entry_points={
    'console_scripts': [
        'add=tt_lib_dao:cmd_add',
    ],
},
)
from setuptools import setup

__version__ = 'dev'

setup(
    name='my_pip_package',
    version=__version__,
    url='https://github.com/tactictrade/tt-lib-dao.git',
    author='CannavIT',
    author_email='cecilio.cannav@gmail.com',
    py_modules=['my_pip_package'],
    entry_points={
    'console_scripts': [
        'add=my_pip_package.math:cmd_add',
    ],
},
)
from setuptools import setup

NAME = "x_client_transaction"
VERSION = "0.0.1"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "beautifulsoup4 >= 4.13.3, < 5.0.0",
    "lxml >= 5.3.1, < 6.0.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="x_client_transaction",
    author_email="yuki@yuki0311.com",
    url="https://github.com/fa0311/x_client_transaction",
    keywords=[],
    install_requires=REQUIRES,
    include_package_data=True,
    license="MIT",
)
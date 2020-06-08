from setuptools import setup
from kanobu_server import __version__

with open("README.md", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="kanobu_server",
    version=__version__,
    author="Daniel Zakharov",
    author_email="daniel734@bk.ru",
    description="Server for kanobu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="kanobu game server",
    url="https://github.com/jDan735/kanobu-server",
    license="MIT",
    include_package_data=True,
    packages=["kanobu_server"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3",
    entry_points={
        "console_scripts": [
            "kanobu-server=kanobu_server.server:server",
            "kanobu-client=kanobu_server.client:client"
        ]
    }
)

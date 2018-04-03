from setuptools import setup
from setuptools import find_packages

setup(
    name="Emojipasta-Bot for Discord",
    description="convert text to emojipasta",
    version="1.0",
    url="https://github.com/musca1997",
    author="toiletplunger#8909",
    author_email="musturtwig@gmail.com",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    packages=find_packages("src"),
    package_dir={'': 'src'},
    package_data={'': ["*.txt", "*.json"]},
    include_package_data=True,
    install_requires=[
        "emoji",
        "praw"
    ]
)


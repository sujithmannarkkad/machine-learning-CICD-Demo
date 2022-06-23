from setuptools import setup
from typing import List

#Declaring variables for setup
PROJECT_NAME="HOUSING-PREDICTOR"
VERSION="0.0.1"
AUTHOR="SUJITHMANNARKKAD@GMAIL.COM"
DESCRIPTION="This is first end to end project using CI-CD"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_lists()->List[str]:
    """
    read data from requirements.txt and return the details as a List
    :return: List of values in requirements.txt as list
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_lists()
)


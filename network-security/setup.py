'''
setup.py is an essential file in a our project 
that contains metadata about the project and instructions on how to install it. 
It is used by setuptools, a Python package that helps with packaging 
and distributing Python projects.
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_lst:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            # Read the lines from the file
            lines = file.readlines()
            for line in lines:
                requirements=line.strip()
                #ignore empty lines and -e .
                if requirements and requirements != "-e .":
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

# print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.1.0",
    aurthor="Hridesh",
    author_email="hridesh.mehrotra@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)

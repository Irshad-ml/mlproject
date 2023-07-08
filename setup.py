from setuptools import find_packages,setup
from typing import List
from os.path import exists

HYPHEN_E_DOT ='-e .'
def get_requirement(file_path:str) -> List[str]:
    """
    This function read the requirements.txt file and return list of packages
    """
    requirements = []
    if not exists(file_path):
        print("File is not available")
    else:
        with open(file_path) as file_object:
            requirements = file_object.readlines()
            requirements=[req.replace('\n','')for req in requirements]    
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)  
    return requirements
setup(
    
    name='mlproject',
    version='0.0.1',
    author='Md Irshad',
    author_email='m3irshad3@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
    
)
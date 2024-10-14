from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Aayon Mukherjee',
    author_email='aayonmukherjee21@gmail.com',
    packages=find_packages(),  # Corrected formatting
    install_requires=get_requirements('requirements.txt')
)

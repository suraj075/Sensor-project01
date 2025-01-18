#setup.py -
# used to build and distribute python package
# it contain - 1.package, 2.Name, 3.version. 4.Dependencies

from setuptools import find_packages, setup
from typing import List

HYPE_E_DOT='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

    if HYPE_E_DOT in requirements:
        requirements.remove(HYPE_E_DOT)
    return requirements

setup(
    name='sensor_detection',
    version='0.0.1',
    author='suraj',
    author_email='kumarsuraj07553@gmail.com',
    install_requirements = get_requirements('requirement.txt'),
    packages = find_packages()
)


# we can trigger the setup.py file in two ways 
#1. simply by 'python setup.py install'
#2. by add '-e.' in the requirement.txt file and run in the command 'pip install -r requirement.txt'
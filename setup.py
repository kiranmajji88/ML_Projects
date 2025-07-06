from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'# This is a constant variable that is used to remove the -e . line from the requirements file, which is used for editable installs.
def get_requirements(file_path:str)->List[str]: # This function will return the list of requirements from the requirements.txt file

    '''
    This function will return the list of requirements
    '''
    requirements=[]    
    with open(file_path) as file_obj: # Open the requirements.txt file in read mode
        # file_obj is a file object that we can use to read the contents of the file
        # We are using the with statement to open the file, which will automatically close the file
        # after the block of code is executed, even if an exception is raised.
        # This is a good practice to avoid leaving files open and consuming system resources.
        # We are using the readlines() method to read all the lines in the file and 
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements] # While reading the requirements file, it includes \n at the end of each line, so we need to remove it.

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # This is used to remove the -e . line from the requirements file, which is used for editable installs.

        return requirements # This will return the list of requirements without the -e . line

setup(
name='mlproject',
version='0.0.1',
author= 'Kiran',
author_email='kiranmajji1988@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt') # This will call the get_requirements function to get the list of requirements from the requirements.txt file

)


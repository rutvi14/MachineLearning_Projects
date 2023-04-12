from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str)->List[str]:
    """Return list of requirements

    Args:
        file_path (str): file path of requirements.txt

    Returns:
        List[str]: List of requirements to be installed.
    """
    requirements = []
    with open(file_path) as fp:
        requirements = fp.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Rutvi",
    author_email="rutvirajesh014@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)
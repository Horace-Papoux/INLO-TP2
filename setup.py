from setuptools import find_packages, setup

setup(
    name="TP2",
    version="0.1.0",
    description="Travail pratique sur la qualité de code et le CI/CD",
    long_description=open("README.md").read(),
    author="prenom.nom",
    package_dir={"TP2": "src"},
    install_requires=open("requirements.txt").readlines()
)

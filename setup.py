from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='whiteboardbot',
    version='0.0.1',
    description='Software für einen Whiteboard beschriftenden Roboter',
    long_description=readme,
    author='Finn Harms',
    packages=find_packages(exclude=('tests', 'docs'))
)

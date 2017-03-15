from setuptools import setup
from setuptools.command.develop import develop

with open('requirements.txt') as r:
    requirements = r.readlines()

setup(
    name='huffmanCodes',
    description='Web app calculating Huffman Coding',
    author='Connor Hallett & Spencer Lee',
    author_email='hallec3@mcmaster.ca',
    url='https://github.com/challett/huffmanCodes',
    install_requires=requirements,
)

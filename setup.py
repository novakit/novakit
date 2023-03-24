from os import path

from setuptools import setup

setup(
    name='novakit',
    version='0.0.1',
    packages=['novakit'],
    url='https://github.com/novakit/novakit',
    license='MIT',
    author='Guo Y.K.',
    author_email='hi@guoyk.xyz',
    description='a stable diffusion toolkit',
    install_requires=open(path.join(path.dirname(__file__), "requirements.txt")).read().splitlines(),
)

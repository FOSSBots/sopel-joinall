from __future__ import print_function
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()
with open('requirements.txt') as requirements_file:
    requirements = list(requirements_file.readlines())


setup(
    name='sopel_plugins.joinall',
    version='1.0.3',
    description='joinall plugin for Sopel',
    long_description=readme,
    long_description_content_type='text/markdown',  # This is important!
    author='MirahezeBot Contributors',
    author_email='staff@mirahezebots.org',
    url='https://github.com/MirahezeBots/sopel-joinall',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=requirements,
    license='Eiffel Forum License, version 2',
)

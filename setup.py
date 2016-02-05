# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-executor',
    version='0.0.1',
    author=u'Will & Skill',
    author_email='info@willandskill.se',
    packages=find_packages(),
    url='https://github.com/willandskill/django-executor',
    license='MIT licence, see LICENCE.txt',
    description='Manage your django management commands easily within your browser',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True
)
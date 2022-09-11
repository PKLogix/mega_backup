# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='mega_backup',
    version=version,
    description='Use Mega Backup for Frappe and ERPNext',
    author='PKLogix.com',
    author_email='pklogix.official@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe","mega"),
)

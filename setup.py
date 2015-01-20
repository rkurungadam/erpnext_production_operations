from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='erpnext_production_operations',
    version=version,
    description='Creates Operations for Production Order based on BOM operations',
    author='earthians',
    author_email='ranjith@earthianslive.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe","erpnext"),
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    from distutils.core import setup
    find_packages = None


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'tendril-utils-core',
    'tendril-utils-types',
    'fs==0.5.4',
    'jinja2',
    'arrow',
    'numpy',
    'matplotlib',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tendril-dox-render',
    version='0.1.1',
    description="Core document rendering primitives for tendril",
    long_description=readme,
    author="Chintalagiri Shashank",
    author_email='shashank@chintal.in',
    url='https://github.com/chintal/tendril-dox-render',
    packages=find_packages(),
    install_requires=requirements,
    license="AGPLv3",
    zip_safe=False,
    keywords='tendril',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    # test_suite='tests',
    # tests_require=test_requirements
)

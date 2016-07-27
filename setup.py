#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'urwid>=1.3.1',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='chatcraft',
    version='0.1.0',
    description="A library and command line client for chatting on Minecraft servers.",
    long_description=readme + '\n\n' + history,
    author="foxfoxfox",
    author_email='flaeme.flow@gmail.com',
    url='https://github.com/Flaeme/chatcraft',
    packages=[
        'chatcraft',
    ],
    package_dir={'chatcraft':
                 'chatcraft'},
    entry_points={
        'console_scripts': [
            'chatcraft=chatcraft.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='chatcraft',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

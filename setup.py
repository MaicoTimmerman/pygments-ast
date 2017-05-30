#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-ast',
    version='0.2',
    description='Pygments lexer for ast',
    long_description=open('README.rst').read(),
    keywords='pygments ruby rspec lexer',
    license='BSD',

    author='Maico Timmerman',
    author_email='maico.timmerman@gmail.com',

    url='',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.lexers]
                    rspec=pygments_ast:ASTLexer''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

#!/usr/bin/env python
import recon.release
from glob import glob
from numpy import get_include as np_include
from setuptools import setup, find_packages, Extension


version = recon.release.get_info()
recon.release.write_template(version, 'lib/stsci/sphinxext')

setup(
    name = 'stsci.sphinxext',
    version = version.pep386,
    author = 'Michael Droettboom',
    author_email = 'help@stsci.edu',
    description = 'A set of tools and templates to customize Sphinx for use in STScI projects',
    url = 'https://github.com/spacetelescope/stsci.sphinxext',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'astropy',
        'docutils',
        'matplotlib',
        'nose',
        'numpy',
        'numpydoc',
        'sphinx',
        'stsci.sphinxext',
    ],
    package_dir = {
        '': 'lib'
    },
    packages = find_packages(),
    package_data = {
        '': ['README'],
        'licenses': '*',
        'stsci/sphinxext': ['latex/*'],
        'stsci_sphinx_theme': ['*.*'],
        'stsci_sphinx_theme/static': ['*.*'],
    },
)

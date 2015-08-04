# Copyright (c) 2015 Florian Wagner
#
# This file is part of XL-mHG.
#
# XL-mHG is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License, Version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

""" A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import sys
import os

from setuptools import setup, find_packages, Extension
# To use a consistent encoding
from codecs import open
from os import path

root = 'xlmhg'

try:
	import numpy as np # numpy is required
except ImportError:
	print 'You must install NumPy before installing XL-mHG!'
	sys.exit(1)

try:
	from Cython.Distutils import build_ext
except ImportError:
	print 'You must install Cython before installing XL-mHG!'
	sys.exit(1)

here = path.abspath(path.dirname(__file__))
description = 'XL-mHG: A Nonparametric Test For Enrichment in Ranked Binary Lists.'

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# extensions
ext_modules = []
ext_modules.append(Extension(root + '.' + 'xlmHG_cython', sources= [root + os.sep + 'xlmHG_cython.pyx'], include_dirs = [np.get_include()]))

setup(
    name='xlmhg',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.2',

    description=description,
    #long_description=long_description,
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/flo-compbio/xlmhg',

    # Author details
    author='Florian Wagner',
    author_email='florian.wagner@duke.edu',

    # Choose your license
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='statistics nonparametric enrichment test ranked binary lists',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    packages=['xlmhg'],

	# extensions
	ext_modules = ext_modules,
	cmdclass = {'build_ext': build_ext},

	#libraries = ['xlmHG_cython.so'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    #install_requires=['peppercorn'],
    install_requires=['numpy','cython'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        #'dev': ['check-manifest'],
        #'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        #'sample': ['package_data.dat'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        #'console_scripts': [
        #    'extract_protein_coding_genes = goparser.extract_protein_coding_genes:main',
        #],
    },
)

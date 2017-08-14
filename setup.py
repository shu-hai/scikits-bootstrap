#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name = "scikits.bootstrap",
    version = "0.3.3dev1",
    packages = find_packages(),

     install_requires = ['numpy','scipy'],
    namespace_packages = ['scikits'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.md', '*.rst'],
    },

    # metadata for upload to PyPI
    author = "Constantine Evans",
    author_email = "cevans@evanslabs.org",
    description = "Bootstrap confidence interval estimation routines for SciPy",
    license = "Modified BSD",
    #keywords = "",
    url = "http://github.com/cgevans/scikits-bootstrap",   # project home page, if any
    classifiers =
        [ 'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: C',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering',
          'Operating System :: OS Independent',
          ],
    test_suite = "nose.collector"
    # could also include long_description, download_url, classifiers, etc.
)

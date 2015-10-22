# -*- coding: utf-8 -*-
"""
This module contains the tool of birdhousebuilder.recipe.sphinx
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1.0'

long_description = (
    read('README.rst')
    )


setup(name='birdhousebuilder.recipe.sphinx',
      version=version,
      description="Buildout recipe to generate and Sphinx-based documentation for Birdhouse.",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        ],
      keywords='buildout sphinx',
      author='Birdhouse',
      author_email='',
      url='https://github.com/birdhouse/birdhousebuilder.recipe.sphinx',
      license='Apache License 2.0',
      packages = find_packages('birdhousebuilder', exclude=['ez_setup']),
      package_dir = {'':'birdhousebuilder'},
      namespace_packages=['birdhousebuilder', 'birdhousebuilder.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'setuptools',
            'zc.buildout',
            'zc.recipe.egg',
            'docutils',
            'Sphinx>=1.3'],
      tests_require=['zope.testing', 'zc.buildout', 'manuel'],
      extras_require=dict(tests=['zope.testing', 'zc.buildout', 'manuel']),
      test_suite = 'birdhousebuilder.recipe.sphinx.tests.test_docs.test_suite',
      entry_points = {"zc.buildout": ["default = birdhousebuilder.recipe.sphinx:Recipe"]}
      )

# python setup.py --long-description | rst2html.py > /dev/null

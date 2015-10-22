# -*- coding: utf-8 -*-
"""
Recipe sphinx

Based on https://pypi.python.org/pypi/collective.recipe.sphinxbuilder
"""

import logging
import os
import re
import sys
#import zc.buildout
#from fnmatch import fnmatch
from birdhousebuilder.recipe import conda

log = logging.getLogger(__name__)


class Recipe(object):
    """buildout recipe to setup sphinx for birdhouse components"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

        self.outputs = options.get('outputs', 'html')

        #self.build_dir = os.path.join(self.buildout_dir, options.get('build', 'docs'))
        #self.source_dir = options.get('source', os.path.join(self.build_dir, 'source'))

    def install(self):
        """Installer"""
        installed = []
        installed += list(self.install_conda())

        return installed

    def install_conda(self):
        script = conda.Recipe(
            self.buildout,
            self.name,
            {'pkgs': 'sphinx sphinx_rtd_theme mako docutils'})
        return script.install()

    def update(self):
        return self.install()


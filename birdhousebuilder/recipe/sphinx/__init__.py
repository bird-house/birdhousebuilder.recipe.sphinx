# -*- coding: utf-8 -*-
"""
Recipe sphinx

Based on https://pypi.python.org/pypi/collective.recipe.sphinxbuilder
"""

import os
import re
import sys
from mako.template import Template
import zc.buildout
#from fnmatch import fnmatch
from birdhousebuilder.recipe import conda

import logging
log = logging.getLogger(__name__)

makefile = Template(filename=os.path.join(os.path.dirname(__file__), "Makefile"))
conf_py = Template(filename=os.path.join(os.path.dirname(__file__), "conf.py"))
index_rst = Template(filename=os.path.join(os.path.dirname(__file__), "index.rst"))

class Recipe(object):
    """buildout recipe to setup sphinx for birdhouse components"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.buildout_dir = self.buildout['buildout']['directory']

        self.outputs = options.get('outputs', 'html')

        self.docs_dir = os.path.join(self.buildout_dir, options.get('docs', 'docs'))
        self.build_dir = os.path.join(self.docs_dir, 'build')
        self.source_dir = os.path.join(self.docs_dir, 'source')

        self.options['project'] = self.options.get('project', 'MyBird')
        self.options['version'] = self.options.get('version', '0.1')
        self.options['html_theme'] = self.options.get('html_theme', 'alabaster')

    def install(self):
        """Installer"""
        installed = []
        installed += list(self.install_conda())
        installed += list(self.install_dir())
        installed += list(self.install_makefile())
        installed += list(self.install_config())
        installed += list(self.install_index())

        return installed

    def install_conda(self):
        script = conda.Recipe(
            self.buildout,
            self.name,
            {'pkgs': 'sphinx sphinx_rtd_theme mako docutils'})
        return script.install()

    def install_dir(self):
        # create build folder
        conda.makedirs(self.build_dir)

        # create source folder
        conda.makedirs(self.source_dir)

        return tuple()

    def install_makefile(self):
        content = makefile.render(**self.options)
        name = os.path.join(self.docs_dir, 'Makefile')
        self._write_file(name, content)
        return [name]

    def install_config(self):
        content = conf_py.render(**self.options)
        name = os.path.join(self.source_dir, 'conf.py')
        self._write_file(name, content)
        return [name]

    def install_index(self):
        content = index_rst.render(**self.options)
        name = os.path.join(self.source_dir, 'index.rst')
        self._write_file(name, content)
        return [name]

    def update(self):
        return self.install()

    def _write_file(self, name, content):
        with open(name, 'w') as fp:
            fp.write(content)

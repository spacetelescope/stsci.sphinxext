from __future__ import division # confidence high
import os
import shutil

import distutils.extension
pkg = "stsci_sphinxext"

setupargs = {
    'version' :         '1.0',
    'description' :
        'A set of tools and templates to customize Sphinx for use in STScI projects',

    'long_description' :
'''In short, you use this package by adding 'from stsci_docs.conf
import *' to the top of your conf.py in your Sphinx documentation
source tree.  In long, see the README file.''',

    'author' :          'Michael Droettboom',

    'author_email' :    'mdroe@stsci.edu',

    'url' :             '',

    'scripts' :         [],

    'license' :         'BSD',

    'platforms' :       ["Linux", "Solaris", "Mac OS X", "Win"],

    'package_dir':      { 'stsci_sphinxext' : 'lib/stsci_sphinxext'  },

    # how to install your data files:
    #   [
    #       ( directory_name_files_go_to, [ file_name_in_source_tree, another_data_file, etc ] )
    #   ]
    'data_files' :      [
        (os.path.join(pkg, 'stsci_sphinx_theme'), [
                'lib/stsci_sphinxext/stsci_sphinx_theme/theme.conf',
                ]
         ),
        (os.path.join(pkg, 'stsci_sphinx_theme', 'static'), [
                'lib/stsci_sphinxext/stsci_sphinx_theme/static/stsci_sphinx.css_t',
                'lib/stsci_sphinxext/stsci_sphinx_theme/static/stsci_logo.png',
                'lib/stsci_sphinxext/stsci_sphinx_theme/static/stsci_background.png'
                ]
         ),
        (os.path.join(pkg, 'latex'), [
                'lib/stsci_sphinxext/latex/stsci_logo.pdf',
                'lib/stsci_sphinxext/latex/tsr.cls',
                'lib/stsci_sphinxext/latex/sphinxtsr.cls'
                ]
         )
        ],
}


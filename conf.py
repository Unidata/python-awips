import sys
import os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../..'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'python-awips'
copyright = '2019, Unidata'
exclude_patterns = []
pygments_style = 'sphinx'
html_static_path = ['_static']

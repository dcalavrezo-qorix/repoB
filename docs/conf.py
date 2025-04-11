import os
import sys

# Project info
project = 'RepoB'
author = 'Dan'
release = '0.1'
version = "v1"

extensions = [
    'sphinx_needs',
]

# Give each repo a unique ID prefix
needs_id_prefix = "MODB_"   
needs_id_required = True   
needs_build_json = True
master_doc = 'index'


# Paths: include your docs folder so Sphinx can find index.rst
sys.path.insert(0, os.path.abspath('.'))



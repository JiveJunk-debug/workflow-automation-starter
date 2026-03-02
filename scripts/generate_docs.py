"""Automatically generates markdown documentation from Python docstrings."""

import os
import pydoc

def generate_docs(module_name):
    """Generate markdown documentation for a given module."""
    module = __import__(module_name)
    docs = pydoc.doc(module)
    return docs

if __name__ == '__main__':
    modules = ['module1', 'module2']  # Add your module names here
    for module in modules:
        output = generate_docs(module)
        with open(f'{module}.md', 'w') as f:
            f.write(output)
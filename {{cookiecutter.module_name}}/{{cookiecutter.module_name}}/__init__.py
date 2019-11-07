"""{{ cookiecutter.short_description }}

See README.md for more intructions on how to run the script.
"""

__version__ = "{{ cookiecutter.version }}"

from .{{ cookiecutter.module_name }} import hello_world  # noqa
from .cli import main  # noqa

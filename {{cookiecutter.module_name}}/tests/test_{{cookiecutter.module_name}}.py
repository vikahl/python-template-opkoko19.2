import pytest

from {{ cookiecutter.module_name }} import {{ cookiecutter.module_name }}


def test_hello_who():

    assert {{ cookiecutter.module_name }}.hello_world('test') == 'Hello world!\nHello test!'

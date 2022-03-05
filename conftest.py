""" pytest configuration file

    Also needed to invoke pytest from the command line on Windows. Ugh :-(
    Otherwise, you get: ModuleNotFoundError: No module named 'myrepo'

    Having a conftest.py in the project root directory will add it to the sys.path
    See https://stackoverflow.com/a/49033954/625350
"""
import pytest

#!/usr/bin/python3

"""
Python file that is used to indicate that the
directory it is present in is a Python package
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

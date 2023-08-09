#!/usr/bin/python3
"""Create a FileStorage instance for the application"""
from models.engine.file_storage import FileStorage

"""Create variable storage, and FileStorage instance"""
storage = FileStorage()
storage.reload()

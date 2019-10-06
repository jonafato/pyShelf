#!/usr/bin/python
import sys
from PIL import Image
sys.path.insert(1, 'lib/')
from pyShelf import InitFiles, Epub
from config import Config
from library import Catalogue

config = Config() # Get configuration settings
InitFiles(config.file_array) # Initialize file system
Catalogue = Catalogue() # Open the Catalogue

# This only needs to be run on first run, & when new books are added
Epub().import_books() # Filter Your books
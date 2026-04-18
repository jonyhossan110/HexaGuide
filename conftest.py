"""
conftest.py — pytest configuration root.

This file ensures pytest can always discover the hexaguide package
whether running from the project root or installed via pip install -e .
"""
import sys
import os

# Add project root to sys.path so `import hexaguide` always works
sys.path.insert(0, os.path.dirname(__file__))

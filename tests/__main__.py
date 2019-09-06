#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

# Code to automatically run all tests sourced from:
# https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory

loader = unittest.TestLoader()
start_dir = '.\\tests'
suite = loader.discover(start_dir, pattern="test_*.py")

runner = unittest.TextTestRunner()
runner.run(suite)

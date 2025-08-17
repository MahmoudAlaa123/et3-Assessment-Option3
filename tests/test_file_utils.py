#!/usr/bin/env python3
"""
Tests for the File Processing Utilities.
"""

import pytest
from pathlib import Path
from word_analyzer.file_utils import FileUtils

def test_process_file_streaming_success(temp_files):
    """Checks if a valid file is processed into a word dictionary."""
    word_dict = FileUtils.process_file_streaming(temp_files['small'])
    assert isinstance(word_dict, dict)
    assert word_dict['python'] == 3
    assert word_dict['test'] == 2

def test_find_working_encoding(temp_files):
    """Ensures both utf-8 and latin-1 encodings are detected correctly."""
    assert FileUtils.find_working_encoding(temp_files['small']) == 'utf-8'
    assert FileUtils.find_working_encoding(temp_files['empty']) == 'utf-16'

def test_file_validation_errors(temp_files):
    """Ensures the correct errors are raised for invalid paths."""
    non_existent_file = temp_files['dir'] / "fake.txt"
    
    with pytest.raises(FileNotFoundError):
        FileUtils.validate_file(non_existent_file)
        
    with pytest.raises(ValueError):
        FileUtils.validate_file(temp_files['dir'])

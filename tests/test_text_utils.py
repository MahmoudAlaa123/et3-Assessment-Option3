#!/usr/bin/env python3
"""
Tests for the Text Processing Utilities.
"""

import pytest
from word_analyzer.text_utils import TextUtils

@pytest.mark.parametrize("input_text, expected_words", [
    ("Hello, World! This is a test.", ["hello", "world", "this", "is", "a", "test"]),
    ("Don't fail this test123...", ["don't", "fail", "this", "test"]),
    ("مرحبا بالعالم", ["مرحبا", "بالعالم"]),
    ("English and عربي", ["english", "and", "عربي"]),
    ("", []),
])
def test_clean_text(input_text, expected_words):
    assert TextUtils.clean_text(input_text) == expected_words
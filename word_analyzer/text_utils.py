#!/usr/bin/env python3
"""
Text Processing Utilities for the Word Frequency Analyzer.

This module provides functions for cleaning text and extracting words
using regular expressions.
"""

import re
from typing import List

class TextUtils:
    """Handles text cleaning and word extraction."""
    
    # Regex pattern for word extraction (English and Arabic)
    WORD_PATTERN = re.compile(r"[a-zA-Z\u0621-\u064A]+(?:'[a-zA-Z]+)?")
    
    @staticmethod
    def clean_text(text: str) -> List[str]:
        """Extract and clean words from text."""
        return TextUtils.WORD_PATTERN.findall(text.lower())

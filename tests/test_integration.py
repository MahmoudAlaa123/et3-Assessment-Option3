#!/usr/bin/env python3
"""
Integration tests for the Word Frequency Analyzer.
"""

import pytest
from word_analyzer.main import WordFrequencyAnalyzer

@pytest.fixture(scope="module")
def analyzer():
    """Create a single WordFrequencyAnalyzer instance for all tests."""
    return WordFrequencyAnalyzer()

def test_full_analysis_workflow(analyzer, temp_files):
    """Tests the complete process from file input to report generation."""
    report = analyzer.generate_report(temp_files['small'], top_n=3)
    
    assert 'file_path' in report
    assert report['total_words'] == 7
    assert report['unique_words'] == 4
    assert report['top_words'] == [('python', 3), ('test', 2), ('hello', 1)]

def test_multilingual_file_workflow(analyzer, temp_files):
    """Ensures the workflow succeeds with multilingual content."""
    report = analyzer.generate_report(temp_files['arabic'], top_n=5)
    
    top_words_list = [word for word, count in report['top_words']]
    assert 'مرحبا' in top_words_list
    assert 'hello' in top_words_list
    assert 'عربي' in top_words_list

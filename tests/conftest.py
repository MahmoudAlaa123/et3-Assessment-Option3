import pytest
import tempfile
import os
from pathlib import Path


from word_analyzer.main import WordFrequencyAnalyzer 

@pytest.fixture(scope="module")
def analyzer():
    """Create a single WordFrequencyAnalyzer instance for all tests in a module."""
    return WordFrequencyAnalyzer()

@pytest.fixture(scope="module")
def temp_files():
    """Create a set of temporary files for testing and clean them up after."""
    temp_dir = tempfile.mkdtemp()
    
    files = {
        'small': Path(temp_dir) / "small.txt",
        'empty': Path(temp_dir) / "empty.txt",
        'arabic': Path(temp_dir) / "arabic.txt",
        'dir': Path(temp_dir) # For testing error cases
    }
    
    # Create the files with content
    with open(files['small'], 'w', encoding='utf-8') as f:
        f.write("Test test python. Hello world! python python.")
    with open(files['empty'], 'w', encoding='utf-16') as f:
        f.write("")
    with open(files['arabic'], 'w', encoding='utf-8') as f:
        f.write("مرحبا بالعالم. Hello and عربي.")

        
    yield files
    
    # Cleanup: Remove files and then the temporary directory
    for key in ['small', 'empty', 'arabic']:
        if files[key].exists():
            files[key].unlink()
    if Path(temp_dir).exists():
        os.rmdir(temp_dir)

@pytest.fixture
def temp_output_path():
    """
    Creates a temporary output path for a CSV file and ensures cleanup.
    """
    temp_dir = tempfile.mkdtemp()
    output_path = Path(temp_dir) / "test_output.csv"
    yield output_path
    if output_path.exists():
        output_path.unlink()
    if Path(temp_dir).exists():
        os.rmdir(temp_dir)

@pytest.fixture
def mock_analysis_data():
    """
    Provides mock data for word frequency analysis tests.
    """
    return {
        'top_words': [('python', 3), ('test', 2), ('hello', 1)],
        'file_stats': {
            'source_file': 'test.txt',
            'file_size': 100,
            'total_words': 6,
            'unique_words': 3,
            'processing_time': 0.5
        }
    }
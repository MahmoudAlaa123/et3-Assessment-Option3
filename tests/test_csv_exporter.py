import csv
from pathlib import Path
from word_analyzer.csv_exporter import CSVExporter
import pytest


def test_export_creates_file(temp_output_path: Path, mock_analysis_data):
    """
    Test that the export_to_csv method successfully creates a CSV file.
    """
    top_words = mock_analysis_data['top_words']
    file_stats = mock_analysis_data['file_stats']

    CSVExporter.export_to_csv(top_words, file_stats, temp_output_path)

    assert temp_output_path.exists()
    assert temp_output_path.is_file()


def test_export_writes_correct_content(temp_output_path: Path, mock_analysis_data):
    """
    Test that the content written to the CSV file is correct.
    """
    top_words = mock_analysis_data['top_words']
    file_stats = mock_analysis_data['file_stats']

    CSVExporter.export_to_csv(top_words, file_stats, temp_output_path)

    with open(temp_output_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        lines = list(reader)

    # Assert metadata (correct indices)
    assert lines[0] == ['Word Frequency Analysis Report']
    # Skip index 1 for the generated date
    assert lines[2][0] == 'Source file:'
    assert lines[2][1] == file_stats['source_file']
    assert lines[3][0] == 'File size (bytes):'
    assert lines[3][1] == str(file_stats['file_size'])
    assert lines[4][0] == 'Total words:'
    assert lines[4][1] == str(file_stats['total_words'])
    assert lines[5][0] == 'Unique words:'
    assert lines[5][1] == str(file_stats['unique_words'])
    
    assert lines[6][0] == 'Processing time (seconds):'
    assert float(lines[6][1]) == file_stats['processing_time']
    
    assert lines[7] == [] 
    
    assert lines[8] == ['Rank', 'Word', 'Frequency']
    
    for i, (word, count) in enumerate(top_words):
        assert lines[i + 9] == [str(i + 1), word, str(count)]
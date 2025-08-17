# Word Frequency Analyzer

A robust Python tool for analyzing word frequencies in text files with smart processing capabilities and multiple output formats.

## Option Chosen

I chose **Option 3: Word Frequency Analyzer** with all bonus features implemented.

## Features

### Core Requirements ✅
- Accepts a path to a text file
- Ignores punctuation and case sensitivity
- Displays the top 10 most frequent words with their counts

### Bonus Features ✅
- **Simple bar chart visualization** of word frequencies
- **Efficient handling of large files** using streaming processing with smart chunking
- **CSV export functionality** with detailed metadata
- **Multi-language support** (English and Arabic)
- **Multiple encoding detection** (UTF-8, UTF-16, UTF-32.)
- **Comprehensive error handling**
- **Modular architecture** with separate utilities
- **Detailed file statistics** (file size category, processing time, etc.)


## Language and Tools Used

- **Language**: Python 3
- **Libraries**: 
  - Standard library modules: `csv`, `pathlib`, `argparse`, `re`, `collections`, `datetime`
  - Testing: `pytest`
- **Architecture**: Modular object-oriented design with separate utility classes

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MahmoudAlaa123/eT3-Assessment-wordFrequencyAnalyzer.git
cd eT3-Assessment-wordFrequencyAnalyzer
```

2. No external dependencies required! Uses only Python standard library.

3. (Optional) Install pytest for running tests:
```bash
pip install pytest
```

## Project Structure

```
word-frequency-analyzer/
├── word_analyzer/
│   ├── __init__.py
│   ├── main.py              # Main orchestration and CLI
│   ├── file_utils.py        # File processing with smart chunking
│   ├── text_utils.py        # Text cleaning and word extraction
│   ├── results_formatter.py # Results display and formatting
│   └── csv_exporter.py      # CSV export functionality
├── tests/
│   ├── conftest.py          # Test fixtures
│   ├── test_csv_exporter.py
│   ├── test_file_utils.py
│   ├── test_integration.py
│   ├── test_text_utils.py
├── sample.txt               # Example text file
└── README.md
```

## How to Run

### Basic Usage
```bash
python3 -m word_analyzer.main sample.txt
```

### Advanced Options
```bash
# Show top 20 words with bar chart
python3 -m word_analyzer.main sample.txt --top 20 --chart

# Export results to CSV
python3 -m word_analyzer.main sample.txt --export-csv results.csv

# Combine all features
python3 -m word_analyzer.main large_file.txt --top 15 --chart --export-csv analysis.csv
```

### Command-line Options
- `file_path`: Path to the text file to analyze (required)
- `--top N`: Number of top words to display (default: 10)
- `--chart`: Display a bar chart of word frequencies
- `--export-csv PATH`: Export results to CSV file at specified path

### Example Output
```
Analyzing file: sample.txt

File Statistics:
File size: 1,234 bytes (Small file)
Total words: 256
Unique words: 89
Processing time: 0.05 seconds

Top 10 Most Frequent Words:
========================================
 1. the        42 occurrences
    ██████████████████████████████
 2. and        31 occurrences
    ██████████████████████
 3. to         28 occurrences
    ████████████████████
 4. of         25 occurrences
    ██████████████████
 5. a          22 occurrences
    ████████████████
...

Results exported to: results.csv
```

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_integration.py
```

## File Processing Intelligence

The analyzer automatically optimizes processing based on file size:
- **Small files** (< 1MB): 4KB chunks
- **Medium files** (1MB - 50MB): 16KB chunks  
- **Large files** (> 50MB): 64KB chunks

This ensures efficient memory usage and processing speed for files of any size.

## Supported Text Formats

- **Encodings**: UTF-8,  UTF-16, UTF-32 (auto-detected)
- **Languages**: English, Arabic (extensible regex pattern)
- **Word Recognition**: Handles contractions (e.g., "don't", "it's")

## Error Handling

Robust error handling for common scenarios:
- File not found or permission errors
- Encoding detection failures
- Invalid command-line arguments


## Example Files

Create a sample text file to test:

```bash
echo "submission of Assessment, assessment of mahmoud alaa, test123" > sample.txt
python -m word_analyzer.main sample.txt --chart
```


#!/usr/bin/env python3
"""
Main script for the Enhanced Word Frequency Analyzer.

This script orchestrates the file processing, text analysis, and results
formatting. It also provides the command-line interface for the tool.
"""

import argparse
import sys
import time
from pathlib import Path
from typing import List, Tuple, Dict

# Use relative imports for modular structure
from .file_utils import FileUtils
from .text_utils import TextUtils
from .results_formatter import ResultsFormatter
from .csv_exporter import CSVExporter

class WordFrequencyAnalyzer:
    """Orchestrates the word frequency analysis workflow."""
    
    def generate_report(self, file_path: Path, top_n: int = 10, 
                       show_chart: bool = False, export_csv: str = None) -> Dict:
        """Generate a complete word frequency report."""
        start_time = time.time()
        try:
            print(f"Analyzing file: {file_path}")
            word_counter = FileUtils.process_file_streaming(file_path)
            top_words = ResultsFormatter.get_top_words(word_counter, top_n)
            
            file_size = file_path.stat().st_size
            total_words = sum(word_counter.values())
            unique_words = len(word_counter)
            processing_time = time.time() - start_time
            
            if file_size <= FileUtils.SMALL_FILE_LIMIT:
                size_category = "Small"
            elif file_size <= FileUtils.MEDIUM_FILE_LIMIT:
                size_category = "Medium"
            else:
                size_category = "Large"
            
            print(f"\nFile Statistics:")
            print(f"File size: {file_size:,} bytes ({size_category} file)")
            print(f"Total words: {total_words:,}")
            print(f"Unique words: {unique_words:,}")
            print(f"Processing time: {processing_time:.2f} seconds")
            
            ResultsFormatter.display_results(top_words, show_chart)
            
            # Export to CSV if requested
            if export_csv:
                csv_path = Path(export_csv)
                CSVExporter.export_to_csv(
                    top_words=top_words,
                    file_stats={
                        'source_file': str(file_path),
                        'file_size': file_size,
                        'total_words': total_words,
                        'unique_words': unique_words,
                        'processing_time': processing_time
                    },
                    output_path=csv_path
                )
                print(f"\nResults exported to: {csv_path}")
            
            return {
                'file_path': str(file_path), 'file_size': file_size,
                'size_category': size_category, 'total_words': total_words,
                'unique_words': unique_words, 'top_words': top_words,
                'processing_time': processing_time
            }
        except (FileNotFoundError, PermissionError, ValueError, IOError) as e:
            print(f"Error: {e}", file=sys.stderr)
            return {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}", file=sys.stderr)
            return {}

def main():
    """Main function for the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Analyze word frequencies in text files with smart processing.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('file_path', type=str, help='Path to the text file to analyze.')
    parser.add_argument('--top', type=int, default=10, metavar='N', help='Number of top words to display.')
    parser.add_argument('--chart', action='store_true', help='Display a bar chart of word frequencies.')
    parser.add_argument('--export-csv', type=str, metavar='PATH', help='Export results to CSV file at specified path.')
    
    args = parser.parse_args()
    
    if args.top <= 0:
        print("Error: --top must be a positive integer.", file=sys.stderr)
        sys.exit(1)
    
    analyzer = WordFrequencyAnalyzer()
    file_path = Path(args.file_path)
    
    if not analyzer.generate_report(
        file_path=file_path, 
        top_n=args.top, 
        show_chart=args.chart,
        export_csv=args.export_csv
    ):
        sys.exit(1)

if __name__ == "__main__":
    main()
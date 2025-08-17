#!/usr/bin/env python3
"""
CSV Export Utilities for the Word Frequency Analyzer.

This module handles exporting word frequency results to CSV format
with metadata and proper formatting.
"""

import csv
from pathlib import Path
from typing import List, Tuple, Dict
from datetime import datetime

class CSVExporter:
    """Handles exporting word frequency results to CSV files."""
    
    @staticmethod
    def export_to_csv(top_words: List[Tuple[str, int]], file_stats: Dict, output_path: Path) -> None:
        """
        Export word frequency results to a CSV file.
        
        Args:
            top_words: List of (word, count) tuples
            file_stats: Dictionary containing file statistics
            output_path: Path where the CSV file will be saved
        """
        # Validate file extension
        if output_path.suffix.lower() != '.csv':
            raise ValueError(f"Output file must have .csv extension, got: {output_path.suffix}")
        
        try:
            
            
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write metadata header
                writer.writerow(['Word Frequency Analysis Report'])
                writer.writerow(['Generated on:', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
                writer.writerow(['Source file:', file_stats['source_file']])
                writer.writerow(['File size (bytes):', file_stats['file_size']])
                writer.writerow(['Total words:', file_stats['total_words']])
                writer.writerow(['Unique words:', file_stats['unique_words']])
                writer.writerow(['Processing time (seconds):', f"{file_stats['processing_time']:.2f}"])
                writer.writerow([])  # Empty row separator
                
                # Write column headers  
                writer.writerow(['Rank', 'Word', 'Frequency'])
                
                # Write word frequency data
                for rank, (word, count) in enumerate(top_words, 1):
                    writer.writerow([rank, word, count])
                
        except PermissionError:
            raise PermissionError(f"No write permission for output path: {output_path}")
        except Exception as e:
            raise IOError(f"Failed to write CSV file {output_path}: {e}")
    

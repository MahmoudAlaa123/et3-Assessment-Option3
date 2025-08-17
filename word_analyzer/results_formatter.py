#!/usr/bin/env python3
"""
Results Formatting Utilities for the Word Frequency Analyzer.

This module handles the sorting, formatting, and display of the
word frequency analysis results.
"""

from typing import List, Tuple, Dict

class ResultsFormatter:
    """Handles formatting and displaying results."""
    
    @staticmethod
    def get_top_words(word_counter: Dict[str, int], n: int = 10) -> List[Tuple[str, int]]:
        """Get top N most frequent words, sorted alphabetically in case of a tie."""
        sorted_items = sorted(
            word_counter.items(),
            key=lambda x: (-x[1], x[0]) # Sort by count (desc) then word (asc)
        )
        return sorted_items[:n]
    
    @staticmethod
    def display_results(top_words: List[Tuple[str, int]], show_chart: bool = False) -> None:
        """Display word frequency results in a formatted table."""
        if not top_words:
            print("No words found in the file.")
            return
        
        print(f"\nTop {len(top_words)} Most Frequent Words:")
        print("=" * 40)
        
        max_count = max(count for _, count in top_words) if top_words else 1
        
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i:2d}. {word:<15} {count:>6} occurrences")
            
            if show_chart:
                bar_length = int((count / max_count) * 30)
                bar = "█" * bar_length
                print(f"    {bar}")

#!/usr/bin/env python3
"""
File Processing Utilities for the Word Frequency Analyzer.

This module contains functions for validating, reading, and processing files
with a focus on efficiency and robust error handling.
"""

from pathlib import Path
from typing import Dict, Generator
from collections import defaultdict
from .text_utils import TextUtils # Use relative import

class FileUtils:
    """Handles file reading with smart chunking and encoding detection."""
    
    SMALL_FILE_LIMIT = 1024 * 1024      # 1MB
    MEDIUM_FILE_LIMIT = 50 * 1024 * 1024  # 50MB
    
    SMALL_CHUNK = 4096      # 4KB
    MEDIUM_CHUNK = 16384    # 16KB
    LARGE_CHUNK = 65536     # 64KB
    
    ENCODINGS_TO_TRY = ['utf-8', 'utf-16', 'utf-32']
    
    @staticmethod
    def validate_file(file_path: Path) -> None:
        """Validate file existence and permissions."""
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not file_path.is_file():
            raise ValueError(f"Path is not a regular file: {file_path}")
        if not file_path.stat().st_mode & 0o400:
            raise PermissionError(f"No read permission for file: {file_path}")

    @staticmethod
    def find_working_encoding(file_path: Path) -> str:
        """Find a working encoding by testing each one."""
        for encoding in FileUtils.ENCODINGS_TO_TRY:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    f.read(1024)
                return encoding
            except (UnicodeDecodeError, UnicodeError):
                continue
        raise IOError(f"Could not determine a working encoding for {file_path}")

    @staticmethod
    def get_chunk_size(file_size: int) -> int:
        """Determine optimal chunk size based on file size."""
        if file_size <= FileUtils.SMALL_FILE_LIMIT:
            return FileUtils.SMALL_CHUNK
        elif file_size <= FileUtils.MEDIUM_FILE_LIMIT:
            return FileUtils.MEDIUM_CHUNK
        else:
            return FileUtils.LARGE_CHUNK

    @staticmethod
    def read_file_chunks(file_path: Path, encoding: str, chunk_size: int) -> Generator[str, None, None]:
        """Generator that yields file chunks."""
        with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    @staticmethod
    def process_file_streaming(file_path: Path) -> Dict[str, int]:
        """Process a file in a streaming fashion."""
        FileUtils.validate_file(file_path)
        
        file_size = file_path.stat().st_size
        chunk_size = FileUtils.get_chunk_size(file_size)
        encoding = FileUtils.find_working_encoding(file_path)
        
        word_counter = defaultdict(int)
        try:
            for chunk in FileUtils.read_file_chunks(file_path, encoding, chunk_size):
                words = TextUtils.clean_text(chunk)
                for word in words:
                    word_counter[word] += 1
            return dict(word_counter)
        except Exception as e:
            raise IOError(f"Failed to read {file_path} with encoding {encoding}: {e}")

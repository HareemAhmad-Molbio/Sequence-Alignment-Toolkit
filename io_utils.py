"""
Input/output utilities for FASTA files.
"""

from pathlib import Path
from Bio import SeqIO


def is_fasta_file(path):
    """
    Return True if the input looks like a FASTA file.
    """

    return Path(path).suffix.lower() in {
        ".fa",
        ".fasta",
        ".fna",
    }


def read_fasta_sequence(path):
    """
    Read the first sequence from a FASTA file.
    """

    records = list(SeqIO.parse(path, "fasta"))

    if not records:
        raise ValueError("No sequences found in FASTA file.")

    return str(records[0].seq).upper()
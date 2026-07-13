import argparse
from algorithms import (
    initialize_matrix,
    calculate_score,
    fill_matrix,
    traceback,
)

from io_utils import (
    is_fasta_file,
    read_fasta_sequence,
)

from formatter import format_alignment

from visualization import plot_score_matrix

from scoring import (
    MATCH_SCORE,
    MISMATCH_SCORE,
    GAP_PENALTY,
)


def main():

    parser = argparse.ArgumentParser(
        description="Global Sequence Alignment using Needleman-Wunsch"
    )

    parser.add_argument(
        "sequence1",
        help="First DNA sequence",
    )

    parser.add_argument(
        "sequence2",
        help="Second DNA sequence",
    )

    args = parser.parse_args()

    if is_fasta_file(args.sequence1):
        seq1 = read_fasta_sequence(args.sequence1)
    else:
        seq1 = args.sequence1.upper()

    if is_fasta_file(args.sequence2):
        seq2 = read_fasta_sequence(args.sequence2)
    else:
        seq2 = args.sequence2.upper()

    valid = set("ACGT")

    for sequence in [seq1, seq2]:

        if not set(sequence).issubset(valid):

            raise ValueError(
                "Sequences must contain only A, C, G and T."
            )
        
    print("Sequence Alignment Toolkit")
    print("=" * 35)

    print(f"Sequence 1 : {seq1}")
    print(f"Sequence 2 : {seq2}")

    print()

    matrix = initialize_matrix(
        len(seq1) + 1,
        len(seq2) + 1,
        GAP_PENALTY,
    )

    matrix = fill_matrix(
        matrix,
        seq1,
        seq2,
        MATCH_SCORE,
        MISMATCH_SCORE,
        GAP_PENALTY,
    )

    aligned_seq1, aligned_seq2,traceback_path = traceback(
        matrix,
        seq1,
        seq2,
        MATCH_SCORE,
        MISMATCH_SCORE,
        GAP_PENALTY,
    )
    
    alignment = format_alignment(
        aligned_seq1,
        aligned_seq2,
    )

    print("Completed Score Matrix\n")
    print(matrix)

    print("\nTraceback Path")
    print("----------------")
    print(traceback_path)

    print("\nOptimal Alignment")
    print("-----------------")

    print(alignment["top"])
    print(alignment["middle"])
    print(alignment["bottom"])

    print()

    print(f"Matches     : {alignment['matches']}")
    print(f"Mismatches  : {alignment['mismatches']}")
    print(f"Gaps        : {alignment['gaps']}")
    print(f"Identity    : {alignment['identity']:.2f}%")

    plot_score_matrix(
        matrix,
        seq1,
        seq2,
        "output/score_matrix_heatmap.png",
        traceback_path,
    )

    print("\nScore matrix heatmap saved to output/score_matrix_heatmap.png")
 

if __name__ == "__main__":
    main()
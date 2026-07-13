from algorithms import (
    initialize_matrix,
    calculate_score,
    fill_matrix,
)

from scoring import (
    MATCH_SCORE,
    MISMATCH_SCORE,
    GAP_PENALTY,
)


def main():

    seq1 = "ACT"

    seq2 = "AT"

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
    
    print("Completed Score Matrix\n")
    print(matrix)

    
if __name__ == "__main__":
    main()
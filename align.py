from algorithms import (
    initialize_matrix,
    calculate_score,
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

    diagonal = matrix[0][0] + MATCH_SCORE

    up = matrix[0][1] + GAP_PENALTY

    left = matrix[1][0] + GAP_PENALTY

    score = calculate_score(
        diagonal,
        up,
        left,
    )
    print("Initialized Matrix\n")
    print(matrix)

    print("\nPossible Scores")
    print("----------------")
    print("Diagonal :", diagonal)
    print("Up       :", up)
    print("Left     :", left)

    print("\nSelected Score :", score)

if __name__ == "__main__":
    main()
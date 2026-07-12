from algorithms import initialize_matrix
from scoring import GAP_PENALTY


def main():

    seq1 = "ACT"

    seq2 = "AT"

    matrix = initialize_matrix(
        len(seq1) + 1,
        len(seq2) + 1,
        GAP_PENALTY,
    )

    print("Initialized Score Matrix\n")

    print(matrix)


if __name__ == "__main__":
    main()
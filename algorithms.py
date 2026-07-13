import numpy as np


def initialize_matrix(rows, cols, gap_penalty):
    """
    Create and initialize the Needleman-Wunsch scoring matrix.

    Parameters
    ----------
    rows : int
        Number of rows.

    cols : int
        Number of columns.

    gap_penalty : int
        Penalty for introducing a gap.

    Returns
    -------
    numpy.ndarray
        Initialized scoring matrix.
    """

    matrix = np.zeros((rows, cols), dtype=int)

    # Initialize first column
    for i in range(rows):
        matrix[i][0] = i * gap_penalty

    # Initialize first row
    for j in range(cols):
        matrix[0][j] = j * gap_penalty

    return matrix


def calculate_score(
    diagonal,
    up,
    left,
):
    """
    Return the maximum of the three possible scores.
    """

    return max(
        diagonal,
        up,
        left,
    )

def fill_matrix(
    matrix,
    seq1,
    seq2,
    match_score,
    mismatch_score,
    gap_penalty,
):
    """
    Fill the Needleman-Wunsch score matrix.
    """

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    for i in range(1, rows):

        for j in range(1, cols):

            if seq1[i - 1] == seq2[j - 1]:
                score = match_score
            else:
                score = mismatch_score

            diagonal = matrix[i - 1][j - 1] + score
            up = matrix[i - 1][j] + gap_penalty
            left = matrix[i][j - 1] + gap_penalty

            matrix[i][j] = calculate_score(
                diagonal,
                up,
                left,
            )

    return matrix
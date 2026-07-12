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


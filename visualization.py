import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def plot_score_matrix(
    matrix,
    seq1,
    seq2,
    output_file,
):
    """
    Plot the Needleman-Wunsch score matrix as a heatmap.
    """

    fig, ax = plt.subplots(
        figsize=(11, 8)
    )

    image = ax.imshow(
        matrix,
        cmap="YlGnBu",
        origin="upper",
        interpolation="nearest",
        aspect="equal",
    )

    ax.set_xticks(
        np.arange(-0.5, matrix.shape[1], 1),
        minor=True,
    )

    ax.set_yticks(
        np.arange(-0.5, matrix.shape[0], 1),
        minor=True,
    )

    ax.grid(
        which="minor",
        color="white",
        linestyle="-",
        linewidth=1.5,
    )

    ax.tick_params(
        which="minor",
        bottom=False,
        left=False,
    )

    cbar = plt.colorbar(
        image,
        ax=ax,
        shrink=0.9,
    )

    cbar.set_label(
        "Alignment Score",
        fontsize=12,
        fontweight="bold",
    )

    x_labels = ["-"] + list(seq2)
    y_labels = ["-"] + list(seq1)

    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_yticks(np.arange(len(y_labels)))

    ax.set_xticklabels(
    x_labels,
    fontsize=12,
    fontweight="bold",
)

    ax.set_yticklabels(
        y_labels,
        fontsize=12,
        fontweight="bold",
    )

    ax.set_xlabel(
        "Sequence 2",
        fontsize=13,
        fontweight="bold",
    )

    ax.set_ylabel(
        "Sequence 1",
        fontsize=13,
        fontweight="bold",
    )

    ax.set_title(
        "Needleman–Wunsch Dynamic Programming Score Matrix",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):

            normalized = image.norm(matrix[i, j])

            color = (
                "white"
                if normalized > 0.5
                else "black"
            )

            ax.text(
                j,
                i,
                f"{matrix[i, j]}",
                ha="center",
                va="center",
                fontsize=11,
                fontweight="bold",
                color=color,
            )

    plt.tight_layout()

    output_path = Path(output_file)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    svg_path = output_path.with_suffix(".svg")

    plt.savefig(
        svg_path,
        bbox_inches="tight",
    )

    plt.close()
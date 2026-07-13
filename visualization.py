import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def plot_score_matrix(
    matrix,
    seq1,
    seq2,
    output_file,
    traceback_path,
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

    if traceback_path:

        rows = [p[0] for p in traceback_path]
        cols = [p[1] for p in traceback_path]

        ax.plot(
            cols,
            rows,
            color="red",
            linewidth=3,
            marker="o",
            markersize=6,
            markerfacecolor="red",
            markeredgecolor="white",
            zorder=10,
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


def plot_alignment(
    aligned_seq1,
    aligned_seq2,
    matches,
    mismatches,
    gaps,
    identity,
    output_file,
):
    """
    Create a publication-style alignment figure.
    """

    from pathlib import Path

    fig, ax = plt.subplots(figsize=(14, 4))

    ax.set_xlim(0, len(aligned_seq1) + 8)
    ax.set_ylim(-1, 5)

    ax.axis("off")

    ax.set_title(
        "Optimal Global Alignment",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    ax.text(
        0,
        3,
        "Sequence 1 :",
        fontsize=13,
        fontweight="bold",
        family="monospace",
    )

    ax.text(
        0,
        1,
        "Sequence 2 :",
        fontsize=13,
        fontweight="bold",
        family="monospace",
    )

    start_x = 5

    for i, (b1, b2) in enumerate(zip(aligned_seq1, aligned_seq2)):

        x = start_x + i

        if b1 == b2:

            color = "forestgreen"
            symbol = "|"

        elif b1 == "-" or b2 == "-":

            color = "red"
            symbol = " "

        else:

            color = "darkorange"
            symbol = "."

        ax.text(
            x,
            3,
            b1,
            color=color,
            fontsize=16,
            family="monospace",
            fontweight="bold",
        )

        ax.text(
            x,
            2,
            symbol,
            color=color,
            fontsize=16,
            family="monospace",
            fontweight="bold",
        )

        ax.text(
            x,
            1,
            b2,
            color=color,
            fontsize=16,
            family="monospace",
            fontweight="bold",
        )

    ax.text(
        0,
        -0.2,
        f"Identity : {identity:.2f}%",
        fontsize=12,
        family="monospace",
    )

    ax.text(
        0,
        -0.7,
        f"Matches : {matches}",
        fontsize=12,
        family="monospace",
    )

    ax.text(
        6,
        -0.7,
        f"Mismatches : {mismatches}",
        fontsize=12,
        family="monospace",
    )

    ax.text(
        15,
        -0.7,
        f"Gaps : {gaps}",
        fontsize=12,
        family="monospace",
    )

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    plt.savefig(
        output_path.with_suffix(".svg"),
        bbox_inches="tight",
    )

    plt.close()


def plot_alignment_statistics(
    matches,
    mismatches,
    gaps,
    identity,
    output_file,
):
    """
    Create a summary chart for alignment statistics.
    """

    from pathlib import Path

    labels = [
        "Matches",
        "Mismatches",
        "Gaps",
    ]

    values = [
        matches,
        mismatches,
        gaps,
    ]

    fig, ax = plt.subplots(figsize=(7, 5))

    bars = ax.bar(
        labels,
        values,
        color=[
            "forestgreen",
            "darkorange",
            "firebrick",
        ],
    )

    ax.set_title(
        "Alignment Statistics",
        fontsize=18,
        fontweight="bold",
        pad=15,
    )

    ax.set_ylabel(
        "Count",
        fontsize=12,
        fontweight="bold",
    )

    ax.set_ylim(
        0,
        max(values) + 2,
    )

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1,
            str(int(height)),
            ha="center",
            fontsize=11,
            fontweight="bold",
        )

    ax.text(
        0.98,
        0.95,
        f"Identity: {identity:.2f}%",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=12,
        fontweight="bold",
        bbox=dict(
            boxstyle="round",
            facecolor="white",
            edgecolor="gray",
        ),
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

    plt.savefig(
        output_path.with_suffix(".svg"),
        bbox_inches="tight",
    )

    plt.close()
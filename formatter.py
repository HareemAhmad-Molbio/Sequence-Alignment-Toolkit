def format_alignment(seq1, seq2):
    """
    Format an alignment with match indicators.
    """

    middle = []

    matches = 0
    mismatches = 0
    gaps = 0

    for a, b in zip(seq1, seq2):

        if a == b:
            middle.append("|")
            matches += 1

        elif a == "-" or b == "-":
            middle.append(" ")
            gaps += 1

        else:
            middle.append(".")
            mismatches += 1

    identity = (matches / len(seq1)) * 100

    return {
        "top": seq1,
        "middle": "".join(middle),
        "bottom": seq2,
        "matches": matches,
        "mismatches": mismatches,
        "gaps": gaps,
        "identity": identity,
    }
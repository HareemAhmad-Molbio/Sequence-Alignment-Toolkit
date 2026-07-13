# 🧬 Sequence Alignment Toolkit

A Python-based bioinformatics toolkit that implements the **Needleman–Wunsch global sequence alignment algorithm** from scratch. The toolkit aligns DNA sequences provided either directly from the command line or through FASTA files and generates detailed alignment statistics.

---

## ✨ Features

- ✅ Needleman–Wunsch Global Sequence Alignment
- ✅ Dynamic Programming Score Matrix
- ✅ Matrix Initialization
- ✅ Matrix Filling Algorithm
- ✅ Traceback Algorithm
- ✅ Optimal Alignment Reconstruction
- ✅ Alignment Statistics
  - Matches
  - Mismatches
  - Gaps
  - Sequence Identity (%)
- ✅ Command-Line Interface (CLI)
- ✅ DNA Sequence Validation
- ✅ FASTA File Support
- ✅ Modular Python Architecture

---

## 📂 Project Structure

```
Sequence-Alignment-Toolkit/
│
├── align.py                # Main command-line application
├── algorithms.py           # Needleman-Wunsch algorithm
├── formatter.py            # Alignment formatting & statistics
├── io_utils.py             # FASTA file handling
├── scoring.py              # Scoring configuration
├── sample_data/
│   ├── human.fasta
│   └── mouse.fasta
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/HareemAhmad-Molbio/Sequence-Alignment-Toolkit.git

cd Sequence-Alignment-Toolkit
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

- Python 3.10+
- NumPy
- Biopython

Install manually

```bash
pip install numpy biopython
```

---

# 🚀 Usage

## Align two DNA sequences

```bash
python align.py ACT AT
```

---

## Align two FASTA files

```bash
python align.py sample_data/human.fasta sample_data/mouse.fasta
```

---

## Example Output

```text
Sequence Alignment Toolkit
======================================

Sequence 1 : ACTGACTGA
Sequence 2 : ACTTACTGA

Completed Score Matrix

[[  0  -2  -4  -6  -8 -10 -12 -14 -16 -18]
 [ -2   1  -1  -3  -5  -7  -9 -11 -13 -15]
 [ -4  -1   2   0  -2  -4  -6  -8 -10 -12]
 ...
]

Optimal Alignment
-----------------

ACTGACTGA
|||.|||||
ACTTACTGA

Matches      : 8
Mismatches   : 1
Gaps         : 0
Identity     : 88.89%
```

---

# 🧬 Needleman–Wunsch Algorithm

The toolkit implements the classical **Needleman–Wunsch dynamic programming algorithm** for global sequence alignment.

### Workflow

1. Initialize scoring matrix
2. Apply gap penalties
3. Fill matrix using dynamic programming
4. Perform traceback
5. Reconstruct optimal alignment
6. Calculate alignment statistics

---

# 📊 Alignment Statistics

The toolkit automatically reports

- Number of Matches
- Number of Mismatches
- Number of Gaps
- Percentage Sequence Identity

---

# 📁 Sample Data

Example FASTA files are provided in

```
sample_data/
```

Example

```
human.fasta
mouse.fasta
```

These can be used immediately after cloning the repository.

---

# 🖼️ Screenshots

## Global Sequence Alignment

```
screenshots/alignment_output.png
```

## Dynamic Programming Score Matrix

```
screenshots/score_matrix.png
```

*(Screenshots will be added as the visualization module is completed.)*

---

# 🛠️ Current Capabilities

| Feature | Status |
|----------|--------|
| Global Alignment | ✅ |
| Needleman–Wunsch | ✅ |
| Dynamic Programming | ✅ |
| Traceback | ✅ |
| FASTA Support | ✅ |
| Command-Line Interface | ✅ |
| Alignment Statistics | ✅ |
| DNA Validation | ✅ |

---

# 🚧 Planned Features

The following features are currently under development.

- 📊 Score Matrix Heatmap
- 🎨 Traceback Path Visualization
- 📈 Alignment Statistics Charts
- 🧬 Smith–Waterman Local Alignment
- 🧪 Protein Sequence Alignment
- 🧬 BLOSUM62 Scoring Matrix
- 📄 HTML Alignment Reports
- 📑 PDF Export
- 🧪 Unit Testing
- ⚡ GitHub Actions CI/CD

---

# 📚 Technologies Used

- Python
- NumPy
- Biopython
- Dynamic Programming
- Sequence Alignment Algorithms
- Command-Line Interface (CLI)

---

# 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

# 👨‍💻 Author

**Hareem Ahmad**

Molecular Biology & Biochemistry Graduate

Bioinformatics | Computational Biology | Python | Sequence Analysis | Genomics

GitHub

https://github.com/HareemAhmad-Molbio
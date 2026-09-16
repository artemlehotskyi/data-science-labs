<div align="center">

# 📊 Data Science Labs

**Hands-on Python notebooks: from core algorithms to NumPy, pandas, visualization and optimization.**

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)

</div>

---

## About

A collection of practical Data Science exercises, each solved in a Jupyter notebook.
The focus is on writing clean, typed, readable Python and understanding *why* a solution
works — not just getting the right number.

Principles followed across the labs:

- **Vectorize where it matters** — NumPy operations instead of Python loops
- **Type hints and input validation** on every function
- **Reproducibility** — fixed random seeds, results visible directly in the notebook

## Labs

| # | Topic | Key skills | Status |
|:-:|-------|-----------|:------:|
| 01 | Python fundamentals | Taylor series approximation, list processing, string transformation | ✅ |
| 02 | NumPy vectorization | Loop-free computation, boolean masks, array transforms | ⏳ |
| 03 | Linear algebra | Matrix operations without built-in aggregations | ⏳ |
| 04 | Data analysis with pandas | Filtering and aggregating a real dataset (Titanic) | ⏳ |
| 05 | Data visualization | Bar charts, function plots with Matplotlib | ⏳ |
| 06 | Optimization | Gradient descent for one and several variables | ⏳ |

## Repository structure

```
data-science-labs/
├── lab-01/          # one folder per lab: notebook + data it needs
├── lab-02/
├── ...
├── requirements.txt
└── README.md
```

## Getting started

```bash
git clone https://github.com/artemlehotskyi/data-science-labs.git
cd data-science-labs

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

jupyter lab
```

## Tech stack

- **Python 3.14**
- **Jupyter Lab** — interactive notebooks
- **NumPy** — numerical computing
- **pandas** — tabular data analysis
- **Matplotlib / Seaborn** — visualization

---

<div align="center">

Made by [Artem Lehotskyi](https://github.com/artemlehotskyi)

</div>

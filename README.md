# Introduction to Machine Learning 

Welcome to the repository for the "Introduction to Machine Learning " course offered at [ESMT](https://esmt.berlin/) to students in the [Master of Analytics and AI](https://esmt.berlin/degrees/master-programs/master-analytics-artificial-intelligence) master program. 

This repository augments the lecture by providing access to all materials for the practice sessions.

For enrolled students, additional resources, updates, and discussions are available on  [Canvas page](https://canvas.esmt.berlin/courses/794).

## Installation

This repository requires **Python 3.14**. Clone the repository, then choose one of the installation methods below:

```bash
git clone https://github.com/stefanlessmann/ESMT_IML.git
cd ESMT_IML
```

### Option 1: Using `uv` (recommended)

If you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed:

```bash
uv sync
```

**Advantages:** Fast, reliable, automatically handles Python 3.14 if not present.  
**Install uv:** See [installation guide](https://docs.astral.sh/uv/getting-started/installation/) (macOS: `brew install uv`, Windows/Linux: follow docs)

### Option 2: Using `pip`

If you prefer the standard Python package manager:

```bash
python -m venv .venv
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

pip install -r requirements.txt
```

**Advantages:** Widely available, minimal setup.  
**Note:** Ensure Python 3.14 is installed on your system first.

### Option 3: Using `conda`

If you use Anaconda or Miniconda:

```bash
conda env create -f environment.yml
conda activate esmt-iml
```

**Advantages:** Handles Python version and binary dependencies seamlessly.  
**Note:** Requires Anaconda, Miniconda, or Mambaforge to be installed.

## Repository Structure

```
.
├── data/        # Datasets used in the tutorials
├── handouts/    # Practice-session demos, exercises, and solutions
├── resources/   # Images and other supporting materials
├── pyproject.toml
├── uv.lock      # Locked dependency versions
├── README.md
└── LICENSE
```

## License

This project is licensed under the terms of the [MIT License](./LICENSE).

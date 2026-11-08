# Introduction to Machine Learning 

Welcome to the repository for the "Introduction to Machine Learning " course offered at [ESMT](https://esmt.berlin/) to students in the [Master of Analytics and AI](https://esmt.berlin/degrees/master-programs/master-analytics-artificial-intelligence) master program. 

This repository augments the lecture by providing access to all materials for the practice sessions.

For enrolled students, additional resources, updates, and discussions are available on  [Canvas page](https://canvas.esmt.berlin/courses/794).

## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) first, then clone the repository and install its dependencies:

```bash
git clone https://github.com/stefanlessmann/ESMT_IML.git
cd ESMT_IML
uv sync
```

`uv sync` creates a virtual environment and installs the dependencies defined in `pyproject.toml`, using `uv.lock` to keep versions consistent. This repository requires Python 3.14.

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

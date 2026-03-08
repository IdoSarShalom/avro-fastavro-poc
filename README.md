## avro-fastavro-poc

Proof-of-concept project for using Avro and `fastavro` on Python with `uv` and `ruff`.

### Prerequisites

- **Python**: 3.9.x (the project is configured for 3.9)
- **uv**: fast Python package and environment manager  
  - Install from the official installer (see `uv` docs), for example on Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Make sure `uv` is on your `PATH` (restart your shell if needed).

### Running the example

From the project root:

```bash
uv run python src/main.py
```

On first run, `uv` will:

- Create a `.venv` virtual environment in the project root.
- Install the dependencies defined in `pyproject.toml` (including `avro` and `fastavro`).

The script will:

- Write two example user records to an Avro file named `users.avro`.
- Read the records back and print them to the console.
- Print the absolute path to the generated `users.avro` file.

### Linting with Ruff

To run Ruff using the development dependency group:

```bash
uv run --group dev ruff check .
```

# Avro / fastavro PoC (Python 3.9.6)

This is a minimal "go-to" project that demonstrates using both **avro** (Apache reference
implementation) and **fastavro** (high‑performance implementation) on Python 3.9.6, with
`uv` for environment management and `ruff` for linting.

## Requirements

- Python 3.9.x (tested with 3.9.6)
- `uv` installed (see https://docs.astral.sh/uv/)

## Quick start

```bash
# Create & sync the virtualenv
uv venv --python 3.9
uv sync

# Run the PoC script
uv run python -m src.main

# Run Ruff lint
uv run ruff check src tests
```

## Offline install with wheels

The `wheels/` directory contains pinned wheels for Linux compatible with Python 3.9:

- `avro==1.12.1`
- `fastavro==1.12.1`
- `ruff==0.15.4` (dev-only)

To install from local wheels only:

```bash
python3.9 -m venv .venv
source .venv/bin/activate
pip install --no-index --find-links=./wheels \
  avro==1.12.1 fastavro==1.12.1 ruff==0.15.4
```

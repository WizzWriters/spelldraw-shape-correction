# Project Setup with Poetry

This guide provides step-by-step instructions to set up the project using [Poetry](https://python-poetry.org/), a dependency management tool for Python.

## 1. Install Poetry

If you don't have Poetry installed, you can install it using the official installation script:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

Alternatively, if you are using Windows, run:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

After installation, verify that Poetry is installed:

```sh
poetry --version
```

## 2. Enable the `poetry shell` Plugin

Poetry requires a plugin to use `poetry shell`. Install it with:

```sh
poetry self add poetry-plugin-shell
```

## 3. Install Project Dependencies

Navigate to the project directory and install dependencies:

```sh
poetry install
```

This will create a virtual environment (if not already created) and install all dependencies defined in `pyproject.toml`.

## 4. Activate the Virtual Environment

To activate the Poetry-managed virtual environment, run:

```sh
poetry shell
```

To exit the virtual environment, simply type:

```sh
exit
```

## 5. Running the Project

Once inside the virtual environment, you can run the application as follows:

```sh
python demo.py
```

## Additional Resources
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Poetry GitHub](https://github.com/python-poetry/poetry)
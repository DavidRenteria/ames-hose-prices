# Development Guide

This document contains useful commands for developing, testing, and running the House Price Prediction project.

## 1. Environment Management

Activate the Conda environment:

```bash
conda activate qml
```

Check the active Python version:

```bash
python --version
which python
```

## 2. Dependency Management

Inspect installed package versions:

```bash
python -m pip show fastapi uvicorn joblib httpx
```

List installed packages:

```bash
python -m pip list
```

Install project dependencies:

```bash
python -m pip install -r requirements.txt
```

## 3. Run FastAPI

From the project root:

```bash
python -m uvicorn app.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

## 4. Test API Endpoints

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/eda/overview
curl http://127.0.0.1:8000/eda/missing-values
curl http://127.0.0.1:8000/eda/summary
```

Note: These endpoints require the corresponding routes to be implemented.

## 5. Run Tests

```bash
python -m pytest -v
```



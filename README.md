# Dino Park Totem Calculator 🦖
![CI](https://github.com/KKasjan/DinoPark/actions/workflows/ci.yml/badge.svg)

[➡️ View on GitHub](https://github.com/KKasjan/DinoPark)

A lightweight Python tool designed to automate the calculation of resources needed to complete "Totems" in the Dino Park game. It helps players track their progress and identifies exactly how many level 1 units are missing for each dinosaur.

## 🎯 Purpose

This project was created as a practical exercise in:

- modular architecture,
- automated testing,
- static code analysis,
- CI/CD,
- JSON data persistence,
- and general development workflow.

It is part of my learning path toward becoming an Automation QA Engineer.

## 🚀 Features

- **Full-Level Input (6→1):** Enter all dinosaur levels in one flow.
- **Data Persistence:** Automatically saves each dinosaur’s levels to `dino-data.json`.
- **Existing Data Detection:** If a dinosaur already has saved levels, the app asks 
- **Modular Architecture:** Clean separation between logic, data, and user interface.
- **Automated Calculations:** Converts various dinosaur levels (1-6) into base units (Level 1) using pre-defined balance rates.
- **Unit Testing:** Integrated test suite for core logic and input validation.
  
## 📂 Project Structure 

```
DinoPark/
│
├── src/
│   └── dinopark/
│       ├── __init__.py
│       ├── main.py          # Application entry point
│       ├── logic.py         # Core mathematical engine
│       ├── ui.py            # User input/output handling
│       ├── data.py          # Dino data loading & filtering
│       ├── config.py        # Global constants & balance settings
│       └── dino-data.json   # Dinosaur definitions & statuses
│
├── tests/
│   ├── test_logic.py        # Unit tests for logic
│   └── test_ui.py           # Unit tests for UI validation
│
├── .github/workflows/ci.yml # CI pipeline (pytest, mypy, Ruff)
├── .pre-commit-config.yaml  # Pre-commit hooks
├── mypy.ini                 # Static type checking config
├── ruff.toml                # Linting & formatting rules
├── requirements.txt         # Dependencies
└── README.md
```

## 🔄 Continuous Integration (CI)

The project uses GitHub Actions to automatically run:

- tests (`pytest`)
- static analysis (`mypy`)
- linting (`ruff check`)
- formatting (`ruff format --check`)

Every push and pull request must pass the pipeline.

## 🧪 Testing
The project includes unit tests to ensure the accuracy of the core calculation engine (logic.py).
Tests are written using pytest.

**Requirements:**
- `pytest` library

**How to run tests:**
1. Install pytest (if not already installed):
```bash
pip install pytest
```
2. Run tests from the root directory:
```bash
pytest
```

## 🛠️ Technical Stack
- **Language:** Python 3.12+
- **Architecture:** Modular, layered design (UI → Logic → Data)
- **Testing Framework:** Pytest
- **Static Analysis:** mypy
- **Linting & Formating:** Ruff
- **CI/CD:** GitHub Actions

## 📋 How It Works

The application follows a simple, user-friendly workflow:

1. **Choose Dinosaur**  
   The user selects a dinosaur from the list.

2. **Check Existing Data**  
   If the dinosaur already has saved levels, the app displays them and asks whether to update.

3. **Enter Levels (6 → 1)**  
   The user enters the number of units for each level.

4. **Save to JSON**  
   All levels for the selected dinosaur are saved to `dino-data.json`.

5. **Calculate Totem Progress**  
   - Convert all levels to Level 1 equivalents using exponential scaling.
   - Sum the total.
   - Compare against the target.
   - Display how many units are missing.

### Conversion Logic (Balance Table)

Level scaling uses base‑2 exponential growth:

| Level | Value |
|-------|--------|
| 1     | 1      |
| 2     | 2      |
| 3     | 4      |
| 4     | 8      |
| 5     | 16     |
| 6     | 32     |

## 📦 Requirements
- Python 3.12+
- pip

## 💻 Installation & Usage
**Clone the repository:**

```Bash
git clone https://github.com/KKasjan/DinoPark.git
```
**Run the script:**

```Bash
python -m dinopark.main
```

## 🔮 Future Enhancements

- Web API using Flask
- GUI version (Tkinter / PySide)
- Export results to JSON/CSV
- Visualization of progress (charts)
- Multi-dino summary view
- Backup/restore of saved data

## 📈 Roadmap
[x] Add try...except blocks for input validation (Error handling).

[x] Add unit tests for core logic.

[x] Expand test coverage (UI input validation, edge cases)

[x] Add Ruff formatting & linting

[x] Add mypy static type checking

[x] Migrate to src/ project structure

[x] Implement data persistence (Save/Load from JSON file).

[ ] Add a Graphical User Interface (GUI) or a web-based dashboard.

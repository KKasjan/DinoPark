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
- working with JSON,
- and general development workflow.

It is part of my learning path toward becoming an Automation QA Engineer.

## 🚀 Features
- **Modular Architecture:** Clean separation between logic, data, and user interface.
- **Automated Calculations:** Converts various dinosaur levels (1-6) into base units (Level 1) using pre-defined balance rates.
- **Dynamic Configuration:** Automatic target calculation based on balance settings.
- **Collection Filtering:** Skips dinosaurs that already have a "Golden Chest".
- **Unit Testing:** Integrated test suite for verifying core mathematical logic and UI input validation.
  
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
- **Concepts used:** Modular Programming (File Separation), Data Isolation, Logic Decoupling.
- **Architecture:** Modular, layered design (UI → Logic → Data)
- **Testing Framework:** Pytest
- **Static Analysis:** mypy
- **Linting & Formating:** Ruff
- **CI/CD:** GitHub Actions

## 📋 How It Works
The application follows a modular data processing pipeline:

1. **Data Loading:**  
`data.py` loads dinosaur definitions from `dino-data.json` and filters out completed ones.
2. **User Input:**  
`ui.py` prompts the user for the number of units at each level (1–6).
3. **Core Logic:**  
`logic.py` converts all units to Level 1 equivalents using exponential scaling.
4. **Result Output:**  
The missing amount is calculated and displayed.

**Conversion Logic:**
Level scaling uses base‑2 exponential growth:
- Level 1 = 1
- Level 2 = 2
- Level 3 = 4
- Level 4 = 8
- Level 5 = 16
- Level 6 = 32

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
- Persistent user data (save/load)

## 📈 Roadmap
[x] Add try...except blocks for input validation (Error handling).

[x] Add unit tests for core logic.

[x] Expand test coverage (UI input validation, edge cases)

[x] Add Ruff formatting & linting

[x] Add mypy static type checking

[x] Migrate to src/ project structure

[ ] Implement data persistence (Save/Load from JSON file).

[ ] Add a Graphical User Interface (GUI) or a web-based dashboard.

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
(This structure will be updated after the planned project migration.)
- `main.py` - The central orchestrator that manages the application flow.
- `config.py` - Global settings and dynamic calculation constants.
- `logic.py` - The calculation engine (pure mathematical functions).
- `ui.py` - Handles all user interactions (input/output).
- `data.py` - The database containing dinosaur attributes and statuses.
- `test_logic.py` - Unit tests for core logic.
- `test_ui.py` - Unit tests containing mock data for inputs
- `.github/workflows/ci.yml` – GitHub Actions pipeline running tests, linting, formatting, and static analysis.
- `.pre-commit-config.yaml` – Configuration for pre-commit hooks (Ruff, formatting, linting before each commit).
- `mypy.ini` – Static type checking configuration for mypy.
- `requirements.txt` – List of Python dependencies required to run the project.
- `ruff.toml` – Configuration for Ruff (linting + formatting rules).

## 🔄 Continuous Integration (CI)
The project uses GitHub Actions to automatically run:

- tests (`pytest`)
- static analysis (`mypy`)
- linting (`ruff check`)
- formatting (`ruff format --check`)

Each push and pull request triggers a pipeline that must pass for changes to be accepted.

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
- **Language:** Python 3.x
- **Concepts used:** Modular Programming (File Separation), Data Isolation, Logic Decoupling.
- **Architecture:** Separation of concerns (UI, Logic, Data, Config).
- **Testing Framework:** Pytest

## 📋 How It Works
The application follows a modular data processing pipeline:

1. Data Extraction: The main controller fetches dinosaur records from data.py, filtering out those with a "Golden Chest".
2. User Input: For active targets, ui.py prompts the user for the quantity of units at each level (6 to 1).
3. Core Logic: The logic.py module calculates the total value in "Level 1" units using balances from config.py.
4. Result Presentation: The final missing amount is calculated and displayed back to the user via the UI module.

**Conversion Logic:**
- The system uses a base-2 exponential scaling (where Level 6 = 32 units). The TARGET is dynamically set to a full totem value (Level 7 equivalent minus 1).

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
python main.py
```

## 🔮 Future Enhancements

- Web API using Flask
- GUI version (Tkinter / PySide)
- Export results to JSON/CSV
- Visualization of progress (charts)

## 📈 Roadmap
[x] Add try...except blocks for input validation (Error handling).

[x] Add unit tests for core logic.

[x] Expand test coverage (UI input validation, edge cases)

[x] Add Ruff formatting & linting

[x] Add mypy static type checking

[ ] Implement data persistence (Save/Load from JSON file).

[ ] Add a Graphical User Interface (GUI) or a web-based dashboard.

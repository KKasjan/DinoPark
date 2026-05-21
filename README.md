# Dino Park Totem Calculator 🦖
![CI](https://github.com/KKasjan/DinoPark/actions/workflows/ci.yml/badge.svg)

[➡️ View on GitHub](https://github.com/KKasjan/DinoPark)

A lightweight Python tool designed to automate the calculation of resources needed to complete "Totems" in the Dino Park game. It helps players track their progress and identifies exactly how many level 1 units are missing for each dinosaur.

## 🎯 Purpose

This project is a showcase of a professional development workflow, specifically tailored for an Automation QA Engineer role:

- **Advanced Logic:** Handling complex "carry-over" rules (losing a level 6 dino upon totem acquisition).
- **Test-Driven Mentality:** Extensive suite of unit and integration tests.
- **Robust Architecture:** Clear separation of concerns (UI, Logic, Data, Config).
- **Quality Gates:** Fully automated CI/CD pipeline using Ruff, MyPy, and Pytest.

## 🚀 Features

- **Totem Progression Logic:** Automatically calculates "Effective Totems" based on owned dinosaurs (1 totem per 63 value units).
- **Golden Chest Roadmap:** Precisely calculates the total value of level 1 units needed to reach the Golden Chest, accounting for the "carry-over" effect (refilling the enclosure after losing level 6 units).
- **Smart SQLite Persistence:** Automatically saves/loads state from a relational SQLite database with an optimized `INSERT OR REPLACE` (UPSERT) mechanism.
- **Auto-Seeding Mechanism:** If the database is completely empty on startup, the application automatically initializes and seeds itself using a predefined dataset of 40+ dinosaurs.
- **Dino Enclosure Monitoring:** Detects "Full Enclosure" status (at least one dinosaur of each level from 1 to 6).
- **Comprehensive Testing:** Unit tests for math logic, UI mock tests, and main flow integration tests.
  
## 📂 Project Structure 

```
DinoPark/
├── src/
│   └── dinopark/
│       ├── __init__.py      # Initialization
│       ├── main.py          # Application entry point (orchestrator)
│       ├── config.py        # Constants, point thresholds and game balance
│       ├── data.py          # Loading, filtering, and validating JSON
│       ├── constants.py     # Application constants and default 40+ dinosaur dataset
|       |── db_setup.py      # SQLite Database initialization schema script
│       ├── logic.py         # Math Engine (Totems, Golden Chest)
│       └── ui.py            # I/O support and console interface
│
├── tests/
│   ├── test_data.py         # Database mock tests using unittest.mock
│   ├── test_integration.py  # Inter-module flow tests
│   ├── test_logic.py        # Unit tests of formulas and calculations
│   ├── test_main.py         # Tests mocking the main loop of the program
│   └── test_ui.py           # User input validation tests
│
├── .env                     # Environment variables
├── .gitattributes           # Git attributes configuration
├── .pre-commit-config.yaml  # Automatic pre-commit checks
├── mypy.ini                 # Static type checking configuration
├── pyprojects.toml          # Tool configuration (e.g., Ruff, Build system)
├── pytest.ini               # Main pytest framework settings
├── README.md                # Project documentation
└── requirements.txt         # Dependency list (pytest, ruff, mypy)
```

## 🔄 Continuous Integration (CI)

The project uses GitHub Actions to automatically run:

- tests (`pytest`)
- static analysis (`mypy`)
- linting (`ruff check`)
- formatting (`ruff format --check`)

Every push and pull request must pass the pipeline.

## 🧪 Testing & Quality Assurance

Quality is baked into the project:
- **Pytest:** Runs all unit and integration tests.
- **Database Mocking:** Uses `unittest.mock.MagicMock` to patch `sqlite3.connect` interfaces, testing full structural data parsing without hitting the physical disk.
- **Static Analysis:** mypy ensures strict type safety.
- **Linting:** ruff enforces industry-standard Python formatting.

The suite covers unit tests for math, mock-based UI tests, and integration tests to verify the end-to-end user flow.

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
- **Database Engine:** SQLite 3
- **Architecture:** Modular, layered design (UI → Logic → Data)
- **Testing Framework:** Pytest
- **Static Analysis:** mypy
- **Linting & Formating:** Ruff
- **CI/CD:** GitHub Actions

## 📋 How It Works

The application follows a simple, user-friendly workflow:

1. **Choose Dinosaur**  
    The user selects a dinosaur from the list.

2. **Check Existing DB Data**
    The application queries the SQLite table. If the dinosaur already has a state saved, it fetches it and triggers a "Verify Status" flow.

3. **Enter Levels (6 → 1)**  
    The user enters the number of units for each level.

4. **Save to SQLite**  
    Data is updated in the dinosaurs table using SQL UPSERT logic.

5. **Calculate Totem Progress**  
   - Convert all levels to Level 1 equivalents using exponential scaling.
   - Sum the total.
   - Compare against the target and calculate the path to the Golden Chest (including carry-over refills).
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
**Set up the Database Schema:**
Before running the application for the first time, execute the initialization script to prepare the database:

```Bash
$env:PYTHONPATH="src"
python -m dinopark.db_setup
```
**Run the script:**

```Bash
$env:PYTHONPATH="src"
python -m dinopark.main
```

## 💾 Relational Database Schema (SQLite)

The backend data architecture uses a relational structure defined in dinopark.db within the dinosaurs table.

**Table Definition**

- **name (TEXT, PRIMARY KEY)** — The unique identifier of the dinosaur (e.g., ammonite).
- **type (TEXT)** — Dinosaur category (e.g., herbivore, carnivore).
- **golden_chest (INTEGER)** — Boolean flag stored as 1 (True) or 0 (False).
- **totems (INTEGER)** — Number of totems unlocked.
- **lvl_1 to lvl_6 (INTEGER)** — Count of units available at each level tier.


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

[x] Complex Golden Chest carry-over logic.

[x] Migrate persistence layer from JSON to relational SQLite database.

[ ] Add a Graphical User Interface (GUI) or a web-based dashboard.
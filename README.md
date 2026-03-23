# Dino Park Totem Calculator 🦖
A lightweight Python tool designed to automate the calculation of resources needed to complete "Totems" in the Dino Park game. It helps players track their progress and identifies exactly how many level 1 units are missing for each dinosaur.

## 🚀 Features
- **Modular Architecture:** Clean separation between logic, data, and user interface.
- **Automated Calculations:** Converts various dinosaur levels (1-6) into base units (Level 1) using pre-defined balance rates.
- **Dynamic Configuration:** Automatic target calculation based on balance settings.
- **Collection Filtering:** Skips dinosaurs that already have a "Golden Chest".
  
## 📂 Project Structure
- `main.py` - The central orchestrator that manages the application flow.
- `config.py` - Global settings and dynamic calculation constants.
- `logic.py` - The calculation engine (pure mathematical functions).
- `ui.py` - Handles all user interactions (input/output).
- `data.py` - The database containing dinosaur attributes and statuses.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Concepts used:** Modular Programming (File Separation), Data Isolation, Logic Decoupling.
- **Architecture:** Separation of concerns (UI, Logic, Data, Config).

## 📋 How It Works
The application follows a modular data processing pipeline:

1. Data Extraction: The main controller fetches dinosaur records from data.py, filtering out those with a "Golden Chest".
2. User Input: For active targets, ui.py prompts the user for the quantity of units at each level (6 to 1).
3. Core Logic: The logic.py module calculates the total value in "Level 1" units using balances from config.py.
4. Result Presentation: The final missing amount is calculated and displayed back to the user via the UI module.

**Conversion Logic:**
- The system uses a base-2 exponential scaling (where Level 6 = 32 units). The TARGET is dynamically set to a full totem value (Level 7 equivalent minus 1).

## 💻 Installation & Usage
**Clone the repository:**

```Bash
git clone https://github.com/KKasjan/DinoPark.git
```
**Run the script:**

```Bash
python main.py
```

## 📈 Roadmap
[ ] Add try...except blocks for input validation (Error handling).

[ ] Implement data persistence (Save/Load from JSON file).

[ ] Add a Graphical User Interface (GUI) or a web-based dashboard.

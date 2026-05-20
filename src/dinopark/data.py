import sqlite3
from typing import Any

from dinopark.db_setup import DB_PATH

# ---------------------------------------
# LOADING & SAVING (SQLite)
# ---------------------------------------


def load_all_dinos() -> dict[str, Any]:
    """
    Fetches all dinosaurs from the SQLite database and converts them
    into the application's dictionary format.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Retrieving all records from the dinosaurs table
    cursor.execute("""
        SELECT name, type, golden_chest, totems,
               lvl_1, lvl_2, lvl_3, lvl_4, lvl_5, lvl_6
        FROM dinosaurs
    """)
    rows = cursor.fetchall()

    connection.close()

    dinos_dict: dict[str, Any] = {}

    for row in rows:
        (
            name, dino_type, golden_chest, totems,
            l1, l2, l3, l4, l5, l6
        ) = row

        # Reconstructs the dictionary structure
        # (changing 1/0 from the database to True/False in Python)
        dinos_dict[name] = {
            "type": dino_type,
            "golden_chest": bool(golden_chest),
            "totems": totems,
            "levels": {
                "1": l1,
                "2": l2,
                "3": l3,
                "4": l4,
                "5": l5,
                "6": l6
            }
        }

    return dinos_dict


def save_all_dinos(dinos_data: dict[str, Any]) -> None:
    """
    Saves or updates the dinosaurs dictionary structure in the SQLite database
    using a safe INSERT OR REPLACE (UPSERT) mechanism.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    for name, data in dinos_data.items():
        cursor.execute("""
            INSERT OR REPLACE INTO dinosaurs (
                name, type, golden_chest, totems,
                lvl_1, lvl_2, lvl_3, lvl_4, lvl_5, lvl_6
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            data["type"],
            # Converting True/False to 1/0 for SQLite
            1 if data["golden_chest"] else 0,
            data["totems"],
            data["levels"]["1"],
            data["levels"]["2"],
            data["levels"]["3"],
            data["levels"]["4"],
            data["levels"]["5"],
            data["levels"]["6"]
        ))

    connection.commit()
    connection.close()


# ---------------------------------------
# VALIDATION (Business Rules)
# ---------------------------------------


def validate_park_data(data: Any) -> bool:
    """
    Validates the entire dino JSON structure and business rules.
    Ensures:
    - correct types
    - correct keys
    - levels 1–6 exist and are ints >= 0
    - totems in range 0–3
    - golden_chest is bool
    - sum(levels) <= 6
    """
    if not isinstance(data, dict):
        return False

    for _name, dino in data.items():
        if not isinstance(dino, dict):
            return False

        # Required keys
        required_keys = {"type", "golden_chest", "totems", "levels"}
        if not required_keys.issubset(dino.keys()):
            return False

        # Validate type
        if not isinstance(dino["type"], str):
            return False

        # Validate totems
        totems = dino["totems"]
        if not isinstance(totems, int) or not (0 <= totems <= 3):
            return False

        # Validate golden chest
        if not isinstance(dino["golden_chest"], bool):
            return False

        # Validate levels
        levels = dino["levels"]
        if not isinstance(levels, dict):
            return False

        # Must contain exactly levels 1-6
        expected_levels = {str(i) for i in range(1, 7)}
        if set(levels.keys()) != expected_levels:
            return False

        # Validate each level count
        total = 0
        for _lvl, count in levels.items():
            if not isinstance(count, int) or count < 0:
                return False
            total += count

        # Business rule: max 6 dinos in enclosure
        if total > 6:
            return False

    return True

import os

# Base repo name
BASE_DIR = "TECH-SPHERE"

# Folder and file structure
structure = {
    "explainers-non-code": {
        "A-basics": ["variables.md", "data-types.md", "operators.md"],
        "B-control-flow": [],
        "C-functions-modularity": [],
        "D-data-structures": [],
        "E-algorithms": [],
        "F-advanced-basics": [],
    },
    "tier-1-baby-steps": {
        "greeting-app": ["greeting.py"],
        "bmi-calculator": ["bmi.py"],
        "odd-even-checker": ["odd_even.py"]
    },
    "tier-2-logic-builders": {
        "rock-paper-scissors": ["rps.py"],
        "prime-checker": ["prime.py"],
        "fibonacci": ["fibonacci.py"]
    },
    "tier-3-mini-apps": {
        "todo-cli": [],
        "weather-cli": [],
        "naija-slang-translator": []
    },
    "tier-4-capstones": {
        "calculator": [],
        "quiz-app": [],
        "basic-banking-system": []
    },
    "tier-5-intermediate": {},
    "tier-6-advanced": {},
    "algorithm-challenges": {
        "sudoku-solver": [],
        "binary-search": []
    },
    "templates": {
        "": ["code-template.md", "explainer-template.md"]
    }
}

# Files at the root
root_files = ["README.md", "CONTRIBUTING.md"]

# Create the base directory
os.makedirs(BASE_DIR, exist_ok=True)

# Create root files
for file in root_files:
    with open(os.path.join(BASE_DIR, file), "w") as f:
        f.write(f"# {file.replace('.md', '').capitalize()}\n")

# Create folder structure
for main_folder, subfolders in structure.items():
    for subfolder, files in subfolders.items():
        # Handle folders without sub-subfolders (like templates)
        folder_path = os.path.join(BASE_DIR, main_folder, subfolder) if subfolder else os.path.join(BASE_DIR, main_folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, "w") as f:
                f.write(f"# {file.replace('.md', '').replace('.py', '').capitalize()}\n")

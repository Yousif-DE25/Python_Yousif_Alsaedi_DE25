from pathlib import Path

file_path = Path(__file__).parent / "09_file_handling"

with open(file_path / "quotes_cleand.txt") as file:
    print(file.read())
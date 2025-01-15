import json


def read_json(file_path: str) -> dict:
    """Читает JSON-файл и возвращает данные в виде словаря."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, ValueError):
        return {"best_score": 0}

def write_json(file_path: str, data: dict) -> None:
    """Записывает данные в файл в формате JSON."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4) # type: ignore

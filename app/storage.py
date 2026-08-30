import json


def guardar_tareas(tareas):
    with open("data/tasks.json", "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=4)
import json


def guardar_tareas(tareas):
    with open("data/tasks.json", "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, ensure_ascii=False, indent=4)
        
def cargar_tareas():
    try:
        with open("data/tasks.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
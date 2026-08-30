def agregar_tarea(tareas, titulo):
    if titulo.strip() == "":
        return False

    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo.strip(),
        "completada": False
    }

    tareas.append(tarea)

    return True
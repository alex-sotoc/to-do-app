from datetime import datetime


def agregar_tarea(tareas, titulo):
    if titulo.strip() == "":
        return False

    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo.strip(),
        "completada": False,
        "fecha_creacion": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    tareas.append(tarea)

    return True


def completar_tarea(tareas, id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            return True

    return False


def eliminar_tarea(tareas, id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tareas.remove(tarea)
            return True

    return False


def editar_tarea(tareas, id_tarea, nuevo_titulo):
    if nuevo_titulo.strip() == "":
        return False

    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["titulo"] = nuevo_titulo.strip()
            return True

    return False


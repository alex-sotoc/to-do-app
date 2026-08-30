import customtkinter as ctk

from tasks import (
    agregar_tarea,
    completar_tarea,
    eliminar_tarea,
    editar_tarea,
    obtener_pendientes,
    obtener_completadas
)

from storage import guardar_tareas, cargar_tareas


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


ventana = ctk.CTk()
ventana.title("Mis tareas")
ventana.geometry("700x600")
ventana.configure(fg_color="white")


tareas = cargar_tareas()
filtro_actual = "todas"


titulo = ctk.CTkLabel(
    ventana,
    text="Mis tareas",
    font=("Arial", 30, "bold"),
    text_color="black"
)
titulo.pack(pady=(30, 5))


subtitulo = ctk.CTkLabel(
    ventana,
    text="Organiza tus tareas pendientes",
    font=("Arial", 15),
    text_color="gray"
)
subtitulo.pack(pady=(0, 25))


entrada = ctk.CTkEntry(
    ventana,
    width=430,
    height=40,
    placeholder_text="Escribe una tarea..."
)
entrada.pack(side="top", pady=5)


marco_tareas = ctk.CTkScrollableFrame(
    ventana,
    width=580,
    height=280,
    fg_color="white"
)
marco_tareas.pack(pady=15)


def mostrar_tareas():
    for elemento in marco_tareas.winfo_children():
        elemento.destroy()

    if filtro_actual == "pendientes":
        lista = obtener_pendientes(tareas)
    elif filtro_actual == "completadas":
        lista = obtener_completadas(tareas)
    else:
        lista = tareas

    for tarea in lista:
        marco = ctk.CTkFrame(
            marco_tareas,
            fg_color="white"
        )
        marco.pack(fill="x", padx=10, pady=5)

        texto = tarea["titulo"]

        if tarea["completada"]:
            texto = "✓ " + texto

        etiqueta = ctk.CTkLabel(
            marco,
            text=texto,
            text_color="black",
            font=("Arial", 16)
        )
        etiqueta.pack(side="left", padx=10)

        fecha = ctk.CTkLabel(
            marco,
            text=tarea["fecha_creacion"],
            text_color="gray",
            font=("Arial", 11)
        )
        fecha.pack(side="left", padx=5)

        boton_completar = ctk.CTkButton(
            marco,
            text="✓",
            width=40,
            command=lambda id_tarea=tarea["id"]: completar(id_tarea)
        )
        boton_completar.pack(side="right", padx=3)

        boton_editar = ctk.CTkButton(
            marco,
            text="Editar",
            width=60,
            command=lambda id_tarea=tarea["id"]: editar(id_tarea)
        )
        boton_editar.pack(side="right", padx=3)

        boton_eliminar = ctk.CTkButton(
            marco,
            text="Eliminar",
            width=70,
            command=lambda id_tarea=tarea["id"]: eliminar(id_tarea)
        )
        boton_eliminar.pack(side="right", padx=3)


def agregar():
    texto = entrada.get()

    if agregar_tarea(tareas, texto):
        guardar_tareas(tareas)
        entrada.delete(0, "end")
        mostrar_tareas()


def completar(id_tarea):
    completar_tarea(tareas, id_tarea)
    guardar_tareas(tareas)
    mostrar_tareas()


def eliminar(id_tarea):
    eliminar_tarea(tareas, id_tarea)
    guardar_tareas(tareas)
    mostrar_tareas()


def editar(id_tarea):
    ventana_editar = ctk.CTkToplevel(ventana)
    ventana_editar.title("Editar tarea")
    ventana_editar.geometry("400x180")
    ventana_editar.configure(fg_color="white")

    entrada_editar = ctk.CTkEntry(
        ventana_editar,
        width=300,
        placeholder_text="Nuevo nombre"
    )
    entrada_editar.pack(pady=20)

    def guardar_edicion():
        if editar_tarea(tareas, id_tarea, entrada_editar.get()):
            guardar_tareas(tareas)
            ventana_editar.destroy()
            mostrar_tareas()

    boton_guardar = ctk.CTkButton(
        ventana_editar,
        text="Guardar",
        command=guardar_edicion
    )
    boton_guardar.pack()


def mostrar_todas():
    global filtro_actual
    filtro_actual = "todas"
    mostrar_tareas()


def mostrar_pendientes():
    global filtro_actual
    filtro_actual = "pendientes"
    mostrar_tareas()


def mostrar_completadas():
    global filtro_actual
    filtro_actual = "completadas"
    mostrar_tareas()


boton_agregar = ctk.CTkButton(
    ventana,
    text="Agregar",
    width=120,
    height=40,
    command=agregar
)
boton_agregar.pack(pady=10)


marco_filtros = ctk.CTkFrame(
    ventana,
    fg_color="white"
)
marco_filtros.pack(pady=10)


boton_todas = ctk.CTkButton(
    marco_filtros,
    text="Todas",
    width=110,
    command=mostrar_todas
)
boton_todas.grid(row=0, column=0, padx=5)


boton_pendientes = ctk.CTkButton(
    marco_filtros,
    text="Pendientes",
    width=110,
    command=mostrar_pendientes
)
boton_pendientes.grid(row=0, column=1, padx=5)


boton_completadas = ctk.CTkButton(
    marco_filtros,
    text="Completadas",
    width=110,
    command=mostrar_completadas
)
boton_completadas.grid(row=0, column=2, padx=5)


mostrar_tareas()

ventana.mainloop()
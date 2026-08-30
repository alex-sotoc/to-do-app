import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


ventana = ctk.CTk()
ventana.title("Mis tareas")
ventana.geometry("700x600")
ventana.configure(fg_color="white")


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


boton_agregar = ctk.CTkButton(
    ventana,
    text="Agregar",
    width=120,
    height=40
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
    width=110
)
boton_todas.grid(row=0, column=0, padx=5)


boton_pendientes = ctk.CTkButton(
    marco_filtros,
    text="Pendientes",
    width=110
)
boton_pendientes.grid(row=0, column=1, padx=5)


boton_completadas = ctk.CTkButton(
    marco_filtros,
    text="Completadas",
    width=110
)
boton_completadas.grid(row=0, column=2, padx=5)


marco_tareas = ctk.CTkScrollableFrame(
    ventana,
    width=580,
    height=280,
    fg_color="white"
)
marco_tareas.pack(pady=15)


tarea1 = ctk.CTkCheckBox(
    marco_tareas,
    text="Hacer tarea de Ingeniería de Software",
    text_color="black",
    font=("Arial", 16)
)
tarea1.pack(anchor="w", padx=20, pady=12)


tarea2 = ctk.CTkCheckBox(
    marco_tareas,
    text="Estudiar para el examen",
    text_color="black",
    font=("Arial", 16)
)
tarea2.pack(anchor="w", padx=20, pady=12)


tarea3 = ctk.CTkCheckBox(
    marco_tareas,
    text="Terminar proyecto",
    text_color="black",
    font=("Arial", 16)
)
tarea3.pack(anchor="w", padx=20, pady=12)


ventana.mainloop()
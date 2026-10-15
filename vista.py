"""
vista.py:
    Módulo que contiene la vista del programa.
"""

import tkinter as tk
from tkinter import ttk
from modelo import Abm


class Mi_vista:
    """Interfaz gráfica de la veterinaria."""

    FONDO = "#F3F7F4"
    BLANCO = "#FFFFFF"
    VERDE_OSCURO = "#245C43"
    VERDE = "#39845B"
    VERDE_CLARO = "#E0F0E5"
    ROJO = "#C94C4C"
    TEXTO = "#26352C"
    TEXTO_SECUNDARIO = "#64736A"
    BORDE = "#DCE6DE"

    def __init__(self, window):
        self.master = window
        self.master.title("Veterinaria Perros y Gatos")
        self.master.geometry("1150x760")
        self.master.minsize(900, 650)
        self.master.configure(bg=self.FONDO)

        self.objeto_abm = Abm()
        self.limpiando_formulario = False

        # ------------------------------------------
        # ESTILOS
        # ------------------------------------------

        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Treeview",
            background=self.BLANCO,
            foreground=self.TEXTO,
            fieldbackground=self.BLANCO,
            rowheight=30,
            font=("Verdana", 10),
            borderwidth=0,
        )

        estilo.configure(
            "Treeview.Heading",
            background=self.VERDE_OSCURO,
            foreground=self.BLANCO,
            font=("Verdana", 10, "bold"),
            padding=9,
            relief="flat",
        )

        estilo.map(
            "Treeview",
            background=[("selected", self.VERDE_CLARO)],
            foreground=[("selected", self.TEXTO)],
        )

        # ------------------------------------------
        # CONTENEDOR PRINCIPAL
        # ------------------------------------------

        self.contenido = tk.Frame(
            self.master,
            bg=self.FONDO,
            padx=20,
            pady=15,
        )
        self.contenido.pack(fill="both", expand=True)

        # ------------------------------------------
        # ENCABEZADO
        # ------------------------------------------

        self.encabezado = tk.Frame(
            self.contenido,
            bg=self.VERDE_OSCURO,
            padx=20,
            pady=14,
        )
        self.encabezado.pack(fill="x", pady=(0, 15))

        tk.Label(
            self.encabezado,
            text="Veterinaria Perros y Gatos",
            bg=self.VERDE_OSCURO,
            fg=self.BLANCO,
            font=("Verdana", 19, "bold"),
        ).pack(anchor="w")

        tk.Label(
            self.encabezado,
            text="Gestión de pacientes y registros",
            bg=self.VERDE_OSCURO,
            fg="#D8E9DE",
            font=("Verdana", 10),
        ).pack(anchor="w", pady=(4, 0))

        # ------------------------------------------
        # FORMULARIO SUPERIOR
        # ------------------------------------------

        self.panel_formulario = tk.Frame(
            self.contenido,
            bg=self.BLANCO,
            highlightbackground=self.BORDE,
            highlightthickness=1,
            padx=15,
            pady=12,
        )
        self.panel_formulario.pack(fill="x", pady=(0, 15))

        tk.Label(
            self.panel_formulario,
            text="Datos del animal",
            bg=self.BLANCO,
            fg=self.VERDE_OSCURO,
            font=("Verdana", 13, "bold"),
        ).pack(anchor="w", pady=(0, 10))

        # Variables
        self.var_nombre = tk.StringVar()
        self.var_tipo = tk.StringVar()
        self.var_raza = tk.StringVar()
        self.var_peso = tk.StringVar()

        # Distribución horizontal de los campos
        self.marco_campos = tk.Frame(
            self.panel_formulario,
            bg=self.BLANCO,
        )
        self.marco_campos.pack(fill="x")

        for columna in range(4):
            self.marco_campos.columnconfigure(columna, weight=1)

        campos = [
            ("Nombre", self.var_nombre),
            ("Tipo", self.var_tipo),
            ("Raza", self.var_raza),
            ("Peso", self.var_peso),
        ]

        self.entradas = {}

        for columna, (etiqueta, variable) in enumerate(campos):
            marco_campo = tk.Frame(
                self.marco_campos,
                bg=self.BLANCO,
            )
            marco_campo.grid(
                row=0,
                column=columna,
                sticky="ew",
                padx=(0 if columna == 0 else 8, 0),
            )

            tk.Label(
                marco_campo,
                text=etiqueta,
                bg=self.BLANCO,
                fg=self.TEXTO,
                font=("Verdana", 10, "bold"),
            ).pack(anchor="w", pady=(0, 5))

            entrada = tk.Entry(
                marco_campo,
                textvariable=variable,
                font=("Verdana", 11),
                relief="solid",
                bd=1,
                bg="#FCFDFC",
                fg=self.TEXTO,
                insertbackground=self.TEXTO,
            )
            entrada.pack(fill="x", ipady=5)

            self.entradas[etiqueta] = entrada

        self.entry_nombre = self.entradas["Nombre"]
        self.entry_tipo = self.entradas["Tipo"]
        self.entry_raza = self.entradas["Raza"]
        self.entry_peso = self.entradas["Peso"]

        # ------------------------------------------
        # MENSAJES DE VALIDACIÓN
        # Se conservan los textos originales.
        # Siempre están visibles.
        # ------------------------------------------

        self.marco_mensajes = tk.Frame(
            self.panel_formulario,
            bg=self.BLANCO,
        )
        self.marco_mensajes.pack(fill="x", pady=(8, 0))

        self.e_nombre = tk.Label(
            self.marco_mensajes,
            text="El nombre es obligatorio y debe comenzar en mayúscula.",
            bg=self.BLANCO,
            fg=self.ROJO,
            font=("Verdana", 8),
            wraplength=350,
            justify="left",
        )
        self.e_nombre.pack(side="left", anchor="w", padx=(0, 20))

        self.e_peso = tk.Label(
            self.marco_mensajes,
            text="El peso debe ser un número.",
            bg=self.BLANCO,
            fg=self.ROJO,
            font=("Verdana", 8),
            wraplength=250,
            justify="left",
        )
        self.e_peso.pack(side="left", anchor="w")

        # ------------------------------------------
        # BOTONES
        # ------------------------------------------

        self.marco_botones = tk.Frame(
            self.panel_formulario,
            bg=self.BLANCO,
        )
        self.marco_botones.pack(fill="x", pady=(12, 0))

        self.boton_alta = tk.Button(
            self.marco_botones,
            text="Agregar",
            bg=self.VERDE,
            fg=self.BLANCO,
            activebackground=self.VERDE_OSCURO,
            activeforeground=self.BLANCO,
            font=("Verdana", 10, "bold"),
            relief="flat",
            cursor="hand2",
            command=lambda: self.objeto_abm.alta(
                self.var_nombre.get(),
                self.var_tipo.get(),
                self.var_raza.get(),
                self.var_peso.get(),
                self.tree,
                self.entry_nombre,
                self.entry_raza,
                self.entry_peso,
                self.entry_tipo,
            ),
        )
        self.boton_alta.pack(side="left", padx=(0, 8), ipady=5, ipadx=12)

        self.boton_actualizar = tk.Button(
            self.marco_botones,
            text="Actualizar",
            bg="#E4C96B",
            fg="#3C341B",
            activebackground="#D6B74E",
            font=("Verdana", 10, "bold"),
            relief="flat",
            cursor="hand2",
            command=lambda: self.objeto_abm.actualizar(
                self.var_nombre.get(),
                self.var_tipo.get(),
                self.var_raza.get(),
                self.var_peso.get(),
                self.tree,
                self.entry_nombre,
                self.entry_raza,
                self.entry_peso,
                self.entry_tipo,
                self.boton_alta,
            ),
        )
        self.boton_actualizar.pack(
            side="left",
            padx=(0, 8),
            ipady=5,
            ipadx=12,
        )

        self.boton_limpiar = tk.Button(
            self.marco_botones,
            text="Limpiar formulario",
            bg="#E5EBE6",
            fg=self.TEXTO,
            activebackground="#D5E0D7",
            font=("Verdana", 10),
            relief="flat",
            cursor="hand2",
            command=self.limpiar_formulario,
        )
        self.boton_limpiar.pack(
            side="left",
            padx=(0, 8),
            ipady=5,
            ipadx=12,
        )

        self.boton_borrar = tk.Button(
            self.marco_botones,
            text="Eliminar seleccionado",
            bg="#F8E6E4",
            fg="#A63434",
            activebackground="#F0D0CD",
            font=("Verdana", 10),
            relief="flat",
            cursor="hand2",
            command=lambda: self.objeto_abm.borrar(self.tree),
        )
        self.boton_borrar.pack(side="left", ipady=5, ipadx=12)

        tk.Label(
            self.marco_botones,
            text="Seleccioná una fila para cargar sus datos.",
            bg=self.BLANCO,
            fg=self.TEXTO_SECUNDARIO,
            font=("Verdana", 9),
        ).pack(side="right", padx=(10, 0))

        # ------------------------------------------
        # TABLA INFERIOR
        # ------------------------------------------

        self.panel_tabla = tk.Frame(
            self.contenido,
            bg=self.BLANCO,
            highlightbackground=self.BORDE,
            highlightthickness=1,
            padx=15,
            pady=12,
        )
        self.panel_tabla.pack(fill="both", expand=True)

        # Encabezado y controles de la tabla
        self.marco_encabezado_tabla = tk.Frame(
            self.panel_tabla,
            bg=self.BLANCO,
        )
        self.marco_encabezado_tabla.pack(fill="x", pady=(0, 10))

        tk.Label(
            self.marco_encabezado_tabla,
            text="Registros",
            bg=self.BLANCO,
            fg=self.VERDE_OSCURO,
            font=("Verdana", 14, "bold"),
        ).pack(side="left")

        self.marco_orden = tk.Frame(
            self.marco_encabezado_tabla,
            bg=self.BLANCO,
        )
        self.marco_orden.pack(side="right")

        self.boton_ver_nombre = tk.Button(
            self.marco_orden,
            text="Ordenar por nombre",
            bg=self.BLANCO,
            fg=self.VERDE_OSCURO,
            font=("Verdana", 9),
            relief="solid",
            bd=1,
            cursor="hand2",
            command=lambda: self.objeto_abm.ver_orden_nombre(self.tree),
        )
        self.boton_ver_nombre.pack(side="left", padx=(0, 8))

        self.boton_ver_todo = tk.Button(
            self.marco_orden,
            text="Ordenar por tipo",
            bg=self.BLANCO,
            fg=self.VERDE_OSCURO,
            font=("Verdana", 9),
            relief="solid",
            bd=1,
            cursor="hand2",
            command=lambda: self.objeto_abm.ver_todo(self.tree),
        )
        self.boton_ver_todo.pack(side="left")

        # Tabla con desplazamiento vertical y horizontal
        self.contenedor_tree = tk.Frame(
            self.panel_tabla,
            bg=self.BLANCO,
        )
        self.contenedor_tree.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(
            self.contenedor_tree,
            columns=("col1", "col2", "col3", "col4"),
            show="tree headings",
            selectmode="browse",
        )

        self.tree.heading("#0", text="ID", anchor="w")
        self.tree.heading("col1", text="Nombre", anchor="w")
        self.tree.heading("col2", text="Tipo", anchor="w")
        self.tree.heading("col3", text="Raza", anchor="w")
        self.tree.heading("col4", text="Peso", anchor="w")

        self.tree.column("#0", width=55, minwidth=45, anchor="center", stretch=False)
        self.tree.column("col1", width=200, minwidth=120, anchor="w")
        self.tree.column("col2", width=120, minwidth=90, anchor="w")
        self.tree.column("col3", width=200, minwidth=120, anchor="w")
        self.tree.column("col4", width=100, minwidth=75, anchor="center")

        self.scroll_y = ttk.Scrollbar(
            self.contenedor_tree,
            orient="vertical",
            command=self.tree.yview,
        )
        self.scroll_x = ttk.Scrollbar(
            self.contenedor_tree,
            orient="horizontal",
            command=self.tree.xview,
        )

        self.tree.configure(
            yscrollcommand=self.scroll_y.set,
            xscrollcommand=self.scroll_x.set,
        )

        self.contenedor_tree.rowconfigure(0, weight=1)
        self.contenedor_tree.columnconfigure(0, weight=1)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.scroll_x.grid(row=1, column=0, sticky="ew")

        # Cargar los registros
        self.objeto_abm.ver_orden_nombre(self.tree)

        # Selección automática
        self.tree.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_fila,
        )

    def seleccionar_fila(self, event=None):
        """Carga los datos de la fila seleccionada."""

        if self.limpiando_formulario:
            return

        if not self.tree.selection():
            return

        self.objeto_abm.ver_elemento(
            self.tree,
            self.var_nombre,
            self.var_peso,
            self.var_raza,
            self.var_tipo,
            self.boton_alta,
        )

    def limpiar_formulario(self):
        """Prepara el formulario para agregar un registro nuevo."""

        self.limpiando_formulario = True

        try:
            self.var_nombre.set("")
            self.var_tipo.set("")
            self.var_raza.set("")
            self.var_peso.set("")

            self.tree.selection_remove(self.tree.selection())

            self.boton_alta.config(state="normal")
            self.entry_nombre.focus_set()

        finally:
            self.limpiando_formulario = False

# MVC + Pyside6

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-Qt6-green.svg)
![MVC](https://img.shields.io/badge/Pattern-MVC-orange.svg)
![GitHub Repo size](https://img.shields.io/github/repo-size/Willmouzalli/PySide6MVC.svg)
![GitHub license](https://img.shields.io/github/license/Willmouzalli/PySide6MVC.svg)

---

## ✨ Descripción del Proyecto

A simple project using the **MVC (Model-View-Controller) design pattern** and **PySide6** for building a desktop application. This project serves as a clear example of separating concerns in a GUI application, making it maintainable and scalable.

It demonstrates best practices for structuring a PySide6 application, including:
* **Clear separation of logic** (Model), **user interface** (View), and **application flow control** (Controller).
* **Database integration** (SQLite) using SQLAlchemy ORM for data persistence.
* **Modular and reusable components**.

---

## 🚀 Características

* **Implementación del Patrón MVC:** Demostración práctica de cómo aplicar el MVC en una aplicación de escritorio.
* **Interfaz de Usuario con PySide6:** Construcción de una UI interactiva y moderna utilizando el framework Qt a través de PySide6.
* **Persistencia de Datos con SQLite y SQLAlchemy:** Gestión de datos a través de una base de datos local SQLite, con SQLAlchemy como ORM para la interacción con el modelo de datos.
* **Estructura de Directorios Limpia:** Organización lógica del código para facilitar la navegación y el mantenimiento.
* **Manejo Básico de Ventanas:** Ejemplo de cómo mostrar una ventana principal.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* **PySide6** (Qt for Python)
* **SQLAlchemy** (SQL Toolkit and Object Relational Mapper)
* **SQLite** (Base de datos ligera)

---

## 📂 Estructura del Proyecto
````
MVC/                           
├── .git/                      # Repositorio Git
├── .gitignore                 # Archivos y directorios a ignorar por Git
├── config.py                  # Configuración de la aplicación (rutas DB, etc.)
├── main.py                    # Punto de entrada de la aplicación
├── requirements.txt           # Dependencias del proyecto
├── controller/                # Lógica de control entre el modelo y la vista
│   ├── init.py
│   └── main_controller.py     # Controlador principal
├── model/                     # Lógica de negocio y modelos de datos
│   ├── init.py
│   ├── database_manager.py    # Conexión y gestión de la DB
│   └── data_models.py         # Definición de modelos de datos (SQLAlchemy)
├── view/                      # Interfaz de usuario y widgets
│   ├── init.py
│   └── main_window.py         # Ventana principal de la aplicación
└── tests/                     # Pruebas unitarias (opcional)
└── test_example.py
````
---

## ⚙️ Configuración y Ejecución Local

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

### Prerrequisitos

Asegúrate de tener **Python 3.x** instalado.

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/Willmouzalli/mvc_pyside.git](https://github.com/Willmouzalli/mvc_pyside)
    cd mvc_pyside
    ```

2.  **Crea y activa un entorno virtual** (recomendado):
    * En Windows:
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    * En macOS/Linux:
        ```bash
        python3 -m venv .venv
        source ./.venv/bin/activate
        ```

3.  **Instala las dependencias necesarias:**
    ```bash
    pip install -r requirements.txt
    ```
    
### Ejecución

1.  **Asegúrate de que tu entorno virtual esté activado.**
2.  **Ejecuta la aplicación principal:**
    ```bash
    python main.py
    ```

La aplicación debería iniciarse y mostrar la ventana principal. La base de datos `app_database.db` se creará automáticamente en `C:\Users\TU_USUARIO\Documents\MiAplicacion\data\` (o la ruta que hayas configurado en `config.py`).

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si encuentras un bug o tienes una idea para mejorar el proyecto, por favor, abre un "issue" o envía un "pull request".

1.  Haz un fork del repositorio.
2.  Crea tu branch de características (`git checkout -b feature/AmazingFeature`).
3.  Haz tus commits (`git commit -m 'Add some AmazingFeature'`).
4.  Sube tu branch (`git push origin feature/AmazingFeature`).
5.  Abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 📞 Contacto

**Willmouzalli - [wmouzalli@gmail.com](mailto:wmouzalli@gmail.com)**
Enlace a tu Perfil de GitHub - [https://github.com/Willmouzalli](https://github.com/Willmouzalli)

---

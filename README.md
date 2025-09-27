# Mini-blog

Blog personal de Williams construido con Django. Una aplicación web simple para compartir artículos sobre desarrollo web, ciberseguridad y más.

## Características

- ✅ Crear, editar y eliminar posts
- ✅ Contenido en formato Markdown (usando django-markdownx)
- ✅ Interfaz moderna con Tailwind CSS
- ✅ Base de datos SQLite
- ✅ CRUD completo de posts

## Tecnologías

- **Backend**: Django 5.2
- **Base de datos**: SQLite
- **Frontend**: HTML, Tailwind CSS
- **Markdown**: django-markdownx

## Instalación

1. **Clona el repositorio**
   ```bash
   git clone <url-del-repo>
   cd mini-blog
   ```

2. **Crea un entorno virtual**
   ```bash
   python -m venv .venv
   ```

3. **Activa el entorno virtual**
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`

4. **Instala las dependencias**
   ```bash
   pip install django django-markdownx
   ```

5. **Ejecuta las migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Ejecuta el servidor**
   ```bash
   python manage.py runserver
   ```

7. **Accede al blog**
   - Abre http://127.0.0.1:8000 en tu navegador

## Uso

- **Página principal**: Muestra los posts más recientes
- **Lista de posts**: /posts/
- **Ver post**: /post/<id>/
- **Crear post**: /create/
- **Editar post**: /edit/<id>/
- **Eliminar post**: /delete/<id>/

## Estructura del proyecto

```
mini-blog/
├── blog/                 # App principal
│   ├── models.py        # Modelo Post
│   ├── views.py         # Vistas CRUD
│   ├── forms.py         # Formulario para posts
│   ├── urls.py          # URLs de la app
│   ├── static/css/      # Estilos CSS
│   └── templates/blog/  # Templates HTML
├── miniblog/            # Proyecto Django
│   ├── settings.py      # Configuración
│   ├── urls.py          # URLs principales
│   └── wsgi.py
├── db.sqlite3           # Base de datos
├── manage.py            # Script de gestión
└── README.md
```

## Contribuir

Este es un proyecto personal, pero si tienes sugerencias, ¡bienvenidas!

## Autor

Williams - Desarrollador web apasionado

---

*Última actualización: Septiembre 2025*"# MINI-BLOG" 

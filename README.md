# 💰 SaaS de Finanzas Personales – Backend

Este es el backend de un sistema SaaS (Software como Servicio) enfocado en la gestión de finanzas personales y de pequeñas empresas. Desarrollado con **FastAPI**, proporciona una API RESTful moderna, segura y eficiente.

---

## 🚀 Funcionalidades Principales

- 🔐 **Autenticación y autorización segura** (JWT, hashing de contraseñas)
- 👤 **Gestión de usuarios**: registro, inicio de sesión, recuperación de contraseña
- 💵 **Gestión de transacciones**: ingresos, egresos, categorías, etiquetas
- 📊 **Reportes financieros**: balances mensuales, análisis por categoría
- 👥 **Multiusuario** con separación y seguridad de datos
- 🌐 **Integración vía API RESTful** con el frontend (Next.js)

---

## 🛠️ Tecnologías Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** – Framework moderno para APIs con Python
- **[PostgreSQL](https://www.postgresql.org/)** – Base de datos relacional
- **[SQLAlchemy](https://www.sqlalchemy.org/)** – ORM para Python
- **[Pydantic](https://docs.pydantic.dev/)** – Validación de datos basada en Python
- **[Alembic](https://alembic.sqlalchemy.org/)** – Migraciones de base de datos
- **Docker** (opcional) – Contenedores reproducibles para desarrollo y producción

---

## 📁 Estructura del Proyecto

\`\`\`
backend/
├── app/
│   ├── main.py              # Punto de entrada de FastAPI
│   ├── api/                 # Rutas y endpoints
│   ├── models/              # Modelos Pydantic y de base de datos
│   ├── crud/                # Lógica de negocio y operaciones CRUD
│   ├── db/                  # Configuración y conexión a la base de datos
│   ├── core/                # Configs generales, seguridad, utilidades
│   └── utils/               # Funciones auxiliares
├── alembic/                 # Migraciones de base de datos
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
\`\`\`

---

## ⚙️ Configuración Inicial

1. Clona el repositorio:
   \`\`\`bash
   git clone https://github.com/tu_usuario/tu_repo_backend.git
   cd tu_repo_backend
   \`\`\`

2. Instala dependencias:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Configura las variables de entorno (\`.env\`):
   \`\`\`
   DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/tu_db
   SECRET_KEY=una_clave_secreta_segura
   \`\`\`

4. Inicia el servidor:
   \`\`\`bash
   uvicorn app.main:app --reload
   \`\`\`

---

## 📬 API Endpoints

Puedes consultar la documentación automática de la API una vez iniciado el servidor en:

- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

---

## 🧪 Testing (opcional)

Pruebas se pueden ejecutar con:

\`\`\`bash
pytest
\`\`\`

---

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la MIT License.

---

## ✍️ Autor

Desarrollado por [Tu Nombre].
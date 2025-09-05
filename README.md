# RegistroDeHorasApp

Aplicación completa para registro de horas trabajadas con backend Django y frontend Android nativo.

## Estructura del Proyecto

```
├── backend_python/
│   └── RegistroDeHorasApp-backend/     # Backend Django REST API
│       ├── registro_horas/             # Configuración Django
│       ├── contador/                   # App principal
│       ├── requirements.txt           # Dependencias Python
│       ├── Procfile                   # Configuración Render
│       └── build.sh                   # Script de build
└── frontend_kotlin/                   # App Android en Kotlin
    ├── app/                          # Código fuente Android
    ├── build.gradle.kts             # Configuración Gradle
    └── README.md                     # Documentación Android
```

## Tecnologías

**Backend:**
- Django 4.2.0
- Django REST Framework
- PostgreSQL (producción)
- SQLite (desarrollo)

**Frontend:**
- Android nativo con Kotlin
- Retrofit para API calls
- Material Design

## Configuración para Desarrollo

### Backend
1. Navegar al directorio del backend:
   ```bash
   cd backend_python/RegistroDeHorasApp-backend
   ```

2. Crear entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate     # Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar migraciones:
   ```bash
   python manage.py migrate
   ```

5. Crear superusuario:
   ```bash
   python manage.py createsuperuser
   ```

6. Correr servidor:
   ```bash
   python manage.py runserver
   ```

### Frontend
1. Abrir el proyecto en Android Studio
2. Sincronizar dependencias de Gradle
3. Configurar la URL del backend en `RetrofitClient.kt`
4. Ejecutar en emulador o dispositivo

## Deploy en Render

### Backend (Web Service)
1. Conectar este repositorio a Render
2. Configurar como Web Service
3. Configurar variables de entorno:
   - `SECRET_KEY`: Clave secreta de Django
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `registrodehorasapp.onrender.com`
   - `DATABASE_URL`: (Se configura automáticamente con PostgreSQL)
4. Build Command: `./build.sh`
5. Start Command: `gunicorn registro_horas.wsgi:application`

## API Endpoints

- `POST /api/api-token-auth/` - Login
- `POST /api/register/` - Registro de usuario
- `GET /api/registros/` - Obtener registros
- `POST /api/registros/` - Crear registro
- `PUT /api/registros/{id}/` - Actualizar registro
- `DELETE /api/registros/{id}/` - Eliminar registro

## Funcionalidades

- ✅ Autenticación de usuarios
- ✅ Registro de entrada/salida
- ✅ Cálculo automático de horas trabajadas
- ✅ Visualización de registros históricos
- ✅ Configuración de francos
- ✅ Resumen de horas por período
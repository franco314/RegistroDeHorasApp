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

## Funcionalidades

- ✅ Autenticación de usuarios
- ✅ Registro de entrada/salida
- ✅ Cálculo automático de horas trabajadas
- ✅ Visualización de registros históricos
- ✅ Configuración de francos
- ✅ Resumen de horas por período
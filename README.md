# Sistema de Registro de Asistencia - Evento de Posgrados

Sistema web simple para registrar asistencia de estudiantes a sesiones de Zoom con directores de programas de maestría.

## 🎯 Características

- ✅ **Registro automático**: Al acceder al link, se registra la asistencia
- 📧 **Email opcional**: Los estudiantes pueden dejar su email voluntariamente
- 📊 **Exportación a Excel**: Descarga todos los registros con fecha, hora y email
- 🔗 **Links únicos**: Cada director tiene su propio link de registro
- 📈 **Estadísticas en tiempo real**: Panel de administración con métricas
- 🎨 **Diseño profesional**: Interfaz limpia y responsive
- 🌐 **Acceso global**: Funciona desde cualquier ubicación con internet

## 📁 Estructura del Proyecto

```
.
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias Python
├── Procfile                        # Configuración para Render
├── GUIA_DESPLIEGUE.md             # Guía paso a paso de despliegue
├── templates/
│   ├── index.html                 # Página principal con todos los links
│   ├── registro.html              # Página de registro individual
│   └── estadisticas.html          # Panel de estadísticas
└── registros_asistencia.xlsx      # Archivo generado automáticamente
```

## 🚀 Inicio Rápido

### Opción 1: Desarrollo Local

```bash
# 1. Clonar o descargar el proyecto
git clone <tu-repositorio>
cd evento-posgrados

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
python app.py

# 5. Abrir en navegador
# http://localhost:5000
```

### Opción 2: Despliegue en Render (Recomendado)

Ver la guía completa en: **[GUIA_DESPLIEGUE.md](GUIA_DESPLIEGUE.md)**

Resumen rápido:
1. Subir código a GitHub
2. Conectar con Render
3. Configurar como Web Service
4. ¡Listo!

## ⚙️ Configuración

### Editar Programas de Maestría

Abre `app.py` y modifica el diccionario `PROGRAMAS`:

```python
PROGRAMAS = {
    'director1': 'Tu Maestría Aquí',
    'director2': 'Otra Maestría',
    # Agrega o elimina según necesites
}
```

**Importante**: 
- Las claves (`director1`, `director2`, etc.) forman parte de la URL
- Los valores son los nombres que se mostrarán en la interfaz
- Puedes tener cualquier cantidad de programas (no necesariamente 25)

## 📋 Rutas de la Aplicación

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal con lista de todos los links |
| `/<director_id>` | Página de registro para un programa específico |
| `/api/guardar_email` | API POST para guardar emails |
| `/admin/estadisticas` | Panel de estadísticas |
| `/admin/descargar` | Descarga el archivo Excel |

## 📊 Formato del Excel

El archivo generado contiene las siguientes columnas:

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| Programa | Nombre de la maestría | Maestría en Ciencia de Datos |
| Fecha y Hora | Timestamp del registro | 2024-12-09 14:30:45 |
| Email | Email del estudiante | estudiante@universidad.edu |

**Nota**: Si el estudiante no proporciona email, aparecerá "No proporcionado"

## 🔐 Seguridad y Privacidad

- No se requiere autenticación (diseño intencional para facilitar acceso)
- No se almacena información personal más allá del email opcional
- Los datos se guardan localmente en el servidor
- Se recomienda descargar y eliminar el Excel después del evento

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0
- **Procesamiento de datos**: Pandas 2.1
- **Excel**: OpenPyXL 3.1
- **Servidor de producción**: Gunicorn 21.2
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Diseño**: Tipografía Crimson Pro + Work Sans

## 📱 Compatibilidad

- ✅ Navegadores modernos (Chrome, Firefox, Safari, Edge)
- ✅ Dispositivos móviles (iOS, Android)
- ✅ Tablets
- ✅ Responsive design

## 🐛 Solución de Problemas

### La aplicación no inicia
```bash
# Verificar que todas las dependencias estén instaladas
pip install -r requirements.txt

# Verificar que el puerto 5000 esté disponible
# En Linux/Mac: lsof -i :5000
# En Windows: netstat -ano | findstr :5000
```

### El Excel no se genera
```bash
# Verificar permisos de escritura en la carpeta
# El archivo se crea automáticamente en la primera ejecución
```

### Errores en producción (Render)
- Revisar los logs en el dashboard de Render
- Verificar que `Procfile` y `requirements.txt` estén en la raíz
- Asegurar que el repositorio sea público

## 📈 Escalabilidad

El sistema actual está diseñado para eventos medianos (hasta ~500 registros simultáneos).

Para eventos más grandes considera:
- Usar una base de datos (PostgreSQL, MySQL)
- Implementar caché (Redis)
- Usar un plan de pago en Render para más recursos

## 🤝 Contribuciones

Si encuentras bugs o tienes sugerencias:
1. Abre un Issue en GitHub
2. Describe el problema o mejora
3. Si puedes, envía un Pull Request

## 📄 Licencia

Este proyecto es de uso libre para fines educativos y eventos universitarios.

## 📞 Soporte

Para preguntas o problemas:
- Revisa primero: [GUIA_DESPLIEGUE.md](GUIA_DESPLIEGUE.md)
- Consulta la documentación de [Flask](https://flask.palletsprojects.com/)
- Consulta la documentación de [Render](https://render.com/docs)

---

**Desarrollado para el Evento de Posgrados - Universidad**

¡Éxito con tu evento! 🎓

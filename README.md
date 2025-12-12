# 🏥 Módulo de Gestión Médica para Odoo

Módulo personalizado de Odoo 17.0 para la gestión integral de citas médicas, pacientes, médicos y especialidades.

## 📋 Descripción

Este módulo permite administrar de manera completa un sistema de reservas médicas, facilitando la gestión de citas entre pacientes y médicos, organización por especialidades y seguimiento del historial de consultas.

## ✨ Características Principales

- **Gestión de Pacientes**: Registro completo de información del paciente
- **Gestión de Médicos**: Administración de doctores y sus especialidades
- **Especialidades Médicas**: Organización de médicos por especialidades
- **Sistema de Citas**: Programación y seguimiento de citas médicas
- **Vistas de Calendario**: Visualización de citas en formato calendario
- **Contadores Inteligentes**: Estadísticas automáticas de citas y pacientes
- **Estados de Citas**: Control de estados (Programada, Cancelada, Realizada)

## 🗂️ Modelos del Sistema

### 1. Paciente (`gestion.paciente`)

Gestiona la información de los pacientes del sistema.

**Campos:**
- Nombre y apellidos
- Fecha de nacimiento
- Teléfono
- Correo electrónico
- Nombre completo (campo computado)
- Contador de citas
- Historial de citas

**Funcionalidades:**
- Vista rápida de todas las citas del paciente
- Creación de nuevas citas desde el formulario del paciente

### 2. Médico (`gestion.medico`)

Administra la información de los médicos y su disponibilidad.

**Campos:**
- Nombre y apellidos
- Especialidad médica
- Disponibilidad
- Nombre completo (campo computado)
- Contador de citas
- Contador de pacientes atendidos

**Funcionalidades:**
- Vista de calendario con todas las citas del médico
- Lista de pacientes atendidos
- Estadísticas de citas y pacientes

### 3. Especialidad (`gestion.especialidad`)

Define las diferentes especialidades médicas disponibles.

**Campos:**
- Nombre de la especialidad
- Lista de médicos de esa especialidad

### 4. Cita Médica (`gestion.cita`)

Gestiona las citas entre pacientes y médicos.

**Campos:**
- Paciente
- Médico
- Fecha y hora
- Estado (Programada, Cancelada, Realizada)
- Nombre descriptivo de la cita (campo computado)

**Funcionalidades:**
- Vista de calendario
- Filtrado por estado
- Vista de lista y formulario

## 🔧 Requisitos Técnicos

- Odoo 17.0
- Python 3.10+
- PostgreSQL 15
- Docker y Docker Compose (para instalación con contenedores)

## 🚀 Instalación

### Opción 1: Instalación con Docker (Recomendada)

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/Modulo-Odoo-Medico.git
cd Modulo-Odoo-Medico/Odoo_Modulo_Medico
```

2. **Iniciar los contenedores:**
```bash
docker-compose up -d
```

3. **Acceder a Odoo:**
   - URL: `http://localhost:8069`
   - Usuario: `admin`
   - Contraseña: (la que configures en la primera instalación)

4. **Instalar el módulo:**
   - Ir a `Aplicaciones`
   - Buscar "Gestión de Reservas Médicas"
   - Hacer clic en `Instalar`

### Opción 2: Instalación Manual

1. Copiar la carpeta `gestion_medica` en el directorio de addons de Odoo
2. Actualizar la lista de módulos en Odoo
3. Instalar el módulo desde el menú de Aplicaciones

## 🔑 Acceso al Sistema

### Credenciales de Acceso
- **URL:** [http://localhost:8069](http://localhost:8069)
- **Email:** admin@gmail.com
- **Password:** admin
- **Base de datos:** gestion_medica_db

### Instrucciones de Acceso Rápido

1. **Iniciar Docker:**
   ```bash
   cd Odoo_Modulo_Medico
   docker-compose up
   ```

2. **Abrir el navegador en:** [http://localhost:8069](http://localhost:8069)

3. **Iniciar sesión** con las credenciales indicadas arriba

### 🎥 Video Demostración
Puedes ver el funcionamiento completo del módulo en el siguiente enlace:
[Ver Video de Demostración](https://drive.google.com/file/d/1s_a-Mgr4AqfJNxKzI1x4BnKvMdwxSsI1/view)

## 📖 Uso del Módulo

### Configuración Inicial

1. **Crear Especialidades:**
   - Ir a `Gestión Médica > Especialidades`
   - Agregar especialidades como: Cardiología, Pediatría, Dermatología, etc.

2. **Registrar Médicos:**
   - Ir a `Gestión Médica > Médicos`
   - Crear nuevos médicos asignándoles especialidades y disponibilidad

3. **Registrar Pacientes:**
   - Ir a `Gestión Médica > Pacientes`
   - Agregar la información completa de los pacientes

### Gestión de Citas

1. **Crear una Cita:**
   - Ir a `Gestión Médica > Citas`
   - Seleccionar paciente y médico
   - Establecer fecha y hora
   - Guardar

2. **Vista de Calendario:**
   - Visualizar todas las citas en formato calendario
   - Filtrar por médico o paciente
   - Cambiar estados de las citas

3. **Seguimiento:**
   - Actualizar estados: Programada → Realizada / Cancelada
   - Ver historial de citas por paciente
   - Ver agenda de citas por médico

## 📁 Estructura del Proyecto

```
Modulo-Odoo-Medico/
├── Odoo_Modulo_Medico/
│   ├── addons/
│   │   └── gestion_medica/
│   │       ├── __init__.py
│   │       ├── __manifest__.py
│   │       ├── models/
│   │       │   ├── __init__.py
│   │       │   ├── paciente.py
│   │       │   ├── medico.py
│   │       │   ├── especialidad.py
│   │       │   └── cita.py
│   │       ├── views/
│   │       │   ├── paciente_views.xml
│   │       │   ├── medico_views.xml
│   │       │   ├── especialidad_views.xml
│   │       │   ├── cita_views.xml
│   │       │   └── menu_views.xml
│   │       └── security/
│   │           └── ir.model.access.csv
│   ├── config/
│   │   └── odoo.conf
│   ├── docker-compose.yml
│   └── Dockerfile
└── README.md
```

## 🔐 Seguridad

El módulo incluye configuración de permisos de acceso (`ir.model.access.csv`) para controlar el acceso a los diferentes modelos del sistema.

## 🛠️ Tecnologías Utilizadas

- **Odoo Framework 17.0**: Framework ERP de código abierto
- **Python**: Lógica de negocio y modelos
- **XML**: Definición de vistas e interfaces
- **PostgreSQL**: Base de datos relacional
- **Docker**: Contenedorización de la aplicación

## 👨‍💻 Autor

**Alex Jiménez Quiñonero**

## 📄 Licencia

Este proyecto está bajo la licencia LGPL-3 (GNU Lesser General Public License v3.0)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.

## 📞 Soporte

Si tienes alguna pregunta o problema, no dudes en abrir un issue en el repositorio.

---

⭐ Si este módulo te ha sido útil, no olvides darle una estrella al repositorio.

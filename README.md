# Sistema de Gestión de Inventario

[![CI Pipeline](https://github.com/jasbleidy2005/inventory-management/actions/workflows/ci.yml/badge.svg)](https://github.com/jasbleidy2005/inventory-management/actions)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3.0-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Code Coverage](https://img.shields.io/badge/coverage-64%25-yellow)](htmlcov/index.html)

Sistema completo de gestión de inventario con API REST, interfaz web y pipeline CI/CD automatizado.

---

##  Características

-  **API REST completa** con operaciones CRUD
-  **Arquitectura por capas** (Modelos → Servicios → Controladores)
-  **Base de datos relacional** con SQLite + SQLAlchemy ORM
-  **Interfaz web funcional** para gestión de inventario
-  **Suite completa de pruebas** (Unitarias, Integración, E2E, Frontend)
-  **Cobertura de código** del 64%
-  **Análisis estático** con Flake8 y Bandit
-  **Pipeline CI/CD** automatizado con GitHub Actions
-  **Documentación completa** con plan de pruebas detallado

---

##  Arquitectura

### Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (Flask)                      │
│              Templates HTML + CSS + JS                   │
│                   Port: 5001                             │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP Requests
                     ▼
┌─────────────────────────────────────────────────────────┐
│                 BACKEND API (Flask)                      │
│                    Port: 5000                            │
├─────────────────────────────────────────────────────────┤
│               CONTROLLERS (Routes)                       │
│        /api/categories  |  /api/products                 │
├─────────────────────────────────────────────────────────┤
│              SERVICES (Business Logic)                   │
│      CategoryService  |  ProductService                  │
├─────────────────────────────────────────────────────────┤
│               MODELS (ORM Entities)                      │
│          Category Model | Product Model                  │
└────────────────────┬────────────────────────────────────┘
                     │ SQLAlchemy ORM
                     ▼
┌─────────────────────────────────────────────────────────┐
│              DATABASE (SQLite)                           │
│         categories | products                            │
└─────────────────────────────────────────────────────────┘
```

### Componentes

#### Backend (Flask)
- **Modelos**: Entidades de base de datos (Category, Product)
- **Servicios**: Lógica de negocio y validaciones
- **Controladores**: Endpoints REST y manejo de peticiones
- **Base de datos**: SQLite con SQLAlchemy ORM

#### Frontend (Flask + Jinja2)
- **Templates**: Vistas HTML dinámicas
- **Estáticos**: CSS para estilos, JavaScript para interactividad
- **Consumo de API**: Peticiones HTTP al backend

#### Testing
- **Unitarias**: Lógica de servicios aislada
- **Integración**: Endpoints API + Base de datos
- **Frontend**: Rutas y respuestas del frontend
- **E2E**: Flujo completo con Selenium

---

##  Base de Datos

### Diagrama Entidad-Relación

```
┌──────────────────┐         ┌────────────────────────┐
│    Category      │         │       Product          │
├──────────────────┤         ├────────────────────────┤
│ id (PK)          │────┐    │ id (PK)                │
│ name             │    └───<│ category_id (FK)       │
└──────────────────┘         │ name                   │
   1 : N                     │ description            │
                             │ price                  │
                             │ stock                  │
                             └────────────────────────┘
```

### Esquema de Tablas

#### Tabla: `categories`

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Identificador único |
| name | VARCHAR(100) | NOT NULL, UNIQUE | Nombre de la categoría |

**Ejemplo:**
```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);
```

#### Tabla: `products`

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Identificador único |
| name | VARCHAR(100) | NOT NULL | Nombre del producto |
| description | TEXT | | Descripción detallada |
| price | FLOAT | NOT NULL | Precio del producto |
| stock | INTEGER | NOT NULL | Cantidad en inventario |
| category_id | INTEGER | FOREIGN KEY → categories(id) | Categoría asociada |

**Ejemplo:**
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    stock INTEGER NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
```

### Relaciones
- Una **categoría** puede tener **múltiples productos** (1:N)
- Un **producto** pertenece a **una categoría** (N:1)

---

##  Instalación

### Requisitos Previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git
- Google Chrome (para pruebas E2E)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/jasbleidy2005/inventory-management.git
cd inventory-management
```

### Paso 2: Crear Entorno Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r backend/requirements.txt
```

**Dependencias principales:**
- Flask 2.3.0
- Flask-SQLAlchemy 3.0.0
- Flask-CORS 4.0.0
- pytest 7.4.0
- pytest-cov 4.1.0
- Selenium 4.15.0
- Flake8 6.0.0
- Bandit 1.7.5

### Paso 4: Configurar Variables de Entorno (Opcional)

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta-super-segura
DATABASE_URL=sqlite:///inventory.db
BACKEND_URL=http://localhost:5000
```

### Paso 5: Inicializar la Base de Datos

```bash
python run_backend.py
```

Esto creará automáticamente el archivo `inventory.db` con las tablas necesarias.

---

##  Uso

### Ejecutar el Backend (API)

En una terminal:

```bash
cd inventory-management
python run_backend.py
```

**Salida esperada:**
```
============================================================
INITIALIZING BACKEND SERVER...
============================================================
 Database initialized
 Controllers registered
============================================================
 Backend Server Starting on http://localhost:5000
============================================================
```

El backend estará disponible en: **http://localhost:5000**

### Ejecutar el Frontend

En **otra terminal** (sin cerrar la anterior):

```bash
cd inventory-management/frontend
python app.py
```

**Salida esperada:**
```
============================================================
 Frontend Server Starting on http://localhost:5001
============================================================
```

El frontend estará disponible en: **http://localhost:5001**

### Acceder a la Aplicación

1. Abre tu navegador en: **http://localhost:5001**
2. Navega a **Categorías** para crear categorías
3. Navega a **Productos** para gestionar productos

---

##  API Endpoints

### Categorías

| Método | Endpoint | Descripción | Body | Respuesta |
|--------|----------|-------------|------|-----------|
| GET | `/api/categories` | Listar todas las categorías | - | `200` Array de categorías |
| POST | `/api/categories` | Crear nueva categoría | `{"name": "string"}` | `201` Categoría creada |
| GET | `/api/categories/{id}` | Obtener categoría por ID | - | `200` Categoría o `404` |
| PUT | `/api/categories/{id}` | Actualizar categoría | `{"name": "string"}` | `200` Actualizada o `404` |
| DELETE | `/api/categories/{id}` | Eliminar categoría | - | `204` Sin contenido o `404` |

### Productos

| Método | Endpoint | Descripción | Body | Respuesta |
|--------|----------|-------------|------|-----------|
| GET | `/api/products` | Listar todos los productos | - | `200` Array de productos |
| POST | `/api/products` | Crear nuevo producto | Ver ejemplo ↓ | `201` Producto creado |
| GET | `/api/products/{id}` | Obtener producto por ID | - | `200` Producto o `404` |
| PUT | `/api/products/{id}` | Actualizar producto | Ver ejemplo ↓ | `200` Actualizado o `404` |
| DELETE | `/api/products/{id}` | Eliminar producto | - | `204` Sin contenido o `404` |

### Ejemplos de Uso

#### Crear Categoría

```bash
curl -X POST http://localhost:5000/api/categories \
  -H "Content-Type: application/json" \
  -d '{"name": "Electrónicos"}'
```

**Respuesta:**
```json
{
  "id": 1,
  "name": "Electrónicos"
}
```

#### Crear Producto

```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop HP",
    "description": "Laptop HP 15.6 pulgadas, 8GB RAM",
    "price": 899.99,
    "stock": 10,
    "category_id": 1
  }'
```

**Respuesta:**
```json
{
  "id": 1,
  "name": "Laptop HP"
}
```

#### Listar Productos

```bash
curl http://localhost:5000/api/products
```

**Respuesta:**
```json
[
  {
    "id": 1,
    "name": "Laptop HP",
    "description": "Laptop HP 15.6 pulgadas, 8GB RAM",
    "price": 899.99,
    "stock": 10,
    "category_id": 1
  }
]
```

#### Actualizar Producto

```bash
curl -X PUT http://localhost:5000/api/products/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop HP Actualizada",
    "description": "Nueva descripción",
    "price": 799.99,
    "stock": 15,
    "category_id": 1
  }'
```

#### Eliminar Producto

```bash
curl -X DELETE http://localhost:5000/api/products/1
```
---

##  Pruebas

### Ejecutar Todas las Pruebas

```bash
pytest tests/ -v
```

### Pruebas por Tipo

#### Unitarias (9 pruebas)
```bash
pytest tests/unit/ -v
```
Prueban la lógica de negocio en servicios de forma aislada.

#### Integración (6 pruebas)
```bash
pytest tests/integration/ -v
```
Prueban los endpoints de la API con base de datos en memoria.

#### Frontend (6 pruebas)
```bash
pytest tests/frontend/ -v
```
Prueban las rutas y contenido del frontend.

#### E2E (1 prueba)
```bash
pytest tests/e2e/ -v
```
Prueba el flujo completo con navegador automatizado.

### Cobertura de Código

#### Generar Reporte de Cobertura

```bash
pytest tests/ --cov=backend --cov-report=html --cov-report=term
```

#### Ver Reporte HTML

```bash
# Windows
start htmlcov/index.html

# Linux/Mac
open htmlcov/index.html
```

### Resultados de Pruebas

| Tipo de Prueba | Total | Pasadas | Fallidas | % Éxito |
|----------------|-------|---------|----------|---------|
| **Unitarias** | 9 | 9 | 0 | 100% |
| **Integración** | 6 | 6 | 0 | 100% |
| **Frontend** | 6 | 6 | 0 | 100% |
| **E2E** | 1 | 1 | 0 | 100% |
| **TOTAL** | **22** | **22** | **0** | **100%**  |

---

##  Análisis Estático

### Flake8 - Estilo de Código PEP8

```bash
flake8 backend/ --max-line-length=120 --extend-ignore=W292,W293,E402
```

**Resultado esperado:**
```
 0 errores críticos
 Código cumple con PEP8
```

### Bandit - Análisis de Seguridad

```bash
bandit -r backend/ -ll
```

**Resultado esperado:**
```
Run started:2024-12-04 14:35:49.694011

Test results:
>> Issue: [B104:hardcoded_bind_all_interfaces] Possible binding to all interfaces.
   Severity: Medium   Confidence: Medium
   (Mitigado con bind a 127.0.0.1)

Code scanned:
        Total lines of code: 173
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                High: 0 
                Medium: 1 (Mitigado)
                Low: 0 
```

---

##  CI/CD Pipeline

### GitHub Actions Workflow

El proyecto incluye un pipeline automatizado que se ejecuta en cada push o pull request.

**Archivo:** `.github/workflows/ci.yml`


### Ver Estado del Pipeline

[![CI Pipeline](https://github.com/jasbleidy2005/inventory-management/actions/workflows/ci.yml/badge.svg)](https://github.com/jasbleidy2005/inventory-management/actions)

Visita: https://github.com/jasbleidy2005/inventory-management/actions

### Resultado Exitoso

```
 ==========================================
           ALL TESTS PASSED!
 ==========================================
 OK
```

---

##  Tecnologías

### Backend
| Tecnología | Versión | Uso |
|------------|---------|-----|
| Python | 3.9+ | Lenguaje principal |
| Flask | 2.3.0 | Framework web |
| SQLAlchemy | 3.0.0 | ORM para base de datos |
| Flask-CORS | 4.0.0 | Manejo de CORS |
| SQLite | 3.x | Base de datos |

### Frontend
| Tecnología | Versión | Uso |
|------------|---------|-----|
| Flask | 2.3.0 | Servidor frontend |
| Jinja2 | 3.x | Motor de templates |
| HTML5 | - | Estructura |
| CSS3 | - | Estilos |
| JavaScript | ES6 | Interactividad |

### Testing
| Tecnología | Versión | Uso |
|------------|---------|-----|
| pytest | 7.4.0 | Framework de pruebas |
| pytest-flask | 1.2.0 | Pruebas Flask |
| pytest-cov | 4.1.0 | Cobertura de código |
| Selenium | 4.15.0 | Pruebas E2E |

### Calidad de Código
| Tecnología | Versión | Uso |
|------------|---------|-----|
| Flake8 | 6.0.0 | Análisis estático |
| Bandit | 1.7.5 | Análisis de seguridad |

### DevOps
| Tecnología | Versión | Uso |
|------------|---------|-----|
| GitHub Actions | - | CI/CD |
| Git | 2.x | Control de versiones |

---

##  Plan de Pruebas

### Documento Completo

Ver: **[docs/plan_de_pruebas.md](docs/plan_de_pruebas.md)**

### Resumen Ejecutivo

#### Métricas Globales

```
┌───────────────────────────────────────────────┐
│        RESUMEN DE PRUEBAS - PROYECTO          │
├───────────────────────────────────────────────┤
│ Total de Pruebas:        24                   │
│ Pruebas Pasadas:         24                 │
│ Pruebas Fallidas:        0                    │
│ Tasa de Éxito:           100%                 │
│ Cobertura de Código:     64%                  │
│ Estado General:           APROBADO          │
└───────────────────────────────────────────────┘
```

#### Desglose por Tipo

| Tipo | Cantidad | Estado | Cobertura |
|------|----------|--------|-----------|
| **Pruebas Unitarias** | 9 |  100% | Servicios |
| **Pruebas de Integración** | 6 |  100% | API + DB |
| **Pruebas de Frontend** | 6 |  100% | Rutas |
| **Pruebas E2E** | 1 |  100% | Flujo completo |
| **Análisis Estático** | 2 |  100% | Calidad |

#### Casos de Prueba Destacados

1. **PU-001**: Crear Categoría (Service) 
2. **PI-001**: POST /api/categories 
3. **PF-001**: Ruta Principal del Frontend 
4. **PE2E-001**: Flujo Completo CRUD 
5. **AE-001**: Análisis Flake8 
6. **AE-002**: Análisis Bandit 


### Checklist antes de PR

- [ ] Las pruebas pasan localmente
- [ ] Se agregaron pruebas para nuevas funcionalidades
- [ ] El código cumple con PEP8 (Flake8)
- [ ] No hay vulnerabilidades de seguridad (Bandit)
- [ ] Se actualizó la documentación

---

##  Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

### Repositorio
-  URL: https://github.com/jasbleidy2005/inventory-management
-  Issues: https://github.com/jasbleidy2005/inventory-management/issues
-  Projects: https://github.com/jasbleidy2005/inventory-management/projects

### Recursos Adicionales
-  [Documentación de Flask](https://flask.palletsprojects.com/)
-  [Documentación de pytest](https://docs.pytest.org/)
-  [Documentación de SQLAlchemy](https://www.sqlalchemy.org/)

---


**Desarrollado con AMOR por Jasbleidy**

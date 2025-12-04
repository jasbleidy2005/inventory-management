# Inventory Management System

## Descripción del Proyecto
Este proyecto es un sistema de gestión de inventario de productos que incluye una API REST y una interfaz gráfica. Permite la gestión de categorías y productos, ofreciendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para ambos.

## Arquitectura
El sistema está estructurado en dos partes principales: el backend y el frontend.

### Backend
- **Tecnología**: Python con Flask.
- **Estructura**:
  - **Modelos**: Define las entidades `Category` y `Product`.
  - **Servicios**: Contiene la lógica de negocio para manejar categorías y productos.
  - **Controladores**: Maneja las solicitudes HTTP y se comunica con los servicios.
  - **Base de Datos**: Utiliza una base de datos para almacenar información sobre categorías y productos.

### Frontend
- **Tecnología**: Python con Flask.
- **Estructura**:
  - **Templates**: Archivos HTML que definen la interfaz de usuario.
  - **Estáticos**: Archivos CSS y JavaScript para el estilo y la funcionalidad del cliente.

## Base de Datos
El sistema utiliza dos tablas principales:
- **categories**: 
  - `id`: Identificador único de la categoría.
  - `name`: Nombre de la categoría.
  
- **products**: 
  - `id`: Identificador único del producto.
  - `name`: Nombre del producto.
  - `description`: Descripción del producto.
  - `price`: Precio del producto.
  - `stock`: Cantidad disponible en inventario.
  - `category_id`: Clave foránea que relaciona el producto con su categoría.

## Instrucciones para Ejecutar la API
1. Navega al directorio `backend`.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `python app.py`.
4. La API estará disponible en `http://localhost:5000`.

## Instrucciones para Ejecutar la Interfaz Gráfica
1. Navega al directorio `frontend`.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `python app.py`.
4. La interfaz gráfica estará disponible en `http://localhost:5000`.

## Ejecución de Pruebas
Para ejecutar las pruebas automatizadas:
1. Navega al directorio `tests`.
2. Ejecuta `pytest` para correr todas las pruebas unitarias, de integración y E2E.

## Análisis Estático de Código
Para realizar un análisis estático del código, utiliza la herramienta correspondiente (por ejemplo, Flake8) ejecutando el comando adecuado en el directorio del proyecto.

## Pipeline de Integración Continua
El proyecto incluye un flujo de trabajo en GitHub Actions que:
1. Instala las dependencias del backend y frontend.
2. Ejecuta las pruebas unitarias.
3. Ejecuta las pruebas de integración.
4. Ejecuta las pruebas E2E.
5. Realiza el análisis estático de código.

Si todas las etapas finalizan correctamente, se imprimirá "OK". Si alguna etapa falla, el pipeline se marcará como fallido.

## Conclusión
Este sistema de gestión de inventario proporciona una solución completa para manejar productos y categorías, con una arquitectura bien definida y un conjunto robusto de pruebas automatizadas.
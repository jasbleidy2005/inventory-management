# Plan de Pruebas

## Introducción
Este documento describe los casos de prueba para el sistema de gestión de inventario de productos. Se detallan los tipos de pruebas, los prerrequisitos, los pasos a seguir y los resultados esperados.

## Casos de Prueba

### 1. Crear Categoría
- **Tipo de prueba:** Prueba de integración
- **Descripción:** Verificar que se puede crear una nueva categoría en el sistema.
- **Prerrequisitos:** La API debe estar en funcionamiento.
- **Pasos:**
  1. Enviar una solicitud POST a `/api/categories` con el nombre de la categoría.
  2. Verificar que la respuesta tenga un código de estado 201.
  3. Consultar la lista de categorías para confirmar que la nueva categoría fue añadida.
- **Resultado esperado:** La categoría se crea correctamente y aparece en la lista de categorías.
- **Resultado obtenido:** [Por completar tras la ejecución]

### 2. Crear Producto
- **Tipo de prueba:** Prueba de integración
- **Descripción:** Verificar que se puede crear un nuevo producto en el sistema.
- **Prerrequisitos:** La API debe estar en funcionamiento y debe existir al menos una categoría.
- **Pasos:**
  1. Enviar una solicitud POST a `/api/products` con los detalles del producto (nombre, descripción, precio, stock, category_id).
  2. Verificar que la respuesta tenga un código de estado 201.
  3. Consultar la lista de productos para confirmar que el nuevo producto fue añadido.
- **Resultado esperado:** El producto se crea correctamente y aparece en la lista de productos.
- **Resultado obtenido:** [Por completar tras la ejecución]

### 3. Listar Productos
- **Tipo de prueba:** Prueba de integración
- **Descripción:** Verificar que se pueden listar todos los productos en el sistema.
- **Prerrequisitos:** La API debe estar en funcionamiento y debe haber productos en la base de datos.
- **Pasos:**
  1. Enviar una solicitud GET a `/api/products`.
  2. Verificar que la respuesta tenga un código de estado 200.
  3. Confirmar que la lista de productos devuelta contiene los productos existentes.
- **Resultado esperado:** La lista de productos se devuelve correctamente.
- **Resultado obtenido:** [Por completar tras la ejecución]

### 4. Actualizar Producto
- **Tipo de prueba:** Prueba de integración
- **Descripción:** Verificar que se puede actualizar un producto existente.
- **Prerrequisitos:** La API debe estar en funcionamiento y debe existir al menos un producto.
- **Pasos:**
  1. Enviar una solicitud PUT a `/api/products/{id}` con los nuevos detalles del producto.
  2. Verificar que la respuesta tenga un código de estado 200.
  3. Consultar el producto actualizado para confirmar que los cambios se han aplicado.
- **Resultado esperado:** El producto se actualiza correctamente.
- **Resultado obtenido:** [Por completar tras la ejecución]

### 5. Eliminar Producto
- **Tipo de prueba:** Prueba de integración
- **Descripción:** Verificar que se puede eliminar un producto existente.
- **Prerrequisitos:** La API debe estar en funcionamiento y debe existir al menos un producto.
- **Pasos:**
  1. Enviar una solicitud DELETE a `/api/products/{id}`.
  2. Verificar que la respuesta tenga un código de estado 204.
  3. Consultar la lista de productos para confirmar que el producto ha sido eliminado.
- **Resultado esperado:** El producto se elimina correctamente.
- **Resultado obtenido:** [Por completar tras la ejecución]

## Conclusión
Este plan de pruebas cubre los casos más relevantes para la gestión de categorías y productos en el sistema. Se recomienda ejecutar estos casos de prueba tras cada modificación en el código para asegurar la calidad del sistema.
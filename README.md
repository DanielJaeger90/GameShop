🎮 Gaming Shop ERP — Documentación del Proyecto
📌 Descripción general

Este proyecto es una aplicación web tipo ERP desarrollada en Python con Streamlit, orientada a la gestión de inventario, ventas y usuarios de una tienda de productos gaming.

El sistema simula un entorno empresarial real, incluyendo control de stock, roles de usuario, registro de ventas y análisis mediante dashboard.

👥 Tipos de usuarios y roles

El sistema cuenta con tres roles principales, cada uno con permisos específicos:

👑 Admin

Es el usuario con control total del sistema.

✔ Funcionalidades:
Crear y eliminar usuarios
Gestionar productos (CRUD completo)
Acceder a todas las métricas del dashboard
Supervisar ventas y logs
🎯 Objetivo:

Permitir la administración completa del sistema y la supervisión general.

🧑 Usuario_1 (Empleado)

Es un usuario con permisos limitados orientado a tareas operativas.

✔ Funcionalidades:
Visualizar productos
Buscar y filtrar catálogo
Realizar pedidos (compras internas)
❌ Restricciones:
No puede crear ni eliminar productos
No puede gestionar usuarios
🧑‍💼 Usuario_2 (Encargado)

Usuario intermedio con permisos ampliados.

✔ Funcionalidades:
Visualizar productos
Crear, actualizar y eliminar productos
Gestionar stock
Realizar pedidos
🎯 Objetivo:

Actuar como responsable operativo del inventario.

🛒 Sistema de ventas

Cada vez que se realiza un pedido:

Se descuenta stock automáticamente
Se registra la venta en el sistema
Se almacena el usuario que realizó la acción
Se asigna una tienda de destino (Tienda_1 o Tienda_2)
🧾 Sistema de logs (auditoría)

Todas las acciones relevantes quedan registradas en un historial:

Creación de productos
Eliminación o actualización
Ventas realizadas
Acciones de usuarios
🎯 Objetivo:

Garantizar trazabilidad y control del sistema.

📊 Dashboard

El dashboard permite visualizar el estado general del sistema en tiempo real:

📦 Stock total
📉 Productos con stock crítico
❌ Productos sin stock
🛒 Ventas totales
💰 Ingresos generados
🏆 Producto más vendido

Además, incluye gráficos dinámicos para análisis visual.

🚨 Sistema de alertas

El sistema genera alertas automáticas cuando:

Un producto tiene stock crítico
Un producto se queda sin stock

Esto permite una gestión preventiva del inventario.

👥 Gestión de usuarios

Solo el admin puede:

Crear nuevos usuarios
Asignar roles
Eliminar usuarios

Cada usuario tiene credenciales independientes y un rol asignado.

🛍️ Sistema de pedidos

El sistema de pedidos incluye:

Formulario de selección de producto
Cantidad a comprar
Selección de tienda destino
Actualización automática de stock
🏗️ Arquitectura del proyecto

El proyecto está organizado en módulos para mejorar la mantenibilidad:

📁 data/

Contiene los archivos JSON que simulan una base de datos:

productos.json
usuarios.json
ventas.json
logs.json
📁 modules/

Contiene la lógica principal de la aplicación:

CRUD de productos
gestión de usuarios
sistema de pedidos
dashboard
📁 utils/

Herramientas auxiliares del sistema:

gestión de archivos JSON
exportación de datos
autenticación
estilos
📁 config/

Contiene la configuración global:

rutas del sistema
roles y permisos
reglas de negocio
configuración visual
⚙️ Tecnologías utilizadas
🐍 Python: lenguaje principal del proyecto
🌐 Streamlit: interfaz web interactiva
📊 Pandas: análisis y manipulación de datos
📈 Matplotlib: generación de gráficos
📁 JSON: almacenamiento de datos
🧾 BytesIO: exportación de archivos Excel/CSV
⏰ Datetime: gestión de fechas y registros
🎯 Objetivo del proyecto

El objetivo principal es simular un sistema ERP funcional que permita:

Gestionar inventario de forma eficiente
Controlar usuarios con roles diferenciados
Registrar ventas y movimientos
Analizar datos mediante dashboard
Mantener trazabilidad completa del sistema
🚀 Evolución del proyecto

Inicialmente, el sistema fue diseñado como una tienda tipo “Steam”.

Sin embargo, evolucionó hacia un sistema de gestión empresarial (ERP) debido a la incorporación de:

sistema de roles
control de inventario
sistema de ventas
dashboard analítico
🧠 Conclusión

Este proyecto representa una simulación de un sistema empresarial real, integrando:

✔ arquitectura modular
✔ control de accesos
✔ persistencia de datos
✔ análisis de información
✔ automatización de procesos

🏁 Frase final

“El sistema ha sido diseñado siguiendo principios de modularidad, escalabilidad y separación de responsabilidades, simulando un entorno ERP real aplicado a la gestión de inventario y ventas.”

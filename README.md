# 🛒 Sistema de Gestión de Ventas - TAMBO+

Sistema de gestión de inventario y ventas para minimarket desarrollado en Python con interfaz gráfica Tkinter.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)

## 📋 Descripción

Sistema desarrollado como proyecto académico para optimizar la gestión del almacén de un minimarket, permitiendo el registro, control y consulta eficiente del inventario de productos mediante la implementación de estructuras de datos y algoritmos de ordenamiento.

## 🎯 Características Principales

- ✅ **Registro de ventas** con código, producto, precio y cantidad
- ✅ **Visualización de inventario** en tiempo real
- ✅ **Algoritmos de ordenamiento implementados:**
  - Ordenamiento Burbuja (por precio)
  - QuickSort recursivo (por código y cantidad)
- ✅ **Búsqueda y filtrado** de productos en tiempo real
- ✅ **Reportes estadísticos completos:**
  - Total acumulado de ventas
  - Ticket promedio
  - Top 5 productos más vendidos
  - Top 5 productos menos vendidos
- ✅ **Cálculo recursivo** de totales de venta
- ✅ **Interfaz gráfica intuitiva** con tema personalizado TAMBO+
- ✅ **Catálogo de productos** con más de 80 items predefinidos

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias
```bash
pip install pillow
```

### Ejecutar el Sistema
```bash
python menuCasual.py
```

## 📂 Estructura del Proyecto
```
sistema-gestion-minimarket/
│
├── menuCasual.py          # Código principal del sistema
├── logo_tambo.png         # Logo de la aplicación (opcional)
└── README.md              # Documentación
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación principal
- **Tkinter** - Librería para interfaz gráfica de usuario (GUI)
- **PIL/Pillow** - Procesamiento y visualización de imágenes

## 💡 Algoritmos Implementados

### 1. Ordenamiento Burbuja
Algoritmo de ordenamiento por comparación e intercambio.
- **Complejidad temporal:** O(n²)
- **Uso en el sistema:** Ordenamiento de productos por precio
- **Ventaja:** Implementación simple y directa

### 2. QuickSort Recursivo
Algoritmo de ordenamiento eficiente por división y conquista.
- **Complejidad temporal:** O(n log n) en promedio
- **Uso en el sistema:** Ordenamiento por código y cantidad
- **Ventaja:** Mayor eficiencia para grandes conjuntos de datos

### 3. Suma Recursiva
Algoritmo recursivo para cálculo de totales.
- **Complejidad temporal:** O(n)
- **Uso en el sistema:** Cálculo del total recaudado en cierre de caja
- **Ventaja:** Demostración de técnicas de recursión

## 📊 Funcionalidades del Sistema

### 🔹 Registrar Venta
Permite ingresar nuevas ventas con validación de datos:
- Código del producto (único por producto)
- Descripción del producto
- Precio unitario (S/)
- Cantidad vendida

**Características especiales:**
- Generación aleatoria de ventas para pruebas
- Validación de códigos duplicados
- Mensajes de confirmación en tiempo real

### 🔹 Ver Inventario
Visualización completa del inventario en formato tabla:
- Código de producto
- Nombre del producto
- Precio unitario
- Cantidad en stock
- Total por producto

### 🔹 Ordenar Lista
Opciones múltiples de ordenamiento:
- **Por precio** → Algoritmo Burbuja
- **Por código** → QuickSort
- **Por cantidad** → QuickSort

### 🔹 Buscar Producto
Sistema de búsqueda dinámica en tiempo real:
- Búsqueda por código del producto
- Búsqueda por nombre del producto
- Filtrado instantáneo mientras se escribe

### 🔹 Reporte de Ventas
Dashboard con estadísticas completas:
- **Total acumulado** de todas las ventas
- **Ticket promedio** por transacción
- **Top 5 productos más vendidos** (por cantidad)
- **Top 5 productos menos vendidos** (por cantidad)

### 🔹 Cierre de Caja
Cálculo del total recaudado usando algoritmo recursivo.
- Suma recursiva de todas las transacciones
- Visualización del monto total en formato destacado

## 🎨 Interfaz de Usuario

El sistema cuenta con una interfaz gráfica profesional que incluye:

- **Panel lateral de navegación** con botones de acceso rápido
- **Área principal de trabajo** adaptable según la función seleccionada
- **Tablas interactivas** con scroll para grandes cantidades de datos
- **Formularios de entrada** con validación
- **Esquema de colores** inspirado en la marca TAMBO+
  - Morado corporativo (#6A1B9A)
  - Amarillo de acento (#FFD600)
  - Diseño limpio y minimalista

## 📦 Catálogo de Productos

El sistema incluye un catálogo predefinido con más de 80 productos organizados en categorías:

- 🥤 Bebidas (gaseosas, agua, energizantes, jugos)
- 🍺 Licores (cerveza, ron, vodka, whisky, vino, pisco)
- 🍿 Snacks (papas, galletas, chocolates, caramelos)
- 🍔 Comida rápida (empanadas, hamburguesas, pizza, sandwich)
- ☕ Bebidas calientes (café, cappuccino)
- 🛒 Productos varios (cigarros, hielo, preservativos, papel higiénico)

## 👨‍💻 Desarrollo

**Autor:** Proyecto académico  
**Curso:** Estructuras de Datos y Algoritmos  
**Institución:** [Tu Universidad]  
**Año:** 2024

## 📈 Análisis de Complejidad

| Operación | Algoritmo | Complejidad |
|-----------|-----------|-------------|
| Inserción de venta | Lista simple | O(1) |
| Búsqueda de producto | Búsqueda lineal | O(n) |
| Ordenamiento por precio | Burbuja | O(n²) |
| Ordenamiento por código/cantidad | QuickSort | O(n log n) |
| Cálculo de total | Recursión | O(n) |

## 🔄 Mejoras Futuras

Posibles extensiones del proyecto:
- [ ] Implementación de Árbol Binario de Búsqueda para optimizar búsquedas
- [ ] Persistencia de datos en base de datos o archivos
- [ ] Generación de reportes en PDF
- [ ] Sistema de usuarios y autenticación
- [ ] Control de stock con alertas de reposición
- [ ] Historial de transacciones con fechas
- [ ] Gráficos estadísticos con matplotlib

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 📞 Contacto

Para consultas o sugerencias sobre el proyecto:
- **GitHub:** [@Seddru13](https://github.com/Seddru13)
- **Repositorio:** [sistema-gestion-minimarket](https://github.com/Seddru13/sistema-gestion-minimarket)

---

⭐ **Si este proyecto te fue útil, considera darle una estrella en GitHub**

Desarrollado con 💜 para el curso de Estructuras de Datos

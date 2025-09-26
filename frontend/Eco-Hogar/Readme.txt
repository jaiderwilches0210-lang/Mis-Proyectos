# Eco-Hogar Backend

Este proyecto es el backend de la aplicación Eco-Hogar, construido con **Spring Boot 3** y **Maven**. Se encarga de gestionar la base de datos (productos y ventas), procesar las peticiones del frontend y servir como una API REST.

---

### Requisitos

Antes de iniciar, asegúrate de tener instalado lo siguiente:

* **Java Development Kit (JDK) 24 o superior**
* **Maven**
* **MySQL Workbench** o una base de datos MySQL

---

### Configuración de la base de datos

1.  Abre tu cliente de MySQL (por ejemplo, MySQL Workbench).
2.  Crea una nueva base de datos llamada `ecohogar`.
3.  El proyecto está configurado para conectarse a esta base de datos automáticamente. No necesitas ejecutar ningún script SQL, ya que Spring Boot se encargará de crear las tablas (`productos`, `ventas` y `venta_productos`) al iniciar la aplicación.

---

### Inicio del servidor

Para ejecutar el servidor de Spring Boot, sigue estos pasos:

1.  Abre una terminal (CMD, PowerShell, o la terminal integrada de tu editor de código).
2.  Navega a la carpeta principal del proyecto (donde se encuentra el archivo `pom.xml`). Si tu proyecto está en `G:\Mi unidad\Programacion\js\Eco-Hogar\eco-hogar-backend\backend`, usa el siguiente comando:

    ```bash
    cd "G:\Mi unidad\Programacion\js\Eco-Hogar\eco-hogar-backend\backend"
    ```

3.  Ejecuta el comando de Maven para compilar y arrancar la aplicación:

    ```bash
    mvn spring-boot:run
    ```

4.  El servidor estará activo cuando veas el mensaje **"Started BackendApplication"**. Se ejecutará en el puerto 8080.

---

### Endpoints de la API

El backend expone los siguientes endpoints para interactuar con los datos:

| HTTP Method | Endpoint                       | Descripción                                 |
|-------------|--------------------------------|---------------------------------------------|
| **`POST`** | `/api/productos`               | Crea un nuevo producto.                     |
| **`GET`** | `/api/productos`               | Obtiene todos los productos.                |
| **`PUT`** | `/api/productos/{id}`          | Actualiza un producto por su ID.            |
| **`DELETE`**| `/api/productos/{id}`          | Elimina un producto por su ID.              |
| **`GET`** | `/api/ventas`                  | Obtiene el reporte de todas las ventas.     |
| **`POST`** | `/api/ventas`                  | Procesa una nueva venta (carrito de compra).|

---

### Inicio del Frontend (Página web)

El frontend son archivos HTML, CSS y JavaScript que se ejecutan directamente en el navegador.

1.  Asegúrate de que el servidor de Spring Boot esté corriendo.
2.  Navega en tu explorador de archivos a la carpeta del frontend.
3.  Abre los archivos `crear.html`, `eliminar.html`, `actualizar.html` o `reportes.html` haciendo doble clic. No es necesario usar un servidor en vivo (Live Server).
4.  El frontend se comunicará con el backend que está corriendo en el puerto 8080.
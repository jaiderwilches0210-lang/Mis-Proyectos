package com.ecohogar.controlador;

import com.ecohogar.modelo.Producto;
import com.ecohogar.repositorio.ProductoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/productos")
public class ProductoController {

    @Autowired
    private ProductoRepository productoRepository;

    @GetMapping
    public List<Producto> obtenerTodosLosProductos() {
        return productoRepository.findAll();
    }

    @PostMapping
    public ResponseEntity<Producto> crearProducto(@RequestBody Producto producto) {
        try {
            Producto nuevoProducto = productoRepository.save(producto);
            return new ResponseEntity<>(nuevoProducto, HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PutMapping("/{id}")
    public ResponseEntity<Producto> actualizarProducto(@PathVariable Long id, @RequestBody Producto producto) {
        Producto productoExistente = productoRepository.findById(id).orElse(null);
        if (productoExistente != null) {
            productoExistente.setNombre(producto.getNombre());
            productoExistente.setPrecio(producto.getPrecio());
            productoExistente.setDescripcion(producto.getDescripcion());
            productoExistente.setImagen(producto.getImagen());
            Producto productoActualizado = productoRepository.save(productoExistente);
            return new ResponseEntity<>(productoActualizado, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> eliminarProducto(@PathVariable Long id) {
        if (productoRepository.existsById(id)) {
            productoRepository.deleteById(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
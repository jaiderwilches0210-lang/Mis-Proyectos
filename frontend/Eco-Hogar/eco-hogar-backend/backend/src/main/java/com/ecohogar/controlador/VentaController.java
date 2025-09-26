package com.ecohogar.controlador;

import com.ecohogar.modelo.Venta;
import com.ecohogar.modelo.VentaProducto;
import com.ecohogar.repositorio.VentaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/ventas")
public class VentaController {

    @Autowired
    private VentaRepository ventaRepository;

    @GetMapping
    public List<Venta> obtenerTodasLasVentas() {
        return ventaRepository.findAll();
    }

    @PostMapping
    public ResponseEntity<Venta> procesarVenta(@RequestBody List<VentaProducto> carrito) {
        try {
            // Convierte la lista de productos del carrito a una lista de VentaProducto
            List<VentaProducto> productosVenta = carrito.stream()
                    .map(p -> new VentaProducto(p.getId(), p.getNombre(), p.getCantidad(), p.getPrecio()))
                    .collect(Collectors.toList());

            // Crea la venta
            Venta nuevaVenta = new Venta();
            nuevaVenta.setProductos(productosVenta);

            // Guarda la venta en la base de datos
            Venta ventaGuardada = ventaRepository.save(nuevaVenta);
            return new ResponseEntity<>(ventaGuardada, HttpStatus.CREATED);
        } catch (Exception e) {
            System.err.println("Error al procesar la venta: " + e.getMessage());
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
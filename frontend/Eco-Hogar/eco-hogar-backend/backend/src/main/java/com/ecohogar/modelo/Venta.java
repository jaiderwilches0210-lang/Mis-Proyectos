package com.ecohogar.modelo;

import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Table(name = "ventas")
public class Venta {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDateTime fechaVenta;

    @OneToMany(cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    @JoinColumn(name = "venta_id")
    private List<VentaProducto> productos;

    public Venta() {
        this.fechaVenta = LocalDateTime.now();
    }

    // Getters y Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public LocalDateTime getFechaVenta() {
        return fechaVenta;
    }

    public void setFechaVenta(LocalDateTime fechaVenta) {
        this.fechaVenta = fechaVenta;
    }

    public List<VentaProducto> getProductos() {
        return productos;
    }

    public void setProductos(List<VentaProducto> productos) {
        this.productos = productos;
    }
}
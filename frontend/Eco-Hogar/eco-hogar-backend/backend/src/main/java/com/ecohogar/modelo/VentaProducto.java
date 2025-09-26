package com.ecohogar.modelo;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "venta_productos")
public class VentaProducto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long productoId;
    private String nombre;
    private int cantidad;
    private double precio;

    // Constructores, Getters y Setters
    public VentaProducto() {}

    public VentaProducto(Long productoId, String nombre, int cantidad, double precio) {
        this.productoId = productoId;
        this.nombre = nombre;
        this.cantidad = cantidad;
        this.precio = precio;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getProductoId() {
        return productoId;
    }

    public void setProductoId(Long productoId) {
        this.productoId = productoId;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }
}
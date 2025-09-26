package tienda.accesoDatos;

public class Cliente extends Usuario {
    private String direccion;
    private String telefono;

    public Cliente(int idUsuario, String nombre, String apellido, int edad, String email, String contrasena, String direccion, String telefono) {
        super(idUsuario, nombre, apellido, edad, email, contrasena, "cliente");
        this.direccion = direccion;
        this.telefono = telefono;
    }

    // Getters y Setters
    public String getDireccion() { return direccion; }
    public void setDireccion(String direccion) { this.direccion = direccion; }
    public String getTelefono() { return telefono; }
    public void setTelefono(String telefono) { this.telefono = telefono; }
}
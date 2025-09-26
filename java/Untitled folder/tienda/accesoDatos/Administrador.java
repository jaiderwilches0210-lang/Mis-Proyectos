package tienda.accesoDatos;

public class Administrador extends Usuario {
    public Administrador(int idUsuario, String nombre, String apellido, int edad, String email, String contrasena) {
        super(idUsuario, nombre, apellido, edad, email, contrasena, "administrador");
    }
}

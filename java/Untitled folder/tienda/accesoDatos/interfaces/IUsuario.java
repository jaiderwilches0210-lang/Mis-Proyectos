package tienda.accesoDatos.interfaces;

public interface IUsuario {

    void registrar();
    boolean iniciarSesion(String email, String contrasena);
    void cerrarSesion();
   
    
}

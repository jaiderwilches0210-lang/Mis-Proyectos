package tienda.servicio;

import tienda.accesoDatos.dao.UsuarioDaoImpl;
import tienda.accesoDatos.interfaces.*;
import tienda.accesoDatos.Usuario;
import java.sql.SQLException;
import java.util.List;

public class TiendaServicio {
    private final IUsuarioDao usuarioDao;

    public TiendaServicio() {
        this.usuarioDao = new UsuarioDaoImpl();
    }

    public boolean crearUsuario(Usuario usuario) {
        try {
            usuarioDao.crearUsuario(usuario);
            return true;
        } catch (SQLException e) {
            System.err.println("Error al crear usuario: " + e.getMessage());
            return false;
        }
    }

    public Usuario iniciarSesion(String email, String contrasena) {
        try {
            Usuario usuario = usuarioDao.obtenerUsuarioPorEmail(email);
            if (usuario != null && usuario.getContrasena().equals(contrasena)) {
                return usuario;
            }
        } catch (SQLException e) {
            System.err.println("Error al iniciar sesión: " + e.getMessage());
        }
        return null;
    }

    public List<Usuario> obtenerTodosLosUsuarios() {
        try {
            return usuarioDao.obtenerTodosLosUsuarios();
        } catch (SQLException e) {
            System.err.println("Error al obtener usuarios: " + e.getMessage());
            return null;
        }
    }

    public Usuario obtenerUsuarioPorEmail(String email) {
        try {
            return usuarioDao.obtenerUsuarioPorEmail(email);
        } catch (SQLException e) {
            System.err.println("Error al buscar usuario: " + e.getMessage());
            return null;
        }
    }

    public void actualizarUsuario(Usuario usuario) {
        try {
            usuarioDao.actualizarUsuario(usuario);
        } catch (SQLException e) {
            System.err.println("Error al actualizar usuario: " + e.getMessage());
        }
    }

    public void eliminarUsuario(int idUsuario) {
        try {
            usuarioDao.eliminarUsuario(idUsuario);
        } catch (SQLException e) {
            System.err.println("Error al eliminar usuario: " + e.getMessage());
        }
    }
}

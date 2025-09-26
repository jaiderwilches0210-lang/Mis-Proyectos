package tienda.accesoDatos.dao;
import tienda.accesoDatos.interfaces.IUsuarioDao;
import tienda.accesoDatos.Administrador;
import tienda.accesoDatos.Cliente;
import tienda.accesoDatos.Usuario;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class UsuarioDaoImpl implements IUsuarioDao {

    @Override
    public void crearUsuario(Usuario usuario) throws SQLException {
        String sqlUsuario = "INSERT INTO usuario (nombre, apellido, edad, email, contrasena, rol) VALUES (?, ?, ?, ?, ?, ?)";
        String sqlCliente = "INSERT INTO cliente (idCliente, direccion, telefono) VALUES (?, ?, ?)";
        String sqlAdmin = "INSERT INTO administrador (idAdministrador) VALUES (?)";

        try (Connection conn = DB.getConnection();
             PreparedStatement stmtUsuario = conn.prepareStatement(sqlUsuario, Statement.RETURN_GENERATED_KEYS)) {

            stmtUsuario.setString(1, usuario.getNombre());
            stmtUsuario.setString(2, usuario.getApellido());
            stmtUsuario.setInt(3, usuario.getEdad());
            stmtUsuario.setString(4, usuario.getEmail());
            stmtUsuario.setString(5, usuario.getContrasena());
            stmtUsuario.setString(6, usuario.getRol());
            stmtUsuario.executeUpdate();

            try (ResultSet rs = stmtUsuario.getGeneratedKeys()) {
                if (rs.next()) {
                    usuario.setIdUsuario(rs.getInt(1));
                    if (usuario instanceof Cliente) {
                        try (PreparedStatement stmtCliente = conn.prepareStatement(sqlCliente)) {
                            stmtCliente.setInt(1, usuario.getIdUsuario());
                            stmtCliente.setString(2, ((Cliente) usuario).getDireccion());
                            stmtCliente.setString(3, ((Cliente) usuario).getTelefono());
                            stmtCliente.executeUpdate();
                        }
                    } else if (usuario instanceof Administrador) {
                        try (PreparedStatement stmtAdmin = conn.prepareStatement(sqlAdmin)) {
                            stmtAdmin.setInt(1, usuario.getIdUsuario());
                            stmtAdmin.executeUpdate();
                        }
                    }
                }
            }
        }
    }

    @Override
    public Usuario obtenerUsuarioPorEmail(String email) throws SQLException {
        String sql = "SELECT * FROM usuario WHERE email = ?";
        try (Connection conn = DB.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, email);
            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    int id = rs.getInt("idUsuario");
                    String nombre = rs.getString("nombre");
                    String apellido = rs.getString("apellido");
                    int edad = rs.getInt("edad");
                    String contrasena = rs.getString("contrasena");
                    String rol = rs.getString("rol");
                    
                    if (rol.equals("cliente")) {
                        String sqlCliente = "SELECT * FROM cliente WHERE idCliente = ?";
                        try (PreparedStatement stmtCliente = conn.prepareStatement(sqlCliente)) {
                            stmtCliente.setInt(1, id);
                            try (ResultSet rsCliente = stmtCliente.executeQuery()) {
                                if (rsCliente.next()) {
                                    return new Cliente(id, nombre, apellido, edad, email, contrasena, rsCliente.getString("direccion"), rsCliente.getString("telefono"));
                                }
                            }
                        }
                    } else if (rol.equals("administrador")) {
                        return new Administrador(id, nombre, apellido, edad, email, contrasena);
                    }
                }
            }
        }
        return null;
    }
    
    @Override
    public List<Usuario> obtenerTodosLosUsuarios() throws SQLException {
        List<Usuario> usuarios = new ArrayList<>();
        String sql = "SELECT * FROM usuario";
        try (Connection conn = DB.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                usuarios.add(obtenerUsuarioPorEmail(rs.getString("email")));
            }
        }
        return usuarios;
    }

    @Override
    public void actualizarUsuario(Usuario usuario) throws SQLException {
        String sqlUsuario = "UPDATE usuario SET nombre = ?, apellido = ?, edad = ?, contrasena = ? WHERE idUsuario = ?";
        try (Connection conn = DB.getConnection();
             PreparedStatement stmtUsuario = conn.prepareStatement(sqlUsuario)) {
            stmtUsuario.setString(1, usuario.getNombre());
            stmtUsuario.setString(2, usuario.getApellido());
            stmtUsuario.setInt(3, usuario.getEdad());
            stmtUsuario.setString(4, usuario.getContrasena());
            stmtUsuario.setInt(5, usuario.getIdUsuario());
            stmtUsuario.executeUpdate();
            
            if (usuario instanceof Cliente) {
                String sqlCliente = "UPDATE cliente SET direccion = ?, telefono = ? WHERE idCliente = ?";
                try (PreparedStatement stmtCliente = conn.prepareStatement(sqlCliente)) {
                    stmtCliente.setString(1, ((Cliente) usuario).getDireccion());
                    stmtCliente.setString(2, ((Cliente) usuario).getTelefono());
                    stmtCliente.setInt(3, usuario.getIdUsuario());
                    stmtCliente.executeUpdate();
                }
            }
        }
    }

    @Override
    public void eliminarUsuario(int idUsuario) throws SQLException {
        String sql = "DELETE FROM usuario WHERE idUsuario = ?";
        try (Connection conn = DB.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, idUsuario);
            stmt.executeUpdate();
        }
    }
}
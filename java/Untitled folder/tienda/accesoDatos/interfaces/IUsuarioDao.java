package tienda.accesoDatos.interfaces;
import tienda.accesoDatos.Usuario;
import java.sql.SQLException;
import java.util.List;

public interface IUsuarioDao {
    void crearUsuario(Usuario usuario) throws SQLException;
    Usuario obtenerUsuarioPorEmail(String email) throws SQLException;
    List<Usuario> obtenerTodosLosUsuarios() throws SQLException;
    void actualizarUsuario(Usuario usuario) throws SQLException;
    void eliminarUsuario(int idUsuario) throws SQLException;
}

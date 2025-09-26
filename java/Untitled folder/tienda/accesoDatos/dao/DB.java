package tienda.accesoDatos.dao;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class DB {
    private static final Properties props = new Properties();

    static {
        try (FileInputStream fis = new FileInputStream(".env")) {
            props.load(fis);
        } catch (IOException e) {
            System.err.println("No se pudo cargar .env, usando valores por defecto.");
        }
    }

    private DB() {}

    public static String get(String key, String def) {
        return props.getProperty(key, def);
    }

    public static Connection getConnection() throws SQLException {
        String host = get("DB_HOST", "localhost");
        String port = get("DB_PORT", "3306");
        String db   = get("DB_NAME", "tiendaEH");
        String user = get("DB_USER", "root");
        String pass = get("DB_PASS", "Jaiderylaura0210*");
        String url = "jdbc:mysql://" + host + ":" + port + "/" + db + "?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";
        return DriverManager.getConnection(url, user, pass);
    }

    public static boolean useMySql() {
        return "1".equals(get("USE_MYSQL", "0"));
    }
}

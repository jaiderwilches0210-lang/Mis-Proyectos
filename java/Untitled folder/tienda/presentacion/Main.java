package tienda.presentacion;

import tienda.accesoDatos.Administrador;
import tienda.accesoDatos.Cliente;
import tienda.accesoDatos.Usuario;
import tienda.servicio.TiendaServicio;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static final Scanner scanner = new Scanner(System.in);
    private static final TiendaServicio servicio = new TiendaServicio();
    private static Usuario usuarioLogueado = null;

    public static void main(String[] args) {
        mostrarMenuPrincipal();
    }

    private static void mostrarMenuPrincipal() {
        while (true) {
            if (usuarioLogueado == null) {
                System.out.println("\n--- Bienvenido a la Tienda Online Virtual Eco_Hogar---");
                System.out.println("1. Iniciar sesión");
                System.out.println("2. Registrarse");
                System.out.println("3. Salir");
                System.out.print("Seleccione una opción: ");
                String opcion = scanner.nextLine();
                switch (opcion) {
                    case "1":
                        iniciarSesion();
                        break;
                    case "2":
                        preguntarTipoUsuario();
                        break;
                    case "3":
                        System.out.println("¡Gracias por usar la aplicación!");
                        return;
                    default:
                        System.out.println("Opción no válida.");
                }
            } else {
                if (usuarioLogueado instanceof Cliente) {
                    menuCliente();
                } else if (usuarioLogueado instanceof Administrador) {
                    menuAdministrador();
                }
            }
        }
    }

    private static void iniciarSesion() {
        System.out.print("Ingrese su email: ");
        String email = scanner.nextLine();
        System.out.print("Ingrese su contraseña: ");
        String contrasena = scanner.nextLine();

        usuarioLogueado = servicio.iniciarSesion(email, contrasena);

        if (usuarioLogueado != null) {
            System.out.println("¡Bienvenido, " + usuarioLogueado.getNombre() + "!");
        } else {
            System.out.println("Credenciales incorrectas.");
        }
    }

    private static void preguntarTipoUsuario() {
        System.out.println("\n--- Registro de Nuevo Usuario ---");
        System.out.println("¿Qué tipo de usuario desea registrar?");
        System.out.println("1. Cliente");
        System.out.println("2. Administrador");
        System.out.print("Seleccione una opción: ");
        String tipo = scanner.nextLine();

        switch (tipo) {
            case "1":
                registrarCliente();
                break;
            case "2":
                registrarAdministrador();
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    private static void registrarCliente() {
        System.out.print("Ingrese su nombre: ");
        String nombre = scanner.nextLine();
        System.out.print("Ingrese su apellido: ");
        String apellido = scanner.nextLine();
        System.out.print("Ingrese su edad: ");
        int edad = Integer.parseInt(scanner.nextLine());
        System.out.print("Ingrese su email: ");
        String email = scanner.nextLine();
        System.out.print("Ingrese su contraseña: ");
        String contrasena = scanner.nextLine();
        System.out.print("Ingrese su dirección: ");
        String direccion = scanner.nextLine();
        System.out.print("Ingrese su teléfono: ");
        String telefono = scanner.nextLine();

        Cliente nuevoCliente = new Cliente(0, nombre, apellido, edad, email, contrasena, direccion, telefono);
        if (servicio.crearUsuario(nuevoCliente)) {
            System.out.println("¡Registro de cliente exitoso! Ya puede iniciar sesión.");
        } else {
            System.out.println("No se pudo completar el registro.");
        }
    }

    private static void registrarAdministrador() {
        System.out.print("Ingrese su nombre: ");
        String nombre = scanner.nextLine();
        System.out.print("Ingrese su apellido: ");
        String apellido = scanner.nextLine();
        System.out.print("Ingrese su edad: ");
        int edad = Integer.parseInt(scanner.nextLine());
        System.out.print("Ingrese su email: ");
        String email = scanner.nextLine();
        System.out.print("Ingrese su contraseña: ");
        String contrasena = scanner.nextLine();

        Administrador nuevoAdmin = new Administrador(0, nombre, apellido, edad, email, contrasena);
        if (servicio.crearUsuario(nuevoAdmin)) {
            System.out.println("¡Registro de administrador exitoso! Ya puede iniciar sesión.");
        } else {
            System.out.println("No se pudo completar el registro.");
        }
    }

    private static void menuCliente() {
        System.out.println("\n--- Menú de Cliente ---");
        System.out.println("1. Editar mi perfil");
        System.out.println("2. Cerrar sesión");
        System.out.print("Seleccione una opción: ");
        String opcion = scanner.nextLine();

        switch (opcion) {
            case "1":
                editarPerfilCliente();
                break;
            case "2":
                usuarioLogueado.cerrarSesion();
                usuarioLogueado = null;
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    private static void editarPerfilCliente() {
        Cliente cliente = (Cliente) servicio.obtenerUsuarioPorEmail(usuarioLogueado.getEmail());
        if (cliente == null) {
            System.out.println("Error: No se pudo cargar el perfil.");
            return;
        }
        
        System.out.println("\n--- Editar Perfil ---");
        System.out.print("Nueva dirección (" + cliente.getDireccion() + "): ");
        String nuevaDir = scanner.nextLine();
        if (!nuevaDir.isEmpty()) cliente.setDireccion(nuevaDir);
        
        System.out.print("Nuevo teléfono (" + cliente.getTelefono() + "): ");
        String nuevoTel = scanner.nextLine();
        if (!nuevoTel.isEmpty()) cliente.setTelefono(nuevoTel);
        
        System.out.print("Nueva contraseña (dejar en blanco para no cambiar): ");
        String nuevaContrasena = scanner.nextLine();
        if (!nuevaContrasena.isEmpty()) cliente.setContrasena(nuevaContrasena);
        
        servicio.actualizarUsuario(cliente);
        System.out.println("Perfil de cliente actualizado.");
    }

    private static void menuAdministrador() {
        System.out.println("\n--- Menú de Administrador ---");
        System.out.println("1. Administrar usuarios");
        System.out.println("2. Cerrar sesión");
        System.out.print("Seleccione una opción: ");
        String opcion = scanner.nextLine();

        switch (opcion) {
            case "1":
                menuAdministrarUsuarios();
                break;
            case "2":
                usuarioLogueado.cerrarSesion();
                usuarioLogueado = null;
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    private static void menuAdministrarUsuarios() {
        while (true) {
            System.out.println("\n--- Administrar Usuarios ---");
            System.out.println("1. Ver todos los usuarios");
            System.out.println("2. Actualizar un usuario");
            System.out.println("3. Eliminar un usuario");
            System.out.println("4. Volver al menú anterior");
            System.out.print("Seleccione una opción: ");
            String opcion = scanner.nextLine();

            switch (opcion) {
                case "1":
                    verUsuarios();
                    break;
                case "2":
                    actualizarUsuario();
                    break;
                case "3":
                    eliminarUsuario();
                    break;
                case "4":
                    return;
                default:
                    System.out.println("Opción no válida.");
            }
        }
    }
    
    private static void verUsuarios() {
        List<Usuario> usuarios = servicio.obtenerTodosLosUsuarios();
        if (usuarios != null && !usuarios.isEmpty()) {
            System.out.println("\n--- Lista de Usuarios ---");
            for (Usuario u : usuarios) {
                System.out.println("ID: " + u.getIdUsuario() + ", Nombre: " + u.getNombre() + " " + u.getApellido() + ", Email: " + u.getEmail() + ", Rol: " + u.getRol());
                System.out.println("-------------------------");
            }
        } else {
            System.out.println("No hay usuarios registrados.");
        }
    }
    
    private static void actualizarUsuario() {
        System.out.print("Ingrese el email del usuario a actualizar: ");
        String email = scanner.nextLine();
        Usuario usuario = servicio.obtenerUsuarioPorEmail(email);
        
        if (usuario != null) {
            System.out.println("\n--- Actualizar Usuario: " + usuario.getNombre() + " ---");
            System.out.print("Nuevo nombre (" + usuario.getNombre() + "): ");
            String nuevoNombre = scanner.nextLine();
            if (!nuevoNombre.isEmpty()) usuario.setNombre(nuevoNombre);
            
            System.out.print("Nuevo apellido (" + usuario.getApellido() + "): ");
            String nuevoApellido = scanner.nextLine();
            if (!nuevoApellido.isEmpty()) usuario.setApellido(nuevoApellido);

            System.out.print("Nueva edad (" + usuario.getEdad() + "): ");
            String edadStr = scanner.nextLine();
            if (!edadStr.isEmpty()) usuario.setEdad(Integer.parseInt(edadStr));
            
            System.out.print("Nueva contraseña (dejar en blanco para no cambiar): ");
            String nuevaContrasena = scanner.nextLine();
            if (!nuevaContrasena.isEmpty()) usuario.setContrasena(nuevaContrasena);
            
            if (usuario instanceof Cliente) {
                Cliente cliente = (Cliente) usuario;
                System.out.print("Nueva dirección (" + cliente.getDireccion() + "): ");
                String nuevaDir = scanner.nextLine();
                if (!nuevaDir.isEmpty()) cliente.setDireccion(nuevaDir);
                
                System.out.print("Nuevo teléfono (" + cliente.getTelefono() + "): ");
                String nuevoTel = scanner.nextLine();
                if (!nuevoTel.isEmpty()) cliente.setTelefono(nuevoTel);
            }
            
            servicio.actualizarUsuario(usuario);
            System.out.println("Usuario actualizado exitosamente.");
            
        } else {
            System.out.println("Usuario no encontrado.");
        }
    }
    
    private static void eliminarUsuario() {
        System.out.print("Ingrese el email del usuario a eliminar: ");
        String email = scanner.nextLine();
        Usuario usuario = servicio.obtenerUsuarioPorEmail(email);

        if (usuario != null) {
            System.out.print("¿Está seguro de que desea eliminar a " + usuario.getNombre() + " " + usuario.getApellido() + "? (s/n): ");
            String confirmacion = scanner.nextLine();
            if (confirmacion.equalsIgnoreCase("s")) {
                servicio.eliminarUsuario(usuario.getIdUsuario());
                System.out.println("Usuario eliminado exitosamente.");
            } else {
                System.out.println("Eliminación cancelada.");
            }
        } else {
            System.out.println("Usuario no encontrado.");
        }
    }
}
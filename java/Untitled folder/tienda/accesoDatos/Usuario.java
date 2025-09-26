package tienda.accesoDatos;
import  tienda.accesoDatos.interfaces.IUsuario;

public abstract class Usuario implements IUsuario {

    


    private Integer  idUsuario;
    private String nombre ; 
    private String apellido; 
    private int edad ;                                                 
    private String email;
    private String contrasena;
    private String rol;


    public Usuario(Integer  idUsuario, String nombre, String apellido, int edad, String email, String contrasena, String rol){
        this.idUsuario = idUsuario;
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad =edad;
        this.email = email;
        this.contrasena = contrasena;
        this.rol =rol;
    }

     public Usuario( String nombre, String apellido, int edad, String email, String contrasena, String rol){
      this(null, nombre, apellido, edad, email, contrasena, rol);
    }

    //GET
    public Integer getIdUsuario(){return idUsuario;}
    public String getNombre(){return nombre;}
    public String getApellido(){return apellido;}
    public int getEdad(){return edad;}
    public String getEmail(){return email;}
    public String getContrasena(){return contrasena;}
    public String getRol(){return rol;}

    //SET
     public void setIdUsuario(Integer idUsuario){this. idUsuario= idUsuario ;}
     public void setNombre(String nombre){this. nombre = nombre;}
     public void setApellido(String apellido){this.apellido = apellido;}
     public void setEdad(int edad){this.edad = edad;}
     public void setEmail(String email){this. email= email;}
     public void setContrasena(String contrasena){this. contrasena = contrasena;}
     public void setRol(String rol){this.rol = rol;}

     @Override
     public void registrar(){}
     @Override
     public boolean iniciarSesion(String email, String contrasena){return false;}
     @Override
     public void cerrarSesion(){
        System.out.println("SESION CERRADA PARA EL USUARIO: "+this.nombre);
     }
     


    
}


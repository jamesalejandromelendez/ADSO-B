/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package base_de_datos;
import java.sql.Connection;
import java.sql.DriverManager;
/**
 *
 * @author SENA
 */
public class Conectar {
    
    Connection conectar =null;
    
    public Connection conexion(){
    
        try{
            Class.forName("com.mysql.jdbc.Driver");
            
        conectar=DriverManager.getConnection("jdbc:mysql://localhost/hotel","root","");
        }catch(Exception e){
            System.out.print(e.getMessage());
        }
        return conectar;
    }
    
}

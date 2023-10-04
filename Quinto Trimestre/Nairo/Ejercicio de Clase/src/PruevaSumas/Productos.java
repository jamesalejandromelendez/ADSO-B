package PruevaSumas;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Productos {
    public static void main(String[] args){
        
    Scanner sn = new Scanner(System.in);
    boolean salir = false;
    int precio = 0;
    String producto = "";
    
    
    while(!salir){
        
        int opcion = Integer.parseInt(JOptionPane.showInputDialog("1. papas 5000 \n2. gomitas 4000 \n3. gaseosa 6000 \n4. pan 1000 \n5. jugo 2000 \n6. salir"
                +"\nEscribe una de las opciones"));
        
        switch (opcion) {
                case 1:
                    JOptionPane.showMessageDialog(null,"Has seleccionado papas por 5000");
                    producto = "papas";
                    precio = 5000;
                    break;
                case 2:
                    JOptionPane.showMessageDialog(null,"Has seleccionado gomitas por 4000");
                    producto = "gomitas";
                    precio = 4000;
                    break;
                case 3:
                    JOptionPane.showMessageDialog(null,"Has seleccionado gaseosa por 6000");
                    producto = "gaseosa";
                    precio = 6000;
                    break;
                case 4:
                    JOptionPane.showMessageDialog(null,"Has seleccionado pan por 1000");
                    producto = "pan";
                    precio = 1000;
                    break;
                case 5:
                    JOptionPane.showMessageDialog(null,"Has seleccionado jugo por 2000");
                    producto = "jugo";
                    precio = 2000;
                    break;
                case 6:
                    salir = true;
                    JOptionPane.showMessageDialog(null,"Gracias por utilizar nuestros servicios");
                    break;
                default:
                    JOptionPane.showMessageDialog(null,"Opción inválida");
                    break;
            }
        }
    }
}
    
    
    





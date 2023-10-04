package PruevaSumas;

import javax.swing.JOptionPane;

public class salario {
    public static void main(String[] args)
    {
    String nombre = JOptionPane.showInputDialog("digite su nombre ");
    String empresa = JOptionPane.showInputDialog("digite su empresa ");
    int dias = Integer.parseInt(JOptionPane.showInputDialog("cuantos dias trabajo? "));
    int salario = 3200000;
    int operacion = (3200000/30)*dias;
    
    JOptionPane.showMessageDialog(null,"su salario es "+operacion);
    } 
}


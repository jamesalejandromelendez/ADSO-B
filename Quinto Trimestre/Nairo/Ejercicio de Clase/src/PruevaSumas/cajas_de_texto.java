package PruevaSumas;

import javax.swing.JOptionPane;

public class cajas_de_texto {
    public static void main(String[] args)
    {
        System.out.println("hola esto es una prueva");
        
        JOptionPane.showMessageDialog(null,"sr usuario digite un numero");
        
        String minombre = JOptionPane.showInputDialog("digite su nombre ");
        
        int miedad = Integer.parseInt(JOptionPane.showInputDialog("digite su edad "));
        
        String micurso = JOptionPane.showInputDialog("digite su curso ");
        
        double misalario = Double.parseDouble(JOptionPane.showInputDialog("Digite su salário:"));
        
        JOptionPane.showMessageDialog(null, "su nombre es "+minombre+" su edad es "+miedad+" su curso es "+micurso+" y su salario es "+misalario);
         
    }
    
}
////////////////////////////////////////////////////////////////////////////////

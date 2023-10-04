package PruevaSumas;

import javax.swing.JOptionPane;

public class PruevaSumas {

    public static void main(String[] args) {
        String operacion = JOptionPane.showInputDialog("que operacion va a ralizar ");
        int numero1 = Integer.parseInt(JOptionPane.showInputDialog("primer numero "));
        int numero2 = Integer.parseInt(JOptionPane.showInputDialog("segundo numero "));
     
        if (operacion.equals("suma")){
            int resultado = numero1+numero2;
        JOptionPane.showMessageDialog(null,"su resultado es "+resultado);
        }
        
        if (operacion.equals("resta")){
            int resultado = numero1-numero2;
        JOptionPane.showMessageDialog(null,"su resultado es "+resultado);
        }
        
        if (operacion.equals("multiplicacion")){
            int resultado = numero1*numero2;
        JOptionPane.showMessageDialog(null,"su resultado es "+resultado);
        }
        
        if (operacion.equals("divicion")){
            int resultado = numero1/numero2;
        JOptionPane.showMessageDialog(null,"su resultado es "+resultado);
        }
        
    }
    
}
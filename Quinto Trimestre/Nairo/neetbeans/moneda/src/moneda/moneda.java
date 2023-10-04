package moneda;

import javax.swing.JOptionPane;

public class moneda {

    public static void main(String[] args) {
        double tasaCambio = 0.00027;
        double pesosColombianos = Double.parseDouble(JOptionPane.showInputDialog("Ingrese la cantidad de pesos colombianos: "));
        double dolares = pesosColombianos * tasaCambio;
        
        JOptionPane.showMessageDialog(null,pesosColombianos+" pesos colombianos son "+dolares+" dolares");
    }
}
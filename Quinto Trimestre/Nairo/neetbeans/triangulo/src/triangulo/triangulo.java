package triangulo;

import javax.swing.JOptionPane;

public class triangulo {

    public static void main(String[] args) {
        int altura = Integer.parseInt(JOptionPane.showInputDialog("digita la altura del triangulo"));
        int base = Integer.parseInt(JOptionPane.showInputDialog("digita la base del triangulo"));

        JOptionPane.showMessageDialog(null, "Su resultado es: " + base*altura/2);
    }
}


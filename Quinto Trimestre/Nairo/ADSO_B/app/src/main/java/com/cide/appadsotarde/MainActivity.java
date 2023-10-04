package com.cide.appadsotarde;

import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.renderscript.Sampler;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.function.Function;

public class MainActivity extends AppCompatActivity {
    Button btn_ir;
    EditText caja_Nombre, caja_Clave;
    Button btn_Registrarse2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        btn_ir=findViewById(R.id.btn_ir);
        btn_Registrarse2 = findViewById(R.id.btn_Registrarse2);
        caja_Clave=findViewById(R.id.caja_Clave);

        btn_ir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Toast.makeText(MainActivity.this, "Bienvenido ", Toast.LENGTH_SHORT).show();
                startActivity(new Intent(MainActivity.this, MenuPrincipal.class));

                String minombre = caja_Nombre.getText().toString();
                String miclave = caja_Clave.getText().toString();
                //Toast.makeText(MainActivity.this, "mi nombre "+minombre, Toast.LENGTH_SHORT).show();
                //Toast.makeText(MainActivity.this, "mi clave "+miclave, Toast.LENGTH_SHORT).show();

            }
        });

        btn_Registrarse2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                startActivity(new Intent(MainActivity.this, Registrarse.class));
            }
        });
    }

}

package com.cide.appadsotarde;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

public class Registrarse extends AppCompatActivity {
    ImageButton btn_Devolver2;
    Button btn_Registrarse;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registrarse);

        btn_Devolver2 = findViewById(R.id.btn_Devolver2);
        btn_Registrarse = findViewById(R.id.btn_Registrarse);

        btn_Devolver2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                startActivity(new Intent(Registrarse.this, MenuPrincipal.class));
            }
        });

        btn_Registrarse.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Toast.makeText(Registrarse.this, "Perfecto!", Toast.LENGTH_SHORT).show();
                Toast.makeText(Registrarse.this, "Ahora puedes iniciar sesion", Toast.LENGTH_SHORT).show();
                startActivity(new Intent(Registrarse.this, Login.class));
            }
        });
    }
}
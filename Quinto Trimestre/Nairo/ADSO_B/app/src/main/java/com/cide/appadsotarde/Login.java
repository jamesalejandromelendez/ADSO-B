package com.cide.appadsotarde;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;

public class Login extends AppCompatActivity {

    ImageButton btn_Devolver;
    Button Ingresar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        btn_Devolver = findViewById(R.id.btn_Devolver);
        Ingresar = findViewById(R.id.Ingresar);

        btn_Devolver.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                startActivity(new Intent(Login.this, MainActivity.class));
            }
        });

        Ingresar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Toast.makeText(Login.this, "Contraseña Incorrecta", Toast.LENGTH_SHORT).show();
                Toast.makeText(Login.this, "Intentalo infinitas veses mas", Toast.LENGTH_SHORT).show();
            }
        });

    }
}
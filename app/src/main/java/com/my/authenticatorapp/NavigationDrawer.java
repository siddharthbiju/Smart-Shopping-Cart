package com.my.authenticatorapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.drawerlayout.widget.DrawerLayout;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.MenuItem;

import android.os.Bundle;
import android.widget.Toast;

import com.google.android.material.navigation.NavigationView;

public class NavigationDrawer extends AppCompatActivity {

    DrawerLayout drawerLayout;
    ActionBarDrawerToggle actionBarDrawerToggle;
    NavigationView navigationView;


    private Toolbar toolbar;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_navigation_drawer);
        toolbar=findViewById(R.id.myToolBar);

        setSupportActionBar(toolbar);
        setUpToolbar();
        navigationView = (NavigationView) findViewById(R.id.navigation_menu);
        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
                switch (menuItem.getItemId())
                {
                    case  R.id.db:

                        Intent intent = new Intent(NavigationDrawer.this, NavigationDrawer.class);
                        startActivity(intent);
                        break;
                    case   R.id.profile:
                        Intent intent1 = new Intent(NavigationDrawer.this,MainActivity.class);
                        startActivity(intent1);
                        break;
                    case   R.id.logout:
                        Intent intent2 = new Intent(NavigationDrawer.this,Login.class);
                        startActivity(intent2);
                        Toast.makeText(NavigationDrawer.this, "Logged Out...", Toast.LENGTH_SHORT).show();
                        break;



                }
                return false;
            }
        });
    }
    public void setUpToolbar() {
        drawerLayout = findViewById(R.id.drawerLayout);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        actionBarDrawerToggle = new ActionBarDrawerToggle(this, drawerLayout, toolbar, R.string.app_name, R.string.app_name);
        drawerLayout.addDrawerListener(actionBarDrawerToggle);
        actionBarDrawerToggle.syncState();

    }
}
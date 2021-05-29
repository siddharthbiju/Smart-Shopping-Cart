package com.my.authenticatorapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.Task;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QuerySnapshot;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Toast;


import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;

public class Cart extends AppCompatActivity {
    String cid="FF 19";
    RecyclerView recyclerView;
    Adapter adapter;
    ArrayList<String> items;
    ArrayList<String> desc;
    ArrayList<String> rfid;
    FirebaseFirestore db= FirebaseFirestore.getInstance();
    FirebaseFirestore db1= FirebaseFirestore.getInstance();
    CollectionReference dbs = db.collection("Items");
    CollectionReference dbss = db1.collection("Cart/CartID/"+cid);
    SwipeRefreshLayout refreshLayout;
    int s3,total,k;
    String s1,s2,s5,s4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cart);
        items = new ArrayList<>();
        desc = new ArrayList<>();
        rfid = new ArrayList<>();
        refreshLayout = findViewById(R.id.refresh);

        recyclerView = findViewById(R.id.Recycle);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        adapter = new Adapter(this,items,desc);
        recyclerView.setAdapter(adapter);
        showData();

        refreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                rfid.clear();
                showData();
                refreshLayout.setRefreshing(false);
            }
        });

    }
    public void showData() {

        dbss.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull @NotNull Task<QuerySnapshot> task1) {
                for (DocumentSnapshot snap : task1.getResult()){
                    s4 = snap.getString("Value");
                    Log.d("output","rfid value = "+s4);
                    rfid.add(s4);
                }
            }
        }).addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull @NotNull Exception e) {
                Toast.makeText(Cart.this, "Oops ... something went wrong", Toast.LENGTH_SHORT).show();
            }
        });


        db.collection("Items").get()
                .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                    @Override
                    public void onComplete(@NonNull Task<QuerySnapshot> task) {
                        items.clear();
                        desc.clear();
                        total = 0;
                        for (k = 0 ; k < rfid.size() ; k++)
                        {
                            s4 = rfid.get(k);
                            for (DocumentSnapshot snapshot : task.getResult()) {
                                s1 = snapshot.getString("Name");
                                s2 = snapshot.getString("Price");
                                s5 = snapshot.getString("RFID value");
                                if (s4.equals(s5)){
                                    s3 = Integer.parseInt(s2);
                                    total = total + s3;
                                    items.add(s1);
                                    desc.add("Rs." + s2);
                                }

                            }
                        }
                        items.add("Total");
                        desc.add("Rs." + total);
                        adapter.notifyDataSetChanged();
                    }
                }).addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        Toast.makeText(Cart.this, "Oops ... something went wrong", Toast.LENGTH_SHORT).show();
                    }
                });
         }

    }



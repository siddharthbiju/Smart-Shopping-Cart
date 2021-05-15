package com.my.authenticatorapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import androidx.swiperefreshlayout.widget.SwipeRefreshLayout;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QuerySnapshot;

import android.os.Bundle;
import android.widget.Toast;


import java.util.ArrayList;

public class Cart extends AppCompatActivity {
    RecyclerView recyclerView;
    Adapter adapter;
    ArrayList<String> items;
    ArrayList<String> desc;
    FirebaseFirestore db= FirebaseFirestore.getInstance();
    CollectionReference dbs = db.collection("Items");
    SwipeRefreshLayout refreshLayout;
    int s3,total;
    String s1,s2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cart);
        items = new ArrayList<>();
        desc = new ArrayList<>();
        refreshLayout = findViewById(R.id.refresh);


        recyclerView = findViewById(R.id.Recycle);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        adapter = new Adapter(this,items,desc);
        recyclerView.setAdapter(adapter);
        showData();

        refreshLayout.setOnRefreshListener(new SwipeRefreshLayout.OnRefreshListener() {
            @Override
            public void onRefresh() {
                showData();
                refreshLayout.setRefreshing(false);
            }
        });

    }
    public void showData() {

        db.collection("Items").get()
                .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                    @Override
                    public void onComplete(@NonNull Task<QuerySnapshot> task1) {
                        items.clear();
                        desc.clear();
                        total = 0;
                        for (DocumentSnapshot snapshot : task1.getResult()){
                            s1 = snapshot.getString("Name");
                            s2 = snapshot.getString("Price");
                            s3=Integer.parseInt(s2);
                            total = total+s3;
                            items.add(s1);
                            desc.add("Rs."+s2);

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
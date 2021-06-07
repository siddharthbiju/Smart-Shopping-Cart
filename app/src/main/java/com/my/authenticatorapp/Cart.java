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
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;


import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;

public class Cart extends AppCompatActivity {
    String cid="cart001";
    RecyclerView recyclerView;
    Adapter adapter;
    ArrayList<String> items;
    ArrayList<String> desc;
    ArrayList<String> rfid;
    ArrayList<Integer> quantity;
    FirebaseFirestore db= FirebaseFirestore.getInstance();
    FirebaseFirestore db1= FirebaseFirestore.getInstance();
    CollectionReference dbs = db.collection("Items");
    CollectionReference dbss = db1.collection(cid+"/products/itemsCollections");
    SwipeRefreshLayout refreshLayout;
    int s3,total,k,x,z,tz;
    String s1,s2,s5,s4;
    Handler handle;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cart);
        items = new ArrayList<>();
        desc = new ArrayList<>();
        rfid = new ArrayList<>();
        quantity = new ArrayList<>();

        this.handle = new Handler();

        this.handle.postDelayed(runn,5000);

        refreshLayout = findViewById(R.id.refresh);

        recyclerView = findViewById(R.id.Recycle);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        adapter = new Adapter(this,items,desc,quantity);
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
    private final Runnable runn = new Runnable()
    {
        public void run()

        {
            showData();
            Cart.this.handle.postDelayed(runn, 5000);
        }

    };


    @Override
    protected void onPause() {
        super.onPause();
        handle.removeCallbacks(runn);
        finish();

    }
    public void next(int val){

        if(val==1){
            Intent intent11 = new Intent(Cart.this, NavigationDrawer.class);
            startActivity(intent11);
        }
    }
    public void showData() {
        rfid.clear();
        dbss.get().addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
            @Override
            public void onComplete(@NonNull @NotNull Task<QuerySnapshot> task1) {
                for (DocumentSnapshot snap : task1.getResult()){
                    s4 = snap.getString("item_name");
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
        getdata();
         }
    public void getdata(){
        db.collection("Items").get()
                .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                    @Override
                    public void onComplete(@NonNull Task<QuerySnapshot> task) {
                        items.clear();
                        desc.clear();
                        total = 0;
                        for (DocumentSnapshot snapshot : task.getResult()) {
                            s1 = snapshot.getString("Name");
                            s2 = snapshot.getString("Price");
                            s5 = snapshot.getString("RFID value");
                            Log.d("output","Item name = "+s1);
                            Log.d("output","Item rfid = "+s5);
                            for( k = 0 ; k < rfid.size() ; k++ ){
                                s4 = rfid.get(k);
                                if (s4.equals(s5)){
                                    Log.d("output","Item match rfid = "+s4);
                                    s3 = Integer.parseInt(s2);
                                    total = total + s3;
                                    items.add(s1);
                                    desc.add(s2);
                                }
                                else{Log.d("output","Item mismatch  = "+s4);continue;}
                            }

                        }
                        tz=0;
                        quantity.clear();
                        for(k = 0 ; k < items.size() ; k++){
                            z=1;
                            for(x = k+1 ; x < items.size() ; x++){
                                if(items.get(k).equals(items.get(x))){
                                    z = z+1;
                                    Log.d("output","Same");
                                    items.remove(x);
                                    desc.remove(x);
                                }
                                else{continue;}
                            }
                            quantity.add(z);
                            tz = tz + z;
                        }
                        if(k == items.size()){
                            quantity.add(tz);
                            quantity.add(0);
                        }
                        items.add("Total");
                        desc.add(String.valueOf(total));
                        Log.d("output","items:\n"+items);
                        Log.d("output","\ndesc:\n"+desc);
                        Log.d("output","\nqnt:\n"+quantity);
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



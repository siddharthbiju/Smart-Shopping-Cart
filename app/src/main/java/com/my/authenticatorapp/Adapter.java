package com.my.authenticatorapp;

import android.net.Uri;
import android.util.Log;
import android.view.LayoutInflater;
import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.network.ResumableUploadStartRequest;
import com.squareup.picasso.Picasso;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.List;

public class Adapter extends RecyclerView.Adapter<Adapter.ViewHolder> {
    private LayoutInflater layoutInflater;
    private List<String> data;
    private List<String> data2;
    private List<Integer> data3;
    private ArrayList<Integer> qty = new ArrayList<>();
    private Cart cartt;
    int j,k,q;
    private StorageReference SR = FirebaseStorage.getInstance().getReference();


    Adapter(Context context, List<String> data, List<String> data2, List<Integer> data3){
        this.layoutInflater = LayoutInflater.from(context);
        this.data = data;
        this.data2 = data2;
        this.data3 = data3;
    }



    @NonNull
    @NotNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View view = layoutInflater.inflate(R.layout.activity_product,viewGroup,false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull @NotNull Adapter.ViewHolder viewHolder, int i) {

        String title = data.get(i);
        String desc = data2.get(i);
        Integer qty = data3.get(i);
        k = Integer.parseInt(desc);
        k = k*qty;
        Log.d("output","qty = "+qty);
        Log.d("output","i = "+i);
        StorageReference itemref = SR.child("Items/"+title+".jpg");
        if(title == "Total"){
            viewHolder.textTitle.setText(title+" = Rs."+desc);
            viewHolder.textDescription.setVisibility(View.INVISIBLE);
            viewHolder.img.setVisibility(View.INVISIBLE);
            viewHolder.textdesc3.setText("x "+qty);

        }
        else {
            viewHolder.textDescription.setVisibility(View.VISIBLE);
            viewHolder.img.setVisibility(View.VISIBLE);
            viewHolder.textTitle.setText(title);
            viewHolder.textdesc3.setText("Rs."+desc);
            viewHolder.textdesc2.setText("x "+qty);
            viewHolder.textDescription.setText("Rs."+k);
            itemref.getDownloadUrl().addOnSuccessListener(new OnSuccessListener<Uri>() {
                @Override
                public void onSuccess(Uri uri1) {
                    Picasso.get().load(uri1).into(viewHolder.img);
                }
            }).addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull @NotNull Exception e) {
                    Log.d("Output","Failed to load");
                }
            });
        }
    }

    @Override
    public int getItemCount() {
        return data.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView textTitle,textDescription,textdesc2,textdesc3;
        ImageView img;
        public ViewHolder(@NonNull @NotNull View itemView) {
            super(itemView);
            textTitle = itemView.findViewById(R.id.textTitle);
            textDescription = itemView.findViewById(R.id.textDesc);
            img = itemView.findViewById(R.id.imageView);
            textdesc2 = itemView.findViewById(R.id.textDesc2);
            textdesc3 = itemView.findViewById(R.id.textDesc3);

        }
    }
}

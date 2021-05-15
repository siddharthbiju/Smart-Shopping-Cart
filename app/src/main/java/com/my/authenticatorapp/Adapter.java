package com.my.authenticatorapp;

import android.view.LayoutInflater;
import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import org.jetbrains.annotations.NotNull;

import java.util.List;

public class Adapter extends RecyclerView.Adapter<Adapter.ViewHolder> {
    private LayoutInflater layoutInflater;
    private List<String> data;
    private List<String> data2;


    Adapter(Context context, List<String> data, List<String> data2){
        this.layoutInflater = LayoutInflater.from(context);
        this.data = data;
        this.data2= data2;
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
        if(title == "Total"){
            viewHolder.textTitle.setText(title+" = "+desc);
            viewHolder.textDescription.setVisibility(View.INVISIBLE);
            viewHolder.img.setVisibility(View.INVISIBLE);
        }
        else {
            viewHolder.textDescription.setVisibility(View.VISIBLE);
            viewHolder.img.setVisibility(View.VISIBLE);
            viewHolder.textTitle.setText(title);
            viewHolder.textDescription.setText(desc);
        }
    }

    @Override
    public int getItemCount() {
        return data.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView textTitle,textDescription;
        ImageView img;
        public ViewHolder(@NonNull @NotNull View itemView) {
            super(itemView);
            textTitle = itemView.findViewById(R.id.textTitle);
            textDescription = itemView.findViewById(R.id.textDesc);
            img = itemView.findViewById(R.id.imageView);

        }
    }
}

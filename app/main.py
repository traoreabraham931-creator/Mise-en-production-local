#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 07:57:59 2026

@author: abrahamtraore
"""

import os 
from fastapi import FastAPI
import numpy as np

import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense, Input, Dropout, Attention
from tensorflow.keras.models import Model
from pydantic import BaseModel



def  model_recovery(ncols):
        # Définition du modèle
        inputs = Input(shape=(ncols,1))
        # First - layer - LSTM
        first_layer = LSTM(50, activation='relu', return_sequences=True)(inputs)
        # Second layer
        second_layer  = Dropout(0.2)(first_layer)
        # Third layer - Attention
        attention_out = Attention()([second_layer, second_layer])
        pooled = tf.keras.layers.GlobalAveragePooling1D()(attention_out)
        # Fourth layer - output layer
        outputs = Dense(1, activation='relu')(pooled)
        ml_model = Model(inputs, outputs)
        ml_model.compile(optimizer='adam', loss='mean_squared_error')  
        return ml_model
        
        
class Stockdata(BaseModel):
    
    bid: float
    ask: float
    delta: float
    gamma: float
    theta: float
    vega: float
    implied_volatility: float

    class Config:
        schema_extra = {
            "example": {
                  'bid':0.5,
                  'ask':0.1,
                  'delta':0.2,
                  'gamma':0.1,
                  'theta':0.6,
                  'vega':0.7,
                  'implied_volatility':1
                
                }
        }
        
        
app = FastAPI(
    title="Stock price prediction",
    description="Predicts the strike with respect to relevant variables",
    version="1.0.0"
)
 
# # Load the trained model
#model_path = os.path.join("/Users/abrahamtraore/Desktop/Python_upskill/Options_strike_prediction/Programmes/Fast_api/models/","custom_attention.weights.h5")

model_path = os.path.join("custom_attention.weights.h5")
ncols = 7
model = model_recovery(ncols)
model.load_weights(model_path)



@app.get("/")
def health_check():
    return {"status": "healthy", "model": "stock_prediction_v1"}


@app.post("/predict")
def predict_progression(stock: Stockdata):
    """
    Predict diabetes progression score
    """
    # Convert input to numpy array
    features = np.array([[
        stock.bid,
        stock.ask,
        stock.delta,
        stock.gamma,
        stock.theta,
        stock.vega,
        stock.implied_volatility
    ]])
    prediction = model.predict(features)#[0]
    value = prediction[0][0]
    
    return {
        "predicted_progression_score": [int(value)]
    }







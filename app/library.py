#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 07:57:59 2026

@author: abrahamtraore
"""

import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense, Input, Dropout, Attention
from tensorflow.keras.models import Model
from pydantic import BaseModel

import numpy as np


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
                  'bid':1,
                  'ask':1,
                  'delta':1,
                  'gamma':1,
                  'theta':1,
                  'vega':1,
                  'implied_volatility':1
                
                }
        }
        
        
        
  
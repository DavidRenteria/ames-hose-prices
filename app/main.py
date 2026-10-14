from fastapi import FastAPI, HTTPException 

import pandas as pd
from pathlib import Path


#Proyect root directory 
BASE_DIR = Path(__file__).resolve().parent.parent
#Dataset path
DATASET_PATH = BASE_DIR / "data" / "raw" /"ames.csv"

#Create the FastAPI app
app = FastAPI(
    title="House Price Prediction API",
    description="Machine Learning API for predicting house prices based on various features.",
    version="1.0.0"
)

@app.get("/") 
def home():
    return {
        "message": "Welcome to the House Price Prediction API!"
    }

@app.get("/eda")
def eda_info(): 
    return {
        "message": "This endpoint provides information about the Exploratory Data Analysis (EDA) performed on the dataset.",
        "dataset": "Ames Housing", 
        "analysis": "Exploratory Data Analysis (EDA)", 
        "status": "ready"
    }

@app.get("/eda/overview")
def eda_overview(): 
    #load dataset 
    df = pd.read_csv(DATASET_PATH)

    #Identify numerical and categorical features
    numerical_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    #Return dataset overview
    return {
            "n_rows": df.shape[0],
            "n_columns": df.shape[1],
            "numerical_features": list(numerical_cols), 
            "categorical_features": list(categorical_cols)        
    }

@app.get("/eda/summary")
def eda_summary(feature: str):
    #load dataset
    df = pd.read_csv(DATASET_PATH)

    #check whether the feactures exists
    if feature not in df.columns: 
        raise HTTPException(status_code=404, detail=f"Feacture '{feature}' not found")

    #check wheter the feacture is numerical 
    if not pd.api.types.is_numeric_dtype(df[feature]):
        raise HTTPException(status_code=400, detail=f"Feacture '{feature}' is not numerical")

    #calculate descriptive statistics 
    statistics = df[feature].describe()

    return {
        "feature": feature, 
        "count": int(statistics["count"]), 
        "mean": float(statistics["mean"]), 
        "std": float(statistics["std"]),
        "min": float(statistics["min"]),
        "median": float(statistics["50%"]),
        "max": float(statistics["max"]), 
    }
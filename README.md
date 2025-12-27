# Electricity Bill Prediction (TNEB Slab Based)

## Project Overview
Predict electricity unit consumption and bill amount for a household using real inputs and TNEB slab calculation.

## Features
- User inputs: People, Fans, Lights, Appliances, Usage Hours, Temperature
- Calculates Unit Consumed and Bill
- TNEB slab-based billing
- Streamlit interactive UI
- Hidden backend formulas

## Unit Calculation Formula
Unit_Consumed = (Fans*Usage_Hours*2.1) + (Lights*Usage_Hours*0.27) + (Appliances*Usage_Hours*4.5) + (People*15)

## Bill Calculation (TNEB Slab)
- 0-100 units → ₹0
- 101-200 units → ₹2.25/unit
- 201-500 units → ₹4.5/unit
- Above 500 → ₹6.5/unit

## How to Run
1. Install dependencies:
   pip install streamlit
2. Run the app:
   streamlit run app.py

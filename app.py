import streamlit as st

st.title("Electricity Bill Predictor (Slab Based) 🔌⚡")

# -----------------------------
# USER INPUTS (Visible)
# -----------------------------
people = st.number_input("People", min_value=1, step=1)
fans = st.number_input("Fans", min_value=0, step=1)
lights = st.number_input("Lights", min_value=0, step=1)
appliances = st.number_input("Appliances", min_value=0, step=1)
usage_hours = st.number_input("Usage Hours", min_value=0.0, step=0.1)
temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)

# -----------------------------
# BACKEND CALCULATIONS (Hidden)
# -----------------------------

# 1️⃣ Unit Consumed (Your Formula)
unit_consumed = (
    (fans * usage_hours * 2.1) +
    (lights * usage_hours * 0.27) +
    (appliances * usage_hours * 4.5) +
    (people * 15)
)

# 2️⃣ Usage Load (Hidden)
usage_load = usage_hours * appliances

# 3️⃣ Unit Per Person (Hidden)
unit_per_person = unit_consumed / people if people > 0 else 0

# 4️⃣ TNEB Slab Calculation
def calculate_bill(units):
    if units <= 100:
        return 0
    elif units <= 200:
        return (units - 100) * 2.25
    elif units <= 500:
        return (100 * 2.25) + ((units - 200) * 4.5)
    else:
        return (100 * 2.25) + (300 * 4.5) + ((units - 500) * 6.5)

bill_amount = calculate_bill(unit_consumed)

# -----------------------------
# OUTPUT (Visible)
# -----------------------------
if st.button("Predict Bill"):
    st.success(f"🔋 Unit Consumed: {unit_consumed:.2f} units")
    st.info(f"💰 Estimated Bill Amount: ₹ {bill_amount:.2f}")
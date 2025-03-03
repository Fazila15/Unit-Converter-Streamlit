import streamlit as st

# 🔹 Set page config at the start (Must be the first Streamlit command)
st.set_page_config(page_title="Ultra Pro Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS for Glassmorphism UI
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ff9966, #ff5e62);
        background-attachment: fixed;
        color: white;
    }
    .stApp {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    .stTextInput, .stSelectbox {
        border-radius: 10px;
        padding: 5px;
        background: rgba(255, 255, 255, 0.2);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    .stButton button {
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        border-radius: 10px;
        padding: 8px 15px;
        color: white;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.5);
    }
    </style>
""", unsafe_allow_html=True)


# Title
st.title("🔄Unit Converter 🚀")


# Sidebar for category selection
category = st.sidebar.radio("📏 Choose Conversion Type:", ["Length", "Weight", "Temperature"])

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084, "Miles": 0.000621371}
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value

# Conversion UI
if category == "Length":
    st.subheader("📏 Length Converter")
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    col1, col2, col3 = st.columns([2,1,2])
    
    from_unit = col1.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Miles"])
    swap = col2.button("🔄 Swap")
    to_unit = col3.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Miles"])
    
    if swap:
        from_unit, to_unit = to_unit, from_unit
    
    if value:
        result = convert_length(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    st.subheader("⚖️ Weight Converter")
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    col1, col2, col3 = st.columns([2,1,2])
    
    from_unit = col1.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    swap = col2.button("🔄 Swap")
    to_unit = col3.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    
    if swap:
        from_unit, to_unit = to_unit, from_unit
    
    if value:
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    value = st.number_input("Enter Value:", format="%.2f")
    col1, col2, col3 = st.columns([2,1,2])
    
    from_unit = col1.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    swap = col2.button("🔄 Swap")
    to_unit = col3.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if swap:
        from_unit, to_unit = to_unit, from_unit
    
    if value:
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"✅ {value}° {from_unit} = {result:.4f}° {to_unit}")

st.markdown("---")
st.write("💡 **Tip:** Swap units with the 🔄 button for instant conversion!")

# 🚀 Ultra Pro Unit Converter (Streamlit App)

## 🌟 Overview
The **Ultra Pro Unit Converter** is a powerful, interactive, and visually stunning web app built using **Python and Streamlit**. It allows users to convert units (length, weight, temperature, etc.) with a **modern UI**, including a **gradient background, glassmorphism effects, and animated buttons**.

## 🎨 Features
✅ **Multi-unit conversion** (Length, Weight, Temperature, etc.)  
✅ **Modern UI** with **gradient background & glassmorphism**  
✅ **Real-time unit conversion**  
✅ **Animated buttons with hover effects**  
✅ **Simple and beginner-friendly code**  

## 🛠️ Installation & Setup
### 1️⃣ **Install Python** (Skip if already installed)
Make sure Python **3.13.2** (or later) is installed. Check by running:
```bash
python --version
```
If Python is not installed, download it from [Python.org](https://www.python.org/downloads/).

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv unit_env
source unit_env/bin/activate  # For macOS/Linux
unit_env\Scripts\activate    # For Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install streamlit
```

### 4️⃣ **Run the App**
```bash
streamlit run unit-converter.py
```
This will open the app in your **web browser**.

## 📜 Code Explanation
### **1️⃣ Setting Up the Page**
```python
import streamlit as st
st.set_page_config(page_title="Ultra Pro Unit Converter", page_icon="🔄", layout="centered")
```
**Explanation:**  
🔹 `st.set_page_config(...)` sets the **page title, icon, and layout**.  
🔹 This must be **the first Streamlit command** to avoid errors.  

### **2️⃣ Styling with CSS (Glassmorphism & Gradient Background)**
```python
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
    </style>
""", unsafe_allow_html=True)
```
**Explanation:**  
🔹 Adds **gradient background** (Orange to Red) for a modern look.  
🔹 Implements **glassmorphism** (Blur & transparency effects).  
🔹 Improves **UI aesthetics** with rounded corners and shadows.  

### **3️⃣ Building the Unit Converter Logic**
```python
# Unit conversion logic
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "cm": {"m": 0.01, "inch": 0.393701},
        "m": {"cm": 100, "inch": 39.3701},
        "inch": {"cm": 2.54, "m": 0.0254}
    }
    return value * conversion_factors[from_unit][to_unit]
```
**Explanation:**  
🔹 Defines **unit conversion rules** for length.  
🔹 Uses a **dictionary-based approach** for quick conversions.  
🔹 The function takes `value`, `from_unit`, and `to_unit` as input.  

### **4️⃣ Creating the Streamlit UI**
```python
st.title("🔄 Ultra Pro Unit Converter 🚀")

value = st.number_input("Enter Value:")
from_unit = st.selectbox("From Unit", ["cm", "m", "inch"])
to_unit = st.selectbox("To Unit", ["cm", "m", "inch"])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result} {to_unit}")
```
**Explanation:**  
🔹 `st.title(...)` adds the **app title with an emoji**.  
🔹 `st.number_input(...)` allows users to **enter a value**.  
🔹 `st.selectbox(...)` lets users **choose units**.  
🔹 `st.button(...)` triggers the **conversion function** and displays the result.  

## 🎯 Next Steps (Enhancements)
🔹 **Add more units** (Weight, Temperature, Speed, etc.)  
🔹 **Enhance UI further** with animations and themes.  
🔹 **Deploy online** using **Streamlit Cloud** or **Vercel**.  

## 👨‍💻 Author
Developed by **Fazila Malik** 💙  

## 📜 License
This project is licensed under the **MIT License**.


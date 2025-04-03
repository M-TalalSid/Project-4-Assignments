import streamlit as st
import plotly.graph_objects as go

# Custom CSS with responsive design and animations
st.markdown(
    """
    <style>
    .title {
        color: #4CAF50;
        text-align: center;
        font-size: clamp(36px, 5vw, 48px);
        font-weight: bold;
        margin-bottom: 20px;
        animation: fadeIn 1s ease-in;
    }
    .result {
        font-size: clamp(20px, 3vw, 24px);
        text-align: center;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        transition: all 0.5s ease;
    }
    .underweight { color: #2196F3; background-color: #E3F2FD; }
    .normal { color: #4CAF50; background-color: #E8F5E9; }
    .overweight { color: #FF9800; background-color: #FFF3E0; }
    .obese { color: #F44336; background-color: #FFEBEE; }
    .stSlider > div > div > div > div {
        background-color: #4CAF50;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    @media (max-width: 600px) {
        .stColumn { margin-bottom: 10px; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<h1 class="title">Simple BMI Calculator</h1>', unsafe_allow_html=True)

# Unit selection
unit = st.selectbox("Units", ["Metric (cm/kg)", "Imperial (ft/lbs)"])

# Input section with responsive columns
col1, col2 = st.columns(2)
with col1:
    if unit == "Metric (cm/kg)":
        height = st.slider("Height (cm)", 100, 250, 170)
    else:
        height_ft = st.slider("Height (ft)", 3, 8, 5)
        height_in = st.slider("Height (in)", 0, 11, 6)
        height = (height_ft * 30.48) + (height_in * 2.54)  # Convert to cm
with col2:
    if unit == "Metric (cm/kg)":
        weight = st.slider("Weight (kg)", 30, 150, 70)
    else:
        weight_lb = st.slider("Weight (lbs)", 60, 330, 150)
        weight = weight_lb * 0.453592  # Convert to kg

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Determine category and styling
if bmi < 18.5:
    category = "Underweight"
    style = "underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
    style = "normal"
elif 25 <= bmi < 30:
    category = "Overweight"
    style = "overweight"
else:
    category = "Obese"
    style = "obese"

# Display result and gauge
if st.button("Calculate BMI", use_container_width=True):
    # Text result with animation
    st.markdown(
        f'<div class="result {style}">BMI: {bmi:.1f} - {category}</div>',
        unsafe_allow_html=True
    )
    
    # BMI Gauge using Plotly
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=bmi,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 40], 'tickwidth': 1, 'tickcolor': "black"},
            'bar': {'color': "#4CAF50"},
            'steps': [
                {'range': [0, 18.5], 'color': "#E3F2FD"},
                {'range': [18.5, 25], 'color': "#E8F5E9"},
                {'range': [25, 30], 'color': "#FFF3E0"},
                {'range': [30, 40], 'color': "#FFEBEE"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': bmi
            }
        }
    ))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# Info section
with st.expander("BMI Categories"):
    st.write("• Underweight: < 18.5")
    st.write("• Normal: 18.5 - 24.9")
    st.write("• Overweight: 25 - 29.9")
    st.write("• Obese: ≥ 30")
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="線性回歸動態操作台", layout="centered")

st.title("動態線性回歸參數調整")
st.markdown("""
這個應用程式可以讓你動態調整線性回歸的參數 ($m$ 和 $b$)，並觀察隨機生成的資料分布。
""")

# Create placeholder for the plot and equation so they appear above the sliders
plot_placeholder = st.container()

st.divider()

# Parameters at the bottom
st.subheader("參數調整")
col1, col2, col3 = st.columns(3)
with col1:
    m_val = st.slider("斜率 (m)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
with col2:
    b_val = st.slider("截距 (b)", min_value=-50.0, max_value=50.0, value=0.0, step=1.0)
with col3:
    noise_val = st.slider("隨機分布大小 (Noise)", min_value=0.0, max_value=20.0, value=5.0, step=0.5)

num_points = 100

# Generate random data
np.random.seed(42)  # For reproducibility of the underlying noise pattern if desired, 
                   # but here we generate new points based on the sliders.
x = np.linspace(0, 10, num_points)
noise = np.random.normal(0, noise_val, num_points)
y_data = m_val * x + b_val + noise

# Regression line (using the current slider values)
y_line = m_val * x + b_val

# Visualization
fig, ax = plt.subplots(figsize=(6, 4)) # Reduced figure size

# Plot data points
ax.scatter(x, y_data, color='blue', alpha=0.5, label='Random Data Points')

# Plot regression line
ax.plot(x, y_line, color='red', linewidth=2, label=f'Regression Line: $y = {m_val:.1f}x + {b_val:.1f}$')

# Formatting
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Linear Regression Visualization")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)

# Display plot and text in the placeholder
with plot_placeholder:
    st.pyplot(fig)
    st.subheader("目前方程式")
    st.latex(rf"y = {m_val:.1f}x + {b_val:.1f}")
    st.info(f"生成的資料點數量: {num_points}")

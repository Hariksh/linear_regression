import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Custom CSS (clean + minimal)
# ---------------------------
st.markdown("""
<style>
/* App background */
.stApp {
    background: #0f172a;
    color: #e2e8f0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #020617;
}

/* Titles */
h1 {
    color: #38bdf8;
    text-align: center;
    font-weight: 600;
}

/* Card container */
.block-container {
    padding: 2rem;
}

/* Metric card */
.metric-card {
    background: #020617;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #1e293b;
}

/* Text */
p {
    font-size: 15px;
}

/* Slider label */
.stSlider label {
    color: #38bdf8 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Data
# ---------------------------
np.random.seed(42)
X = np.linspace(0, 10, 50)
true_m, true_b = 2, 1
noise = np.random.randn(50)
y = true_m * X + true_b + noise

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.header("Controls")

m = st.sidebar.slider("Slope (m)", -5.0, 5.0, 1.0)
b = st.sidebar.slider("Intercept (b)", -5.0, 5.0, 0.0)

# ---------------------------
# Prediction + MSE
# ---------------------------
y_pred = m * X + b
mse = np.mean((y - y_pred) ** 2)

# ---------------------------
# Plot
# ---------------------------
fig, ax = plt.subplots()

ax.scatter(X, y, label="Data")
ax.plot(X, y_pred, color="red", label="Line")

for i in range(len(X)):
    ax.plot([X[i], X[i]], [y[i], y_pred[i]], linestyle="dashed")

ax.legend()
ax.set_title(f"MSE: {mse:.2f}")

# ---------------------------
# Layout
# ---------------------------
st.title("Linear Regression Visualizer")

col1, col2 = st.columns([3, 1])

with col1:
    st.pyplot(fig)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>Metrics</h3>
        <p><b>MSE:</b> {mse:.2f}</p>
        <p><b>Slope:</b> {m}</p>
        <p><b>Intercept:</b> {b}</p>
    </div>
    """, unsafe_allow_html=True)

st.subheader("What to observe")
st.write("- Adjust slope and intercept")
st.write("- Observe how MSE changes")
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.linspace(0, 10, 50)
true_m, true_b = 2, 1
noise = np.random.randn(50)
y = true_m * X + true_b + noise

st.sidebar.header("Controls")

m = st.sidebar.slider("Slope (m)", -5.0, 5.0, 1.0)
b = st.sidebar.slider("Intercept (b)", -5.0, 5.0, 0.0)

y_pred = m * X + b
mse = np.mean((y - y_pred) ** 2)

fig, ax = plt.subplots()

ax.scatter(X, y, label="Data")
ax.plot(X, y_pred, color="red", label="Line")

for i in range(len(X)):
    ax.plot([X[i], X[i]], [y[i], y_pred[i]], linestyle="dashed")

ax.legend()
ax.set_title(f"MSE: {mse:.2f}")

st.pyplot(fig)

st.write("### 🔍 What to observe:")
st.write("- Adjust slope & intercept")
st.write("- Watch how error (MSE) changes")
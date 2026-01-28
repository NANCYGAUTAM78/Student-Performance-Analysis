import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ---------------- Load Data ----------------
df = pd.read_csv("student_performance.csv")

# Fix typo in CSV column
df.rename(columns={"ender": "gender"}, inplace=True)

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# ---------------- Sidebar ----------------
st.sidebar.title("🎛 Filters")

gender_filter = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + df["gender"].unique().tolist()
)

if gender_filter != "All":
    df = df[df["gender"] == gender_filter]

show_data = st.sidebar.checkbox("Show Raw Dataset")

# ---------------- Main Header ----------------
st.markdown(
    "<h1 style='text-align:center;'>🎓 Student Performance Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:gray;'>Interactive analysis of student scores</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- KPI Cards ----------------
col1, col2, col3 = st.columns(3)

col1.metric("📐 Avg Math Score", round(df["math_score"].mean(), 2))
col2.metric("📖 Avg Reading Score", round(df["reading_score"].mean(), 2))
col3.metric("✍ Avg Writing Score", round(df["writing_score"].mean(), 2))

st.markdown("---")

# ---------------- Charts ----------------
left, right = st.columns(2)

with left:
    st.subheader("👩‍🎓 Gender Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(x="gender", data=df, ax=ax1)
    st.pyplot(fig1)

with right:
    st.subheader("📊 Score Distribution")
    subject = st.selectbox(
        "Choose Subject",
        ["math_score", "reading_score", "writing_score"]
    )

    fig2, ax2 = plt.subplots()
    sns.histplot(df[subject], kde=True, ax=ax2)
    st.pyplot(fig2)

# ---------------- Raw Data ----------------
if show_data:
    st.markdown("### 📄 Raw Dataset")
    st.dataframe(df)

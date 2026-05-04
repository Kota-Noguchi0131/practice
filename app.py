import streamlit as st

st.title("食事カロリー管理アプリ")

target = st.number_input("今日の目標カロリー", value=1600)

food = st.text_input("食べたもの")
calorie = st.number_input("カロリー", min_value=0)

if "meals" not in st.session_state:
    st.session_state.meals = []

if st.button("追加"):
    st.session_state.meals.append((food, calorie))

total = sum(c for _, c in st.session_state.meals)

st.write("合計:", total, "kcal")
st.write("残り:", target - total, "kcal")
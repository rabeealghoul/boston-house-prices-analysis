import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. إعداد صفحة الويب
st.set_page_config(page_title="House Price Predictor", page_icon="🏠")
st.title("🏠 Boston House Price Predictor")
st.write("Enter the number of rooms to predict the house price.")

# 2. تحميل البيانات وتدريب الموديل (عشان الواجهة تكون جاهزة)
@st.cache_data # دي بتخلي البرنامج ميحملش الداتا كل مرة
def load_data():
    # نفس الخطوات اللي عملناها في main.py
    columns_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    df = pd.read_csv('housing.csv', sep=r'\s+', names=columns_names)
    return df

df = load_data()

# تدريب الموديل
X = df[['RM']]
y = df['MEDV']
model = LinearRegression()
model.fit(X, y)

# 3. واجهة المستخدم (Form)
rooms = st.number_input("Number of Rooms (RM):", min_value=1.0, max_value=10.0, value=6.0, step=0.1)

# 4. زر التوقع
if st.button("Predict Price"):
    # عمل التوقع
    prediction = model.predict([[rooms]])[0]
    st.success(f"The predicted house price is: **${prediction * 1000:,.0f}**")
    st.balloons() # حركة احتفالية
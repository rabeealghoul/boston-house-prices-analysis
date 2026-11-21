import pandas as pd

# قائمة بأسماء الأعمدة
columns_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# قراءة الملف مع تسمية الأعمدة
df = pd.read_csv('housing.csv', sep=r'\s+', names=columns_names)

# طباعة أول 5 صفوف
print("--- أول 5 صفوف ---")
print(df.head())

# طباعة معلومات عن الأعمدة
print("\n--- معلومات عن الأعمدة ---")
print(df.info())
# طباعة أسماء الأعمدة
print("\n--- أسماء الأعمدة ---")
print(df.columns)

# طباعة إحصائيات سريعة (المتوسط، الحد الأدنى، الأقصى)
print("\n--- إحصائيات ---")
print(df.describe())
import matplotlib.pyplot as plt
import seaborn as sns

# رسم بياني يوضح العلاقة بين عدد الغرف (RM) وسعر المنزل (MEDV)
plt.figure(figsize=(10, 6))
sns.regplot(x='RM', y='MEDV', data=df, color='blue', line_kws={"color": "red"})

# إضافة عناوين
plt.title('Relationship between Rooms (RM) and House Price (MEDV)')
plt.xlabel('Average Number of Rooms')
plt.ylabel('Median House Value (in $1000s)')
plt.savefig('rooms_vs_price.png')
# إظهار الرسم البياني
plt.show()
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. تجهيز البيانات (سعر البيت مربوط بعدد الغرف)
X = df[['RM']]  # المدخلات (عدد الغرف) - لازم تكون مصفوفة 2D
y = df['MEDV']  # المخرجات (السعر)

# 2. بناء الموديل وتدريبه
model = LinearRegression()
model.fit(X, y)

# 3. تجربة التوقع لبيت فيه 6 غرف
rooms_new = np.array([[6]])
predicted_price = model.predict(rooms_new)

print(f"\n--- التوقع ---")
print(f"سعر بيت فيه 6 غرف تقريباً: {predicted_price[0]:.2f} ألف دولار")
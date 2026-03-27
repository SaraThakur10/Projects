import pandas as pd
from database import create_connection
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = None


def train_model():
    global model

    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()

    if df.empty:
        print("⚠️ No data available for training ML model.")
        return

    # Create Result Column
    df['result'] = df.apply(
        lambda row: 1 if row['marks'] > 40 and row['attendance'] > 70 else 0,
        axis=1
    )

    X = df[['marks', 'attendance']]
    y = df['result']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"📊 Model trained with accuracy: {acc * 100:.2f}%")


def predict_result(marks, attendance):
    global model

    if model is None:
        print("⚠️ Train the model first!")
        return

    prediction = model.predict([[marks, attendance]])

    if prediction[0] == 1:
        print("🎉 Prediction: PASS")
    else:
        print("❌ Prediction: FAIL")
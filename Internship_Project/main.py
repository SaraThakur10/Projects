from database import create_table
from crud import add_student, view_students, update_student, delete_student
from ml_model import train_model, predict_result


def demo():
    create_table()

    # Add students
    add_student("Alice", 19, 85, 90)
    add_student("Bob", 20, 35, 60)
    add_student("Charlie", 21, 50, 75)

    print("\n📋 All Students:")
    view_students()

    # Update
    update_student(2, marks=45, attendance=80)

    print("\n📋 After Update:")
    view_students()

    # Train ML Model
    train_model()

    # Prediction
    print("\n🔮 Prediction Test:")
    predict_result(50, 85)

    # Delete
    delete_student(3)

    print("\n📋 Final Data:")
    view_students()


if __name__ == "__main__":
    demo()
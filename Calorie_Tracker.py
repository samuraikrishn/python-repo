# MYSQL DATABASE INFO

# -- Step 1: Create the database
# CREATE DATABASE IF NOT EXISTS calorie_tracker;
# USE calorie_tracker;

# -- Step 2: Users table
# CREATE TABLE users (
#     user_id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(50) NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     age INT,
#     gender ENUM('male', 'female', 'other'),
#     height_cm FLOAT,
#     weight_kg FLOAT,
#     goal_calories INT DEFAULT 2000,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# -- Step 3: Foods table
# CREATE TABLE foods (
#     food_id INT AUTO_INCREMENT PRIMARY KEY,
#     food_name VARCHAR(100) NOT NULL,
#     calories FLOAT NOT NULL,
#     protein FLOAT DEFAULT 0,
#     carbs FLOAT DEFAULT 0,
#     fat FLOAT DEFAULT 0,
#     serving_size VARCHAR(50) DEFAULT '100g'
# );

# -- Step 4: Meals table
# CREATE TABLE meals (
#     meal_id INT AUTO_INCREMENT PRIMARY KEY,
#     user_id INT NOT NULL,
#     food_id INT NOT NULL,
#     quantity FLOAT DEFAULT 1,
#     date_logged DATE DEFAULT (CURRENT_DATE),
#     time_logged TIME DEFAULT (CURRENT_TIME),
#     FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
#     FOREIGN KEY (food_id) REFERENCES foods(food_id) ON DELETE CASCADE
# );


# -- Step 5: Daily summary table
# CREATE TABLE daily_summary (
#     summary_id INT AUTO_INCREMENT PRIMARY KEY,
#     user_id INT NOT NULL,
#     date DATE NOT NULL,
#     total_calories FLOAT DEFAULT 0,
#     total_burned FLOAT DEFAULT 0,
#     net_calories FLOAT GENERATED ALWAYS AS (total_calories - total_burned) STORED,
#     FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
#     UNIQUE (user_id, date)
# );

import mysql.connector
from datetime import date
import time

# ---------- CONNECT TO DATABASE ----------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Samurai@200723",
        database="calorie_tracker"
    )
    cur = conn.cursor()
    print("✅ Connected to MySQL successfully.\n")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
    exit()

# ---------- FUNCTIONS ----------

def add_user():
    """Add a new user"""
    try:
        name = input("Enter username: ").strip()
        email = input("Enter email: ").strip()
        pw = input("Enter password: ").strip()
        age = int(input("Enter age: ").strip())
        gender = input("Enter gender (M/F/O): ").strip().upper()
        if gender == "M":
            gender = "male"
        elif gender == "F":
            gender = "female"
        else:
            gender = "other"
        height = float(input("Enter height (cm): ").strip())
        weight = float(input("Enter weight (kg): ").strip())

        cur.execute("""
            INSERT INTO users (username, email, password, age, gender, height_cm, weight_kg)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (name, email, pw, age, gender, height, weight))
        conn.commit()
        print("✅ User added successfully!\n")
    except Exception as e:
        print(f"❌ Error adding user: {e}\n")


def display_users():
    """Display all users"""
    try:
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        if not rows:
            print("No users found.\n")
            return
        print("\n👤 USERS")
        print("-" * 70)
        for r in rows:
            print(f"ID: {r[0]} | Name: {r[1]} | Email: {r[2]} | Age: {r[4]} | Gender: {r[5]} | Height: {r[6]} cm | Weight: {r[7]} kg")
        print("-" * 70 + "\n")
    except Exception as e:
        print(f"❌ Error displaying users: {e}\n")


def add_food():
    """Add a food item"""
    try:
        name = input("Enter food name: ").strip()
        cal = float(input("Enter calories per serving: ").strip())
        cur.execute("INSERT INTO foods (food_name, calories) VALUES (%s,%s)", (name, cal))
        conn.commit()
        print("✅ Food added successfully!\n")
    except Exception as e:
        print(f"❌ Error adding food: {e}\n")


def display_food():
    """Display all foods"""
    try:
        cur.execute("SELECT * FROM foods")
        rows = cur.fetchall()
        if not rows:
            print("No food items found.\n")
            return
        print("\n🍎 FOOD ITEMS")
        print("-" * 50)
        for r in rows:
            print(f"ID: {r[0]} | Name: {r[1]} | Calories: {r[2]} kcal")
        print("-" * 50 + "\n")
    except Exception as e:
        print(f"❌ Error displaying foods: {e}\n")


def log_meal():
    """Log a meal for a user"""
    try:
        user_id = int(input("Enter User ID: ").strip())
        food_id = int(input("Enter Food ID: ").strip())
        qty = float(input("Enter quantity (servings): ").strip())
        cur.execute("INSERT INTO meals (user_id, food_id, quantity) VALUES (%s,%s,%s)", (user_id, food_id, qty))
        conn.commit()
        print("✅ Meal logged successfully!\n")
    except Exception as e:
        print(f"❌ Error logging meal: {e}\n")


def display_meals():
    """Display all logged meals"""
    try:
        cur.execute("""
            SELECT m.meal_id, u.username, f.food_name, m.quantity, m.date_logged
            FROM meals m
            JOIN users u ON m.user_id = u.user_id
            JOIN foods f ON m.food_id = f.food_id
        """)
        rows = cur.fetchall()
        if not rows:
            print("No meal logs found.\n")
            return
        print("\n🍽️ MEAL LOGS")
        print("-" * 90)
        for r in rows:
            print(f"Meal ID: {r[0]} | User: {r[1]} | Food: {r[2]} | Qty: {r[3]} | Date: {r[4]}")
        print("-" * 90 + "\n")
    except Exception as e:
        print(f"❌ Error displaying meals: {e}\n")


def view_daily_calories():
    """View today's total calories for a user"""
    try:
        user_id = int(input("Enter User ID: ").strip())
        cur.execute("""
            SELECT SUM(f.calories * m.quantity)
            FROM meals m
            JOIN foods f ON m.food_id = f.food_id
            WHERE m.user_id = %s AND m.date_logged = %s
        """, (user_id, date.today()))
        total = cur.fetchone()[0] or 0
        print(f"🔥 Total calories consumed today: {total:.2f} kcal\n")
    except Exception as e:
        print(f"❌ Error calculating calories: {e}\n")


def summary():
    """Show total users, foods, and meals"""
    try:
        cur.execute("SELECT COUNT(*) FROM users")
        users = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM foods")
        foods = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM meals")
        meals = cur.fetchone()[0]
        print("\n📊 SYSTEM SUMMARY")
        print("-" * 40)
        print(f"👤 Users Registered: {users}")
        print(f"🍎 Foods Available: {foods}")
        print(f"🍽️ Meals Logged: {meals}")
        print("-" * 40 + "\n")
    except Exception as e:
        print(f"❌ Error showing summary: {e}\n")

# ---------- CLI MENU ----------
while True:
    print("========== CALORIE TRACKER ==========")
    print("1. Add User")
    print("2. Display Users")
    print("3. Add Food")
    print("4. Display Foods")
    print("5. Log Meal")
    print("6. Display Meals")
    print("7. View Today's Calories")
    print("8. Summary (All Stats)")
    print("9. Exit")
    choice = input("Choose an option (1–9): ").strip()

    if choice == "1": add_user()
    elif choice == "2": display_users()
    elif choice == "3": add_food()
    elif choice == "4": display_food()
    elif choice == "5": log_meal()
    elif choice == "6": display_meals()
    elif choice == "7": view_daily_calories()
    elif choice == "8": summary()
    elif choice == "9":
        print("Exiting program...")
        time.sleep(1)
        print("✅ All data saved. Goodbye! ❤️")
        break
    else:
        print("❌ Invalid choice. Please try again.\n")

cur.close()
conn.close()

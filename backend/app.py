from flask import Flask, request, jsonify
from database import create_connection, create_table
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -------------------
# USERS
# -------------------
users = {
    "S001": {"pin": "1234", "role": "staff"},
    "M001": {"pin": "9999", "role": "manager"}
}

# -------------------
# ROUTES
# -------------------

@app.route("/")
def home():
    return "RMS is running 🚀"

# LOGIN API
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user_id = data.get("id")
    pin = data.get("pin")

    # check user exists
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    # check pin
    if users[user_id]["pin"] != pin:
        return jsonify({"message": "Wrong PIN"}), 400

    return jsonify({
        "message": "Login success",
        "role": users[user_id]["role"]
    })

@app.route("/add-sale", methods=["POST"])
def add_sale():
    data = request.json

    cash = data.get("cash", 0)
    card = data.get("card", 0)
    uber = data.get("uber", 0)
    date = data.get("date")
    staff_id = data.get("staff_id")

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sales (cash, card, uber, date, staff_id)
        VALUES (?, ?, ?, ?, ?)
    """, (cash, card, uber, date, staff_id))

    conn.commit()
    conn.close()

    return jsonify({"message": "Sale saved"})

@app.route("/sales",methods=["GET"])
def get_sales():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append(dict(row))

    conn.close()
    return jsonify(result)


# -------------------
# RUN SERVER (ONLY ONCE, LAST)
# -------------------
if __name__ == "__main__":
    create_table()
    app.run(debug=True)

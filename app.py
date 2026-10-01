from flask import Flask, render_template, request, redirect, url_for, session
import pickle

app = Flask(__name__)
app.secret_key = "abcdefgh123456789"

users = {}


import pickle

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("SVM_model1.pkl", "rb") as f:
    model = pickle.load(f)

def check_password(stored_password, provided_password):
    return stored_password == provided_password

@app.route("/")
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        # Save user data (In real apps, use a database)
        if email in users:
            return redirect(url_for('register'))
        users[email] = {'username': username, 'password': password}
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login_post():
    email = request.form["email"]
    password = request.form["password"]
    if email in users and check_password(users[email]['password'], password):
        session['email'] = email
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route("/home")
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template("home.html")

@app.route("/input", methods=["GET", "POST"])
def input():
    if "email" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        try:
            data = [[
                float(request.form["radius"]),
                float(request.form["texture_mean"]),
                float(request.form["perimeter_mean"]),
                float(request.form["area_mean"]),
                float(request.form["smoothness_mean"]),
                float(request.form["concavity_mean"]),
                float(request.form["concave_points_mean"]),
                float(request.form["symmetry_mean"]),
                float(request.form["fractal_dimension_mean"])
            ]]

            # Apply the same scaling used during training
            data_scaled = scaler.transform(data)

            # Predict
            prediction = model.predict(data_scaled)[0]

            # Optional probability (works only if probability=True during training)
            confidence = None
            if hasattr(model, "predict_proba"):
                confidence = round(
                    max(model.predict_proba(data_scaled)[0]) * 100,
                    2
                )

            # Label mapping
            result = "Benign (B)" if prediction == 0 else "Malignant (M)"

            print("Input :", data)
            print("Scaled:", data_scaled)
            print("Prediction:", prediction)
            print("Result:", result)

            return render_template(
                "result.html",
                result=result,
                data=int(prediction),
                confidence=confidence
            )

        except Exception as e:
            return f"Prediction Error: {e}"

    return render_template("input.html")

# Performance page route
@app.route("/performance")
def performance():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    # Assuming you have metrics available
    metrics = {
        'accuracy': 98.2,
        'precision': 100,
        'recall': 95.3,
        'f1_score': 97.6
    }
    return render_template("performance.html", metrics=metrics)

# Charts page route
@app.route("/charts")
def charts():
    if 'email' not in session:
        return redirect(url_for('login'))
    
    return render_template("charts.html")

if __name__ == '__main__':
    app.run(debug=True)

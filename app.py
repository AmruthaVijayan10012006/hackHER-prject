from flask import Flask, render_template, request
from original import DiabeticPatient, Food, recommend_food

app = Flask(__name__)

# Route for Welcome Page
@app.route('/')
def welcome():
    return render_template('welcome1.html')

# Route for "Know More About Us" Page
@app.route('/about')
def about():
    return render_template('f.html')

# Route for Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Dummy authentication (Replace with actual user validation)
        if email == "test@example.com" and password == "password123":
            return render_template('drashb.html')  # Redirect to dashboard on success
        else:
            return render_template('login1.html', error="Invalid credentials, try again.")

    return render_template('login1.html')

# Route for Signup Page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Route for Dashboard Page (handles form submission)
@app.route('/drashb', methods=['GET', 'POST'])
def drashb():
    if request.method == 'POST':
        age = request.form.get('age')
        gender = request.form.get('gender')
        insulin_sensitivity = request.form.get('insulin_sensitivity')
        food_name = request.form.get('food_check')

        if not age or not gender or not insulin_sensitivity or not food_name:
            return "Error: Missing form fields", 400  # Handle missing input error

        try:
            age = int(age)
            insulin_sensitivity = float(insulin_sensitivity)
            food_name = food_name.lower()
        except ValueError:
            return "Error: Invalid input format", 400  # Handle incorrect input formats

        # Create patient object
        patient = DiabeticPatient(age, gender, insulin_sensitivity)

        # Food database
        foods = {
            "apple": Food('Apple', 20, 38),
            "banana": Food('Banana', 25, 42),
            "pizza": Food('Pizza', 30, 60),
            "bread": Food('Bread', 40, 70),
            "rice": Food('Rice', 50, 80),
            "oatmeal": Food('Oatmeal', 30, 42),
            "mango": Food('Mango', 25, 51),
            "watermelon": Food('Watermelon', 10, 72),
            "pineapple": Food('Pineapple', 20, 59),
        }

        # Check if food exists
        if food_name in foods:
            food = foods[food_name]
            result = recommend_food(patient, food)
        else:
            result = "Food not found in database. Please try again."

        return result  # Send result text directly (JS will display it)

    return render_template('drashb.html')

if __name__ == '__main__':
    app.run(debug=True)

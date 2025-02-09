# Diabetic-Friendly Food Recommendation System

## Overview
This project is a web-based application that helps diabetic patients determine the impact of various foods on their blood sugar levels. It calculates the Blood Sugar Impact (BSI) based on user inputs like age, gender, and insulin sensitivity, and provides recommendations on whether a specific food is safe to consume.

## Features
- User authentication (login and signup)
- Food recommendation based on BSI calculation
- A database of food items with their carbohydrate content and glycemic index values
- Interactive user interface built with Flask

## Technologies Used
- Python
- Flask
- HTML & CSS (for rendering templates)

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask

### Steps to Run the Application
1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```sh
   pip install flask
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open a web browser and go to `http://127.0.0.1:5000/` to access the application.

## File Structure
- `app.py` - Main Flask application
- `original.py` - Contains logic for BSI calculation and food recommendations
- `templates/` - HTML templates for different pages
- `static/` - CSS and JS files

## Usage
1. Open the application in a browser.
2. Login or sign up.
3. Enter personal details like age, gender, and insulin sensitivity.
4. Input a food name to check its impact.
5. Get recommendations on whether the food is safe, moderate, or dangerous for consumption.

## Future Enhancements
- Store user data and preferences in a database
- Improve UI with better styling and animations
- Add more food items with comprehensive nutritional data
- Implement a personalized diet plan feature

## Contributors
- Developer: [Amrutha Vijayan,Khadeeja Hannath V U,Krishnapriya S ]

## License
This project is licensed under the MIT License.


#Here's an updated version of the program that includes an input menu instead of a choice-based menu:


class DiabeticPatient:
    def __init__(self, age, gender, insulin_sensitivity):
        self.age = age
        self.gender = gender
        self.insulin_sensitivity = insulin_sensitivity

class Food:
    def __init__(self, name, carb_content, gi_value):
        self.name = name
        self.carb_content = carb_content
        self.gi_value = gi_value

def calculate_bsi(patient, food):
    # Calculate Glycemic Load (GL)
    gl = food.carb_content * food.gi_value
    
    # Adjust for insulin sensitivity
    gl_adjusted = gl / patient.insulin_sensitivity
    
    # Adjust for age
    if patient.age < 18:
        gl_adjusted *= 1.1  # increase GL for children and adolescents
    elif patient.age > 65:
        gl_adjusted *= 0.9  # decrease GL for older adults
    
    # Adjust for gender
    if patient.gender.lower() == 'male':
        gl_adjusted *= 1.05  # increase GL for males
    elif patient.gender.lower() == 'female':
        gl_adjusted *= 0.95  # decrease GL for females
    
    # Calculate Blood Sugar Impact (BSI)
    bsi = gl_adjusted / 100
    
    return bsi

def recommend_food(patient, food):
    bsi = calculate_bsi(patient, food)
    
    if bsi < 5:
        return f"{food.name} is a good choice for you. BSI: {bsi:.2f}"
    elif bsi < 10:
        return f"{food.name} may be consumed in moderation. BSI: {bsi:.2f}"
    else:
        return f"Avoid consuming {food.name}. BSI: {bsi:.2f} - **DANGER: HIGH BSI**"

def check_danger_condition(patient, food):
    bsi = calculate_bsi(patient, food)
    
    if bsi > 10:
        print(f"**DANGER: HIGH BSI ({bsi:.2f}) - SEEK MEDICAL ATTENTION IMMEDIATELY**")
    elif bsi > 8:
        print(f"**WARNING: HIGH BSI ({bsi:.2f}) - PLEASE CONSULT A DOCTOR**")

def main():
    # Create patient object
    patient_age = int(input("Enter your age: "))
    patient_gender = input("Enter your gender (male/female): ")
    patient_insulin_sensitivity = float(input("Enter your insulin sensitivity : "))
    patient = DiabeticPatient(patient_age, patient_gender, patient_insulin_sensitivity)

    # Food database with GI values
    foods = {
        "apple": Food('Apple', 20, 38),
        "banana": Food('Banana', 25, 42),
        "pizza": Food('Pizza', 30, 60),
        "bread": Food('Bread', 40, 70),
        "rice": Food('Rice', 50, 80),
        "oatmeal": Food('Oatmeal', 30, 42),
        "grapes": Food('Grapes', 20, 59),
        "mango": Food('Mango', 25, 51),
        "watermelon": Food('Watermelon', 10, 72),
        "pineapple":Food('Pineapple', 20, 59),
        "broccoli":Food ('broccoli', 10, 5),
        "carrots":Food ('carrots', 25,  10),
        "Chicken Breast":Food ('Chicken Breast', 0,  0),
        "egg":Food ('egg', 0,  1),
        "fish":Food ('fish' ,0,  0),
        "french fries":Food ('french fries', 75,  30),
        "grapes":Food ('grapes', 59,  20),
        "mango":Food ('mango', 51,  25),
        "orange": Food('orange',40,  15),
        "pasta":Food ( 'pasta', 50,  30),
        "Pear":Food ('Pear' ,35, 20),
        "pizza":Food ("pizza",80,  30),
        "potato":Food ("potato",70, 20),
        "salmon":Food ("salmon", 0,  0),
        "spinach":Food ("spinach",10,  5),
        "sweet Potato":Food ("sweet Potato", 50,  20),
        "tuna":Food ("tuna" ,0,  0),
        "watermelon":Food ("watermelon", 72,  15),
        "burger":Food ("burger", 85,  40),
        "chips":Food ("chips", 80,  30),
        "cookies":Food ( "cookies",75,  30),
        "doughnuts":Food ("doughnuts",80,  30),
        "ice cream":Food ("ice cream", 70,  30),
        "popcorn":Food ("popcorn", 65,  20),
        "soda":Food ( "soda", 90,  40),
        "fried rice":Food ( "fried rice",90,  60),
        "chicken curry":Food ("chicken curry", 50,  30),
        "mandi":Food ("mandi", 70,  50),
        "idli":Food ("idli" ,60,  40),
        "dosa": Food( "dosa",60,  20),
        "puttu":Food ("puttu",70,  50),
        "chutney":Food ("chutney", 40,  20),
        "juice":Food (  "juice",100,  40),
        "mutton biriyani": Food("mutton biriyani", 80,  55),
        "beef biriyani":Food ( "beef biriyani",75,50),
        "beef roast":Food ("beef roast", 0,  5),
        "cake": Food("cake",90,  60),
       "laddu":Food ("laddu", 90,  60),
       "jalebi":Food ("jalebi", 95,  65),
       "halwa":Food ("halwa", 90,  60),
       "kulfi":Food ("kulfi", 70,  40),
       "tapioca":Food ( ' tapioca', 87,  60),
       "chicken biriyani":Food ("chicken biriyani", 60,  50),
       "parotta":Food("parotta",50,40),
    }

    

    while True:
       
        
        food_name = input("\nEnter the name of the food you want to check: ").lower()
        
        if food_name in foods:
            food = foods[food_name]
            print(recommend_food(patient, food))
            check_danger_condition(patient, food)
        else:
            print("Food not found in database. Please try again.")

if __name__ == "__main__":
    main()



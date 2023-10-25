from __init__ import db
from model.cars import Cars  # Import the Car model

# Define the "Cars" model
class Cars(db.Model):
    # Define the table name in the database
    __tablename__ = 'cars'

    # Define model fields (columns)
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    make = db.Column(db.String(128), nullable=False)
    model = db.Column(db.String(256), nullable=False)
    year = db.Column(db.String(256), nullable=False)
    trim = db.Column(db.String(64), nullable=False)
    cylinders = db.Column(db.String(256), nullable=False)

    # Constructor to initialize a new car object
    def __init__(self, make, model, year, trim, cylinders):
        self.make = make
        self.model = model
        self.year = year
        self.trim = trim
        self.cylinders = cylinders

    # Method to return car details in dictionary format
    def alldetails(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "trim": self.trim,
            "cylinders": self.cylinders
        }

    # Method to add a new car to the database
    def create(self):
        try:
            db.session.add(self)  # Add the car to the session
            db.session.commit()  # Commit the transaction to the database
            return self  # Return the created car object
        except:
            db.session.rollback()  # Rollback the transaction if there's an error
            return None  # Return None to indicate an error

    # Method to return car details for API response
    def read(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "trim": self.trim,
            "cylinders": self.cylinders
        }

def initCars():
    car_data = [
        (9, "two seater", 11, 16, 8, "awd", "gas", 14, "bugatti", "chiron", "a", 2018),
        (9, "two seater", 11, 16, 8, "awd", "gas", 14, "bugatti", "chiron", "a", 2019),
        (9, " two seater", 11, 16, 8, "awd", "gas", 14, "bugatti", "chiron", "a", 2020),
        (9, "two seater", 11, 16, 8, "awd", "gas", 14, "bugatti", "chiron", "a", 2021),
        (8, "two seater", 10, 16, 8, "awd", "gas", 13, "bugatti", "chiron pur sport", "a", 2021)
    ]

    for data in car_data:
        make, model, cylinders, mpg_city, mpg_highway, drive_type, fuel_type, make_str, model_str, trim, year = data

        car = Cars(
            make=make_str,
            model=model_str,
            year=year,
            trim=trim,
            cylinders=cylinders,
            mpg_city=mpg_city,
            mpg_highway=mpg_highway,
            drive_type=drive_type,
            fuel_type=fuel_type,
        )
        db.session.add(car)

        # Method to get car details for the API response
        car_details = car.read()
    
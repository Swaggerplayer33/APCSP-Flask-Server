from __init__ import app, db
from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError
import os
import pandas as pd

# Car model
class Cars(db.Model, UserMixin):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(128), unique=True, nullable=False)
    model = db.Column(db.String(256), nullable=False)
    year = db.Column(db.String(256), nullable=False)
    trim = db.Column(db.String(64), nullable=False)
    cylinders = db.Column(db.String(256), nullable=False)

    def __init__(self, make, model, year, trim, cylinders):
        self.make = make
        self.model = model
        self.year = year
        self.trim = trim
        self.cylinders = cylinders

    def alldetails(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "trim": self.trim,
            "cylinders": self.cylinders
        }

# Function to initialize cars
def initCars():
    with app.app_context():
        print("Loading Cars")
        db.create_all()
        if db.session.query(Cars).count() > 0:
            return

        # Get the directory of the script where it's located
        script_dir = os.path.abspath(os.path.dirname(__file__))

        # Define the relative path to the CSV file
        relative_path = "CarStats.csv"

        # Construct the absolute file path
        file_path = os.path.join(script_dir, relative_path)

        try:
            df = pd.read_csv(file_path)

            for index, row in df.iterrows():
                car = Cars(
                    make=row['Make'],
                    model=row['Model'],
                    year=row.get('Year', None),
                    trim=row.get('trim', None),
                    cylinders=row.get('cylinders', None)
                )

                db.session.add(car)
                db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print("Duplicate car or error")
        except Exception as e:
            db.session.rollback()
            print(f"Error adding car: {str(e)}")

if __name__ == "__main__":
    initCars()

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
    year = db.Column(db.String(256), nullable=False)  # Assuming instructions can be nullable
    trim = db.Column(db.String(64), nullable=False)  # Assuming image_name can be nullable
    cylinders = db.Column(db.String(256), nullable=False)  # Assuming cleaned_ingredients can be nullable

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

# Favorite mode
# Function to initialize recipes
def initCars():
    with app.app_context():
        print("Loading Cars")
        db.create_all()
        if db.session.query(Cars).count() > 0:
            return

        basedir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(basedir, "Flask-Server-Back-End-/CarStats.csv")  # Changed to use os.path.join for better compatibility
        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            car = Cars(
                make=row['Make'],
                model=row['Model'],
                year=row.get('Year', None),  # Added a get method to handle the possibility of the key not existing
                trim=row.get('trim', None),
                cylinders=row.get('cylinders', None)
            )

            db.session.add(car)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                print(f"Duplicate car or error: {Cars.title}")
            except Exception as e:
                db.session.rollback()
                print(f"Error adding car at index {index}: {str(e)}")

if __name__ == "__main__":
    initCars()
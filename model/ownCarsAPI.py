
import os
import csv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name)


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    trim = dbm.Column(db.Float, nullable=False)

def initCars():
    with app.app_context():
        print("Creating car tables")
        db.create_all()
        if db.session.query(Car).count() > 0:
            return

        basedir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(basedir, "/Flask-Server-Back-End/CarStatsDatabase.csv")

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                car = Car(
                    make=row['Make'],
                    model=row['Model'],
                    year=int(row['Year']),
                    trim=float(row['Trim'])
                )

                db.session.add(car)
                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
                    print(f"Duplicate car or error: {car.make} {car.model}")
                except Exception as e:
                    db.session.rollback()
                    print(f"Error adding car: {str(e)}")

if __name__ == "__main__":
    initCars()

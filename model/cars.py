from __init__ import db

# Define the "Car" model
class Car(db.Model):
    # Define the table name in the database
    __tablename__ = 'cars'

    # Define model fields (columns)
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    fuel = db.Column(db.String, nullable=False)
    cylinders = db.Column(db.String, nullable=False)

    # Constructor to initialize a new car object
    def __init__(self, make, model, year, fuel, cylinders):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel
        self.cylinders = cylinders

    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "fuel": self.fuel, "cylinders": self.cylinders}
    # Create method to let users add a song to the DB
    def create(self):
        try:
            db.session.add(self)  # add prepares to persist object to table
            db.session.commit()  # SQLAlchemy requires a manual commit
            return self
        except: 
            db.session.remove() # remove object from table if invalid
            return None

    # Method to return car details for API response
    def read(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "fuel": self.fuel,
            "cylinders": self.cylinders
        }

def initCars():
    BugattiChiron = Car(make="Bugatti", model="Chiron", year="2021", fuel="Gas", cylinders="16"),
    TeslaRoadster = Car(make="Tesla", model="Roadster", year="2024", fuel="Electricity", cylinders="0"),
    RollsRoycePhantom = Car(make="Rolls Royce", model="Phantom", year="2021", fuel="Gas", cylinders="8"),
    MercedesBenzGClass = Car(make="Mercedes Benz", model="G Class", year="2022", fuel="Gas", cylinders="10"),
    AstonMartinDB11 = Car(make="Aston Martin", model="DB11", year="2023", fuel="Gas", cylinders="14"),
    Ferrari488GTB = Car(make="Ferrari", model="488GTB", year="2023", fuel="Gas", cylinders="9"),
    BentleyContinentalGT = Car(make="Bentley", model="Continental GT", year="2023", fuel="Gas", cylinders="10"),
    Porsche911Targa = Car(make="Porsche", model="911 Targa", year="2023", fuel="Gas", cylinders="8"),
    Mclaren720S = Car(make="McLaren", model="720 S", year="2024", fuel="Gas", cylinders="6"),
    MaseratiQuattroporte = Car(make="Maserati", model="Quattroporte", year="CNG", fuel="", cylinders="None"),
    AudiR8Spyder = Car(make="Audi", model="R8 Spyder", year="2022", fuel="Hydrogen Powered", cylinders="8"),

db.session.commit()    
from __init__ import db

# Define the "Car" model
class Car(db.Model):
    # Define the table name in the database
    __tablename__ = "Car"

    # This defines all of the attributes of a car that we will display
    id = db.Column(db.Integer, primary_key=True)  
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
    BugattiChiron = Car(make="Make: Bugatti", model="Model: Chiron", year="Year: 2021", fuel="Fuel: Gas", cylinders="Cylinders: 16"); db.session.add(BugattiChiron)
    TeslaRoadster = Car(make="Make: Tesla", model="Model: Roadster", year="Year: 2024", fuel="Fuel: Electricity", cylinders="Cylinders: None"); db.session.add(TeslaRoadster)
    RollsRoycePhantom = Car(make="Make: Rolls Royce", model="Model: Phantom", year="Year: 2021", fuel="Fuel: Gas", cylinders="Cylinders: 8"); db.session.add(RollsRoycePhantom)
    MercedesBenzGClass = Car(make="Make: Mercedes Benz", model="Model: G Class", year="Year: 2022", fuel="Fuel: Gas", cylinders="Cylinders: 10"); db.session.add(MercedesBenzGClass)
    AstonMartinDB11 = Car(make="Make: Aston Martin", model="Model: DB11", year="Year: 2023", fuel="Fuel: Gas", cylinders="Cylinders: 14"); db.session.add(AstonMartinDB11)
    Ferrari488GTB = Car(make="Make: Ferrari", model="Model: 488GTB", year="Year: 2023", fuel="Fuel: Gas", cylinders="Cylinders: 9"); db.session.add(Ferrari488GTB)
    BentleyContinentalGT = Car(make="Make: Bentley", model="Model: Continental GT", year="Year: 2023", fuel="Fuel: Gas", cylinders="Cylinders: 10"); db.session.add(BentleyContinentalGT)
    Porsche911Targa = Car(make="Make: Porsche", model="Model: 911 Targa", year="Year: 2023", fuel="Fuel: Gas", cylinders="Cylinders: 8"); db.session.add(Porsche911Targa)
    McLaren720S = Car(make="Make: McLaren", model="Model: 720 S", year="Year: 2024", fuel="Fuel: Gas", cylinders="Cylinders: 6"); db.session.add(McLaren720S)
    MaseratiQuattroporte = Car(make="Make: Maserati", model="Model: Quattroporte", year="Year: 2021", fuel="Fuel: CNG", cylinders="Cylinders: None"); db.session.add(MaseratiQuattroporte)
    AudiR8Spyder = Car(make="Make: Audi", model="Model: R8 Spyder", year="Year: 2022", fuel="Fuel: Hydrogen Powered", cylinders="Cylinders: 8"); db.session.add(AudiR8Spyder)
    MercedesBenz300SLGullwing = Car(make="Make: Mercedes Benz", model="Model: 300 SL Gullwing", year="Year: 2021", fuel="Fuel: Gas", cylinders="Cylinders: 6"); db.session.add(MercedesBenz300SLGullwing)
    Ferrari250GTCalifornia = Car(make="Make: Ferrari", model="Model: 250 GT California", year="Year: 2023", fuel="Fuel: Gas", cylinders="Cylinders: 8"); db.session.add(Ferrari250GTCalifornia)
    BentleyFlyingSpur = Car(make="Make: Bentley", model="Model: Flying Spur", year="Year: 2021", fuel="Fuel: Gas", cylinders="Cylinders: 4"); db.session.add(BentleyFlyingSpur)
    AudiA8 = Car(make="Make: Audi", model="Model: A8", year="Year: 2022", fuel="Fuel: Gas", cylinders="Cylinders: 8"); db.session.add(AudiA8)
    JaguarFType = Car(make="Make: Jaguar", model="Model: F-Type", year="Year: 2020", fuel="Fuel: Gas", cylinders="Cylinders: 10"); db.session.add(JaguarFType)
    LamborghiniHuracan = Car(make="Make: Lamborghini", model="Model: Huracan", year="Year: 2024", fuel="Fuel: Hydrogen Powered", cylinders="Cylinders: 12"); db.session.add(LamborghiniHuracan)
    RivianR1S = Car(make="Make: Rivian", model="Model: R1S", year="Year: 2023", fuel="Fuel: Electricity", cylinders="Cylinders: None"); db.session.add(RivianR1S)
    MercedesBenzMaybachSClass = Car(make="Make: Mercedes Benz", model="Model: Maybach S Class", year="Year: 2022", fuel="Fuel: Gas", cylinders="Cylinders: 6"); db.session.add(MercedesBenzMaybachSClass)
    BMW7Series = Car(make="Make: BMW", model="Model: 7 Series", year="Year: 2021", fuel="Fuel: Hydrogen Powered", cylinders="Cylinders: 8"); db.session.add(BMW7Series)
    LincolnContinental = Car(make="Make: Lincoln", model="Model: Continental", year="Year: 2020", fuel="Fuel: Gas", cylinders="Cylinders: 4"); db.session.add(LincolnContinental)
    RivianR1T = Car(make="Make: Rivian", model="Model: R1T", year="Year: 2022", fuel="Fuel: Electricity", cylinders="Cylinders: None"); db.session.add(RivianR1T)
    db.session.commit()
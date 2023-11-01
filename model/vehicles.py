import random

# Define the vehicles list with initial data
vehicles = [
    {
        "make": "Bugatti",
        "model": "Chiron",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Tesla",
        "model": "Roadster",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Rolls Royce",
        "model": "Phantom",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Mercedes Benz",
        "model": "G Class",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Aston Martin",
        "model": "DB11",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Ferrari",
        "model": "488GTB",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Bentley",
        "model": "Continental GT",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Porsche",
        "model": "911 Targa",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "McLaren",
        "model": "720 S",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Maserati",
        "model": "Quattroporte",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Audi",
        "model": "R8 Spyder",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Mercedes Benz",
        "model": "300 SL Gullwing",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Ferrari",
        "model": "250 GT California",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Bentley",
        "model": "Flying Spur",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Audi",
        "model": "A8",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Jaguar",
        "model": "F-Type",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Lamborghini",
        "model": "Huracan",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Rivian",
        "model": "R1S",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Mercedes Benz",
        "model": "Maybach S Class",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "BMW",
        "model": "7 Series",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Lincoln",
        "model": "Continental",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Tesla",
        "model": "Cybertruck",
        "likes": 0,
        "dislikes": 0,
    },
    {
        "make": "Lamborghini",
        "model": "Urus",
        "likes": 0,
        "dislikes": 0,
    },
]

def initVehicles():
    # Initialization of vehicles, you can add more vehicles here
    pass

def getVehicles():
    return vehicles

def getVehicle(make, model):
    return next((v for v in vehicles if v["make"] == make and v["model"] == model), None)

def bestVehicle():
    best = 0
    bestVehicle = None
    for vehicle in vehicles:
        if vehicle["likes"] > best:
            best = vehicle["likes"]
            bestVehicle = vehicle
    return bestVehicle

def worstVehicle():
    worst = 0
    worstVehicle = None
    for vehicle in vehicles:
        if vehicle["dislikes"] > worst:
            worst = vehicle["dislikes"]
            worstVehicle = vehicle
    return worstVehicle

def addLike(make, model):
    vehicle = getVehicle(make, model)
    if vehicle:
        vehicle["likes"] += 1
        return "Liked!"
    return "Vehicle not found", 404

def addDislike(make, model):
    vehicle = getVehicle(make, model)
    if vehicle:
        vehicle["dislikes"] += 1
        return "Disliked!"
    return "Vehicle not found", 404

def countVehicles():
    return len(vehicles)

def printVehicle(vehicle):
    print("Make:", vehicle["make"])
    print("Model:", vehicle["model"])
    print("Likes:", vehicle["likes"])
    print("Dislikes:", vehicle["dislikes"])
    print()

if __name__ == "__main__":
    initVehicles()

    best = bestVehicle()
    print("Best Vehicle:")
    printVehicle(best)

    worst = worstVehicle()
    print("Worst Vehicle:")
    printVehicle(worst)

    print("Random Vehicle:")
    random_vehicle = getVehicles()[0]  # Change to get a random vehicle
    printVehicle(random_vehicle)

    print("Vehicles Count:", countVehicles())
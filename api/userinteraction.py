import random

car_data = []

# Initialize car models
def initCars():
    car_list = [
        {"id": 0, "model": "Model A", "likes": 0, "dislikes": 0},
        {"id": 1, "model": "Model B", "likes": 0, "dislikes": 0},
        {"id": 2, "model": "Model C", "likes": 0, "dislikes": 0},
        # Add more car models as needed
    ]
    
    for car in car_list:
        car_data.append(car)

# Return all car models from car_data
def getCars():
    return car_data

# Car model getter
def getCar(id):
    return car_data[id]

# Return random car model from car_data
def getRandomCar():
    return random.choice(car_data)

# Liked car model
def likeCar(id):
    car_data[id]['likes'] += 1
    return car_data[id]['likes']

# Disliked car model
def dislikeCar(id):
    car_data[id]['dislikes'] += 1
    return car_data[id]['dislikes']

# Print car model details
def printCar(car):
    print(f"Car Model ID: {car['id']}")
    print(f"Model Name: {car['model']}")
    print(f"Likes: {car['likes']}")
    print(f"Dislikes: {car['dislikes']}")

# Number of car models
def countCars():
    return len(car_data)

# Test Car Model API
if __name__ == "__main__":
    initCars()  # Initialize car models
    
    # Random car model
    random_car = getRandomCar()
    print("Random Car Model")
    printCar(random_car)
    
    # Like and dislike car models
    car_id = random.randint(0, countCars() - 1)  # Choose a random car model
    likeCar(car_id)
    print(f"Liked Car Model {car_id}")
    printCar(getCar(car_id))
    
    car_id = random.randint(0, countCars() - 1)  # Choose another random car model
    dislikeCar(car_id)
    print(f"Disliked Car Model {car_id}")
    printCar(getCar(car_id))
    
    # Count of car models
    print("Car Models Count: " + str(countCars()))

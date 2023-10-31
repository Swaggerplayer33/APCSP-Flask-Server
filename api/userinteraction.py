import random

class CarModel:
    def __init__(self):
        self.car_data = []

    def init_cars(self):
        car_list = [
            {"id": 0, "model": "Model A", "likes": 0, "dislikes": 0},
            {"id": 1, "model": "Model B", "likes": 0, "dislikes": 0},
            {"id": 2, "model": "Model C", "likes": 0, "dislikes": 0},
            # Add more car models as needed
        ]
        self.car_data.extend(car_list)

    def get_cars(self):
        """Return all car models."""
        return self.car_data

    def get_car(self, car_id):
        """Return a car model by its ID."""
        for car in self.car_data:
            if car['id'] == car_id:
                return car
        raise ValueError("Car with ID {} not found".format(car_id))

    def get_random_car(self):
        """Return a random car model."""
        if not self.car_data:
            return None
        return random.choice(self.car_data)

    def like_car(self, car_id):
        """Increment the like count for a car model."""
        car = self.get_car(car_id)
        car['likes'] += 1
        return car['likes']

    def dislike_car(self, car_id):
        """Increment the dislike count for a car model."""
        car = self.get_car(car_id)
        car['dislikes'] += 1
        return car['dislikes']

    def print_car(self, car):
        """Print the details of a car model."""
        if car is not None:
            print(f"Car Model ID: {car['id']}")
            print(f"Model Name: {car['model']}")
            print(f"Likes: {car['likes']}")
            print(f"Dislikes: {car['dislikes']}")
        else:
            print("Car not found.")

    def count_cars(self):
        """Return the number of car models."""
        return len(self.car_data)

if __name__ == "__main__":
    car_manager = CarModel()
    car_manager.init_cars()

    random_car = car_manager.get_random_car()
    print("Random Car Model")
    car_manager.print_car(random_car)

    try:
        car_id = random.choice(car_manager.get_cars())['id']
        car_manager.like_car(car_id)
        print(f"Liked Car Model {car_id}")
        car_manager.print_car(car_manager.get_car(car_id))
        
        car_id = random.choice(car_manager.get_cars())['id']
        car_manager.dislike_car(car_id)
        print(f"Disliked Car Model {car_id}")
        car_manager.print_car(car_manager.get_car(car_id))
    except ValueError as e:
        print(e)
        
    print("Car Models Count:", car_manager.count_cars())

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name)

csv_file_path = 'CarStats.csv'  # Provide the relative or absolute path to your CSV file

@app.route('/api/cars')
def get_cars():
    car_data = pd.read_csv(csv_file_path)
    return car_data.to_json(orient='records')

if __name__ == '__main__':
    app.run()

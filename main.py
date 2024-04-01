import threading
from flask import render_template
from flask.cli import AppGroup

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app,db, CORS  # Definitions initialization
from api.user import user_api
from model.jokes import initJokes
from model.users import initUsers
from model.cars import initCars
from model.vehicles import initVehicles
from api.job import job_api
# database migrations
from model.users import initUsers
from model.reviews import initReviews
from model.jobs import initJobs
from model.jobuser import initJobsUsers
from api.jobuser import jobuser_api
from api.review import review_api


# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.car import car_api 
from api.vehicle import vehicles_api

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition


# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(app_projects) # register app pages
app.register_blueprint(car_api) #register car api
app.register_blueprint(vehicles_api) #register vehicles api
app.register_blueprint(user_api) # register api routes
app.register_blueprint(job_api)
app.register_blueprint(jobuser_api)
app.register_blueprint(app_projects) # register app pages
app.register_blueprint(review_api)

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/table/')  # connects /stub/ URL to stub() function
def table():
    return render_template("table.html")

@app.before_first_request
def activate_job(): # activate these items 
    allowed_origin = request.headers.get('Origin')
    if allowed_origin in ['http://127.0.0.1:4100/joblyFrontend/', 'http://localhost:4100/joblyFrontend/', 'https://aidanlau10.github.io/joblyFrontend/', 
                          'https://aidanlau10.github.io/', 'http://127.0.0.1:4100/joblyFrontend/jobs/', 'http://localhost:4100/joblyFrontend/jobs/',
                          'http://127.0.0.1:4100/joblyFrontend/survey','http://127.0.0.1:4100',
                          'https://aidanlau10.github.io/joblyFrontend/jobs/', 'http://127.0.0.1:4100']:
        cors._origins = allowed_origin
    
    db.drop_all() #drops preexisting entries fetched by api
    db.create_all() #recreates api entries
    initJokes()
    initUsers()
    initCars()
    initVehicles()
    initUsers()
    initReviews()
    initJobs()
    initJobsUsers()
    initSurveys()
    
@app.route('/vehicles')  # Change the route to /vehicles
def list_vehicles():
    return render_template("vehicles.html", vehicles=vehicles_api)

    
# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8420")

# Jilin Zheng // U49258796

## Prerequisites

You must have MongoDB installed locally, as well as all of the packages specified in [requirements.txt](requirements.txt).

## Instructions

1. Run the [diyml.py](diyml.py) script; if you have not explicitly changed the port MongoDB serves on, you should be able to access the API at localhost:5000/.

## Scripts

- [diyml.py](diyml.py): the module that ties all submodules together; also sets up the flask-restful app
- [authentication.py](authentication.py): consists of the UserAPI, which supports all of the user-related CRUD functions
- [database.py](database.py): connects the app to the MongoDB database

## Database Schemas - Going w/ MongoDB

<img width="1015" alt="Screenshot 2024-02-29 104240" src="https://github.com/jilinzheng/ec530-DIYML/assets/133818802/29b13614-548a-46f1-8e84-107fd5cd2b4f">

## References

- https://www.youtube.com/watch?v=ofme2o29ngU
- https://blog.webdevsimplified.com/2022-02/mongo-db/
- https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
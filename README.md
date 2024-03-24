# Jilin Zheng // U49258796 // DIYML

## Prerequisites

You must have MongoDB installed locally, as well as all of the packages specified in [requirements.txt](requirements.txt).

## Instructions

1. Run the [diyml.py](diyml.py) script; if you have not explicitly changed the port MongoDB serves on, you should be able to access the API at localhost:5000/.

## Scripts

- [diyml.py](diyml.py): the module that ties all submodules together; also sets up the flask-restful app
- [database.py](database.py): connects the app to the MongoDB database
- [authentication.py](authentication.py): consists of the UserAPI, which supports all of the user-related CRUD functions
- [data_upload.py](data_upload.py): handles image uploading and connects to the image collection; NOTE: no quotes around file path for curl form data

## Database Schema

<img width="421" alt="database_schema" src="https://github.com/jilinzheng/DIYML/assets/133818802/3bc6d7dc-8f62-45ac-a57b-5fec8ebbeb31">

## References

- [MongoDB Cheat Sheet](https://blog.webdevsimplified.com/2022-02/mongo-db/)
- [HTTP Status Codes Cheat Sheet](https://cheatography.com/kstep/cheat-sheets/http-status-codes/?source=post_page-----1353126d9cd9--------------------------------)
- [Flask-RESTful Documentation](https://readthedocs.org/projects/flask-restful/downloads/pdf/latest/)
- [File Uploads in Flask-RESTful](https://stackoverflow.com/questions/28982974/flask-restful-upload-image)
- [Splitting Flask App into Multiple Files](https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files)
- [Image Classification with Python and Scikit-learn](https://www.youtube.com/watch?v=il8dMDlXrIE)
- [Fruits Dataset](https://www.kaggle.com/datasets/utkarshsaxenadn/fruits-classification)

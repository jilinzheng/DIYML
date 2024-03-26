# Jilin Zheng // U49258796 // DIYML

## Demos

Below are video demonstrations of certain functions of the API, also serving as course assessments:

- [Task Queue Implementation](https://youtu.be/RKGiA2wFB6o)

Containerization

- <img width="1562" alt="Screenshot 2024-03-26 at 02 43 17" src="https://github.com/jilinzheng/DIYML/assets/133818802/cd0f3284-42df-46c8-9157-2ae8948da6e8">
- ![Screenshot 2024-03-26 at 02 44 50](https://github.com/jilinzheng/DIYML/assets/133818802/f9e29cd8-e711-41e9-991f-0007feee77f8)


## Instructions

### Installing from source code

0. Prerequisites: MongoDB, Redis
1. Clone this repository.
2. cd into the repo, create and activate a virtual environment, and run `python3 -m pip install -r requirements.txt`.
3. Start the Flask app with `python3 src/diyml.py`.
4. Start a (or many!) Redis worker(s) with `python3 src/worker.py`.
5. See [API documentation]() for usage.

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

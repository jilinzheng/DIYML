# Jilin Zheng // U49258796 // Do-It-Yourself Machine Learning!

## Table of Contents
1. [Purpose and Summary](#purp_and_sum)
2. [Features](#features)
3. [Installation Instructions](#instr)
    1. [Installing from source code](#instr_source)
    2. [Installing from Docker image (recommended)](#instr_img)
4. [Demonstrations (please see here for course assignments)](#demos)
    1. [Final Project Demo](#final_demo)

<a name="purp_and_sum"></a>
## Summary and Purpose

Do-It-Yourself Machine Learning is an easy-to-use REST API that allows users to easily train image classification models and create inference requests. This project was completed Spring 2024 for EC530 Software Engineering Principles @ Boston University.

<a name="features"></a>
## Features

This project showcases the following features:

- Manage a simple user database
- Upload/delete images
- Train image classification models with scikit-learn
- Create inference requests
- Get inference results
- Document database with MongoDB
- Task queues with Redis

For more specific details on API usage, please see the [API documentation](https://app.swaggerhub.com/apis-docs/Jilin/DIYML/0.0.1).

<a name="instr"></a>
## Installation Instructions

<a name="instr_source"></a>
### Installing from source code

0. Prerequisites: MongoDB and Redis running on default ports.
1. Clone this repository.
2. `cd` into the repo, create and activate a virtual environment, and run `python3 -m pip install -r requirements.txt`.
3. Start the actual API-serving Flask app with `python3 src/diyml.py`.
4. Start a (or many!) Redis worker(s) with `python3 src/worker.py`.
5. See [API documentation](https://app.swaggerhub.com/apis-docs/Jilin/DIYML/0.0.1) for usage.

<a name="instr_img"></a>
### Installing from Docker image (recommended)

1. Simply pull the [image](https://hub.docker.com/repository/docker/jilinnn/diyml/general).
2. You may choose to use your own container orchestration, but I have included a [Docker Compose file](docker-compose.yml) that includes the necessary dependencies, MongoDB and Redis, as well as a nice MongoDB visualizer, Mongo Express.
3. See [API documentation](https://app.swaggerhub.com/apis-docs/Jilin/DIYML/0.0.1) for usage.

<a name="demos"></a>
## Demos

Below are images/videos demonstrating certain functions of the API, which also serve as course assignment submissions:

<a name="final_demo"></a>
- Full API Demo Video
    
    - [![Full API Demo Video](https://github.com/jilinzheng/DIYML/assets/133818802/f3532809-ba14-40c6-bd39-40d7fdbcf50b)](https://youtu.be/-c4zb4-YEYE)

- [Task Queue Implementation](https://youtu.be/RKGiA2wFB6o)

- Containerization

    - <img width="1562" alt="Screenshot 2024-03-26 at 02 43 17" src="https://github.com/jilinzheng/DIYML/assets/133818802/cd0f3284-42df-46c8-9157-2ae8948da6e8">
    - <img width="1562" alt="Screenshot 2024-03-26 at 02 44 50" src="https://github.com/jilinzheng/DIYML/assets/133818802/f9e29cd8-e711-41e9-991f-0007feee77f8">

- Database Schema (MongoDB)

    - <img width="421" alt="database_schema" src="https://github.com/jilinzheng/DIYML/assets/133818802/3bc6d7dc-8f62-45ac-a57b-5fec8ebbeb31">

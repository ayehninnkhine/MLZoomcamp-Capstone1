# *House Price Prediction Project*  

## **About the project**   

The objective of the project is to predict the house price based on its features.
* 'area' - area of the house
* 'bedrooms' - number of bedrooms in the house
* 'bathrooms' - number of bathrooms in the house
* 'stories' - number of stories in the house
* 'mainroad' - locate on the main road or not (Yes/No)
* 'guestroom' - guestroom included or not (Yes/No)
* 'hotwaterheating' - hotwater service included or not (Yes/No)
* 'airconditioning' - air condition service included or not (Yes/No)
* 'parking' - number of carparks
* 'prefarea' - is it located in preference area? (Yes/No)
* 'furnishingstatus' - is the furniture included in the house? (category variable)
* 'price' - target variable: Price of the house


price               545 non-null int64
area                545 non-null int64
bedrooms            545 non-null int64
bathrooms           545 non-null int64
stories             545 non-null int64
mainroad            545 non-null object
guestroom           545 non-null object
basement            545 non-null object
hotwaterheating     545 non-null object
airconditioning     545 non-null object
parking             545 non-null int64
prefarea            545 non-null object
furnishingstatus    545 non-null object
   
Developed ML model is realized as a web service and deployed to the Google Cloud Platform.    
   
## **Structure of the repository**    
   
The repository contains the next files and folders:

* `README.md` - project documentation    
* `Housing.csv` - housing dataset (https://www.kaggle.com/datasets/ashydv/housing-dataset)
* `EDA-Model-Train.ipynb` - a notebook with exploratory data analysis and model training
* `train.py` - a python script to train the model with Random Forest Regressor
* `model.bin` - a stored linear regression model 
* `Pipfile` and `Pipfile.lock` - files with virtual environment for project
* `predict.py` - a python script to create a web service on the base of developed ML model    
* `Dockerfile` - to containerize the developed ML model
* `predict_local.py` - a python file to test and work with the locally deployed model
* `predict_cloud.py` - a python file to test and work with the model, deployed to Google Cloud Platform    

## **Virtual environment**   
   
Virtual environment of the project is provided by `Pipfile` and `Pipfile.lock`. These files contain all information about libraries and dependencies for the project. To create a virtual environment with libraries and dependencies required for the project, one should install `pipenv` library:  
   
`pip install pipenv`   
   
Then it's necessary to clone this repository from GitHub, open a terminal in the folder with this repository, and run the following commands:   
   
`pipenv install`   # to install project virtual environment
`pipenv shell`     # to activate virtual environment


## **Running a web service in a local server**   
      
Developed final model is implemented in a web service. To run it, it's necessary to install `Docker`, create a container (which contains all system dependencies, libraries, scripts and others) and run it.   
   
`Docker` may be installed from the official site https://www.docker.com/

File `Dockerfile` of the current repository (or cloned to your PC) contains all specifications to a container to be built: python, virtual environment, scripts and model file etc. To build a container one should start a `Docker`, open a terminal or command window and enter the next command:   
   
`docker build -t housing .` (For Linux)

`docker buildx build --platform linux/amd64 -t housing .` (For Apple M1)
   
Once docker container is built, you can run it with the next command:   
   
`docker run -it --rm -p 9696:9696 housing:latest`
   
A script `predict_local.py` sends to the local server a house with following features in json format:   

data = {
    'area': 7420,
    'bedrooms': 4,
    'bathrooms': 2,
    'stories': 3,
    'mainroad': 1,
    'guestroom': 0,
    'basement': 0,
    'hotwaterheating': 0,
    'airconditioning': 1,
    'parking': 2,
    'prefarea': 1,
    'semi-furnished': False,
    'unfurnished': False,
}

The result of script's work should be as follows:   

{
 "predicted_price": 15.946636576688716
}


## **Running a web service in a cloud**   
   
The web service is also deployed to Google Cloud Platform (Cloud Run) with the next commands:   
      
`gcloud config set project <project_ID>`  # create a project  (In this project, the project ID is sylvan-earth-375806)
   
`docker images`   # obtain a list of docker images to get exactly the name of needed image   
   
`docker tag housing:latest gcr.io/sylvan-earth-375806/housing_server`  # create a tag to image   
   
`docker push gcr.io/sylvan-earth-375806/housing_server` # push image to Google Container Registry   
   
`gcloud run deploy housing --image gcr.io/sylvan-earth-375806/housing_server --port 9696 --platform managed --region us-central1`    # deploy image to google cloud

Web service API is available on URL: https://housing-3zktkdeu6a-uc.a.run.app
   
A script `predict_cloud.py` sends to Google cloud server a house with the following features in json format:   

data = {
    'area': 7420,
    'bedrooms': 4,
    'bathrooms': 2,
    'stories': 3,
    'mainroad': 1,
    'guestroom': 0,
    'basement': 0,
    'hotwaterheating': 0,
    'airconditioning': 1,
    'parking': 2,
    'prefarea': 1,
    'semi-furnished': False,
    'unfurnished': False,
}

The result of script's work should be as follows:   

{
 "predicted_price": 15.946636576688716
}


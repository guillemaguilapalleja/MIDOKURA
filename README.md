# **SIMPLE API TO MANAGE GALLERIES AND IMAGES WITHIN THEM**
## *Made by Guillem Aguila i Pallejà*

## Context: We want to create/get/delete galleries, and within these galleries we want to create/get/delete images  that are within them. 


## INSTRUCTIONS TO RUN THE PROJECT:
#### First, we download the code and put it in a folder:

`cd path/to/the/folder`



#### Then, we build the docker with the name that we want (as an example, mine will be named *midokura*)

`docker build . -t midokura`

`docker run -p 8000:8000 -i midokura:latest`



#### Or, you could just run the project by typing following command, in the actual directory:

`uvicorn main:app`

#### The file called requirements.txt is the one I used to save the versions of all the python libraries I have used. By running the docker file by means of the instructions below, it automatically install those requirements. If you wish, you can create a virtual enviorament and add all those libraries to it, so you don't have this libraries in local. You can do it by means of the next command at the promt on the current folder:

`python -m venv venv`

#### And then we have to activate it. If you a using a 3.10.x version of python:

`\venv\Scripts\activate`

#### Nevertheless, I have created a virtual enviorament myself called *venv*, which is a folder in the actual directory. So, instead of creating it, you can just activate this virtual enviorament as mentioned below and then run the docker, and you will have the libraries installed directly inside the virtual enviorament (the docker will try to download it, but you will get a comment saying that all those libraries are actually installed).

## **Now our project is running!**
## **You can test it at the endpoint:**
> http://localhost:8000

## Or, if you wish, you can access to the custom Swagger IU by means of this endpoint:
> http://localhost:8000/docs

--------------------------------------------------------------
# **PROJECT COMMENTS**



## **As seen so far, we have 4 folders and 7 files:**


| Folders | Files |
| :---: | :-----------: |
| crud | crud.py |
| models | models.py |
| schemas | Galleries.py |
| schemas | Images.py |
| venv | Bunch of files |
| MIDOKURA | init.py |
| MIDOKURA | database.py |
| MIDOKURA | Dockerfile |
| MIDOKURA | README.md |
| MIDOKURA | requirements.txt |
| MIDOKURA | sql_app.db |

## In the crud.py file, we'll have the basic functions for running our project:


*`get_gallery_by_id`

*`get_gallery_by_name`

*`get_galleries`

*`create_gallery`

*`get_images`

*`create_gallery_image`

*`delete_gallery`

*`get_images_from_gallery`

*`get_image_by_id`

*`delete_image`

*`save_in_database`

## In the models.py file, we'll have the models for our  database: a model for Gallery and a model for Image (with all of their attributes initialized).


## In the schemas folder, we have 2 files: Galleries.py and Images.py, which both of them are models from a python library called Pydantic, which gives us the ability to validate all our data, among other features.

## And then we have a bunch of different files:

### The file called init.py enables us to run the project.
### The file called database.py is where the database is first created
### The file called Dockerfile is the docker image that I've created to run this project.
### The file main.py is the application itself. It contains all the different endpoints and what do we do in each one of them. For our profect, we have 5 different endpoints:

#### At this endpoint, we can either see our galleries or create one:
> http://localhost:8000/docs/galleries/

#### At this endpoint, we can either see one gallery in particular or either delete it:
> http://localhost:8000/docs/galleries/{gallery_id}/

#### At this endpoint, we can either see our galleries or create one:
> http://localhost:8000/docs/galleries/{gallery_id}/images/

#### At this endpoint, we can create an image inside a certain gallery or we can either get the images inside a gallery:
> http://localhost:8000/docs/galleries/{gallery_id}/images/{image_id}

#### At this endpoint, we can attatch a file to an image or either get the file attatch to that image:
> http://localhost:8000/docs/galleries/{gallery_id}/images/{image_id}/file

### The function of the file called requirements.txt is mentioned below.

### And the last file is the sql_app.db file. As it says, it's the file that contains the database itself, where all the images, galleries, and relations between them are saved.


## For further questions, please don't hesitate to contact me via email:
<guillem.aguila.palleja@estudiantat.upc.edu>


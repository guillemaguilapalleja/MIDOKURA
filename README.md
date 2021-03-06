# **SIMPLE API TO MANAGE GALLERIES AND IMAGES WITHIN THEM**
## *Made by Guillem Aguila i Pallejà*

## Context: We want to create/get/delete galleries, and within these galleries we want to create/get/delete images  that are within them. 

## INSTRUCTIONS TO RUN THE PROJECT:


#### First, we download the code and put it in a folder:

`cd path/to/the/folder`

### RUN THE PROJECT BY MEANS OF THE DOCKER IMAGE:

#### We build the docker with the name that we want (as an example, mine will be named *midokura*)

`docker build . -t midokura`

`docker run -p 8000:8000 -i midokura:latest`


### RUN THE PROJECT WITHOUT THE DOCKER IMAGE:

#### The file called *requirements.txt* is the one I used to save the versions of all the python libraries I have used. By running the docker file by means of the instructions below, it automatically install those requirements into the docker.

#### I have created a virtual enviorament myself called *venv*, which is a folder in the actual directory. So you can activate this virtual enviorament and you will not need to install those requirements. You can do this by means of the following command, in the directory where this folder is:

`venv\Scripts\activate`

#### And, finally, we run the project by typing following command, in the actual directory:

`uvicorn main:app`

**NOTE:** If we don't want to run the project with the docker provided and we don't want to activate either the provided virtual enviorament called *venv*, we will need to install all those libraries in local before running our project with the following command:

`pip install -r requirements.txt`

## IINSTRUCTIONS TO RUN THE TEST:
### We just go to the folder that contains the project and we type the following command:
`pytest my_folder/tests`


### For running the tests, we will need all the libraries within the project, as they are specified in the document  *requirements.txt*. We can see in the test file that:
* We are first creating a gallery.
* Then we create an image within that gallery.
* Then we delete that image.
* And finally we delete that gallery.
### Now we have runned the tests and we saw that everything works fine. Now we have to run the project by means of one of the two ways specified before the "INSTRUCTIONS TO RUN THE TEST" section.

**NOTE:** If we want to run our tests, we can not use the docker image because it is not specified in it to run the tests, it is only specified to run the project itself. If we want to first run the test and then run the project with the docker image, we have to run the tests first, then build the docker image and then we will have our project running.

---
## **Now our project is running!**
## **You can test it at the endpoint:**
> http://localhost:8000

## Or, if you wish, you can access to the custom Swagger IU by means of this endpoint:
> http://localhost:8000/docs

--------------------------------------------------------------
# **PROJECT COMMENTS**



## **As seen so far, we have 5 folders and 7 files:**


| Folders | Files |
| :---: | :-----------: |
| crud | crud.py |
| models | models.py |
| schemas | Galleries.py |
| schemas | Images.py |
| venv | Bunch of files |
| tests | test.py |
| MIDOKURA | database.py |
| MIDOKURA | Dockerfile |
| MIDOKURA | README.md |
| MIDOKURA | requirements.txt |
| MIDOKURA | sql_app.db |
| MIDOKURA | test.db |
| **ALL FOLDERS** | init.py |

## In the crud.py file, we'll have the basic functions for running our project:


* `get_gallery_by_id`

* `get_gallery_by_name`

* `get_galleries`

* `create_gallery`

* `get_images`

* `create_gallery_image`

* `delete_gallery`

* `get_images_from_gallery`

* `get_image_by_id`

* `delete_image`

* `save_in_database`

## In the models.py file, we'll have the models for our  database: a model for **Gallery** and a model for **Image** (with all of their attributes initialized).


## In the schemas folder, we have 2 files: *Galleries.py* and *Images.py*, which both of them are models from a python library called Pydantic, which gives us the ability to validate all our data, among other features.

## And then we have a bunch of different files:

### The file called *init.py* enables us to run the project.
### The file called *database.py* is where the database is first created.
### The file called *Dockerfile* is the docker image that I've created to run this project.

### The file *main.py* is the application itself. It contains all the different endpoints and what do we do in each one of them. For our project, we have 5 different endpoints:

#### At this endpoint, we can either see our galleries or create one:
> http://localhost:8000/docs/galleries/

#### At this endpoint, we can either see one gallery in particular or either delete it:
> http://localhost:8000/docs/galleries/{gallery_id}/

#### At this endpoint, we can either create an image within a gallery or get the images from a gallery:
> http://localhost:8000/docs/galleries/{gallery_id}/images/

#### At this endpoint, we can delete an image from a certain gallery or we can either get a certain image inside that gallery:
> http://localhost:8000/docs/galleries/{gallery_id}/images/{image_id}

#### At this endpoint, we can attatch a file to an image or either get the file attatch to that image:
> http://localhost:8000/docs/galleries/{gallery_id}/images/{image_id}/file

### The function of the file called requirements.txt is mentioned below.

### The file is the *sql_app.db file*. As it says, it's the file that contains the database itself, where all the images, galleries, and relations between them are saved.
### And the last file is the *test.db file*. That's the test database itself.


## For further questions, please don't hesitate to contact me via email:
<guillem.aguila.palleja@estudiantat.upc.edu>


# Social_network_test

The description of the installation below assumes that Git and Docker is already installed on the computer and that you know how to work with it.
The application has been developed and tested on Linux and is recommended to run on UNIX systems.

## How to deploy a project on your local machine

First, we make a clone of the repository to our computer command git clone https://github.com/ArtemGrom/social_network_test.git or with SSH keys git clone git@github.com:ArtemGrom/social_network_test.git

You need to run docker daemon.

Then you need to start the container with the command docker-compose up -d

Application deployed on local machine. 

You can go to http://localhost:8000/api/v1/auth or http://127.0.0.1:8000/api/v1/auth and see that the GET request worked and returned a page with a 200 OK status

## Social Network

1. User signup http://127.0.0.1:8000/api/v1/auth/users/
2. User login http://127.0.0.1:8000/api/v1/drf-authlogin/?next=/api/v1/auth/users/
3. Post creation http://127.0.0.1:8000/api/v1/listposts/ You need to send post method POST
4. Post like http://127.0.0.1:8000/api/v1/listposts/<id_post>/like You need to like the POST method
5. Post unlike http://127.0.0.1:8000/api/v1/listposts/<id_post>/unlike You need to unlike the POST method

Token authentication implemented with JWT. Get token http://127.0.0.1:8000/api/v1/token/ 
You need to enter a username and password and get a token using the POST method

The is-fan attribute keeps track of whether or not an authorized user has liked it.

Database used by Postgresql.

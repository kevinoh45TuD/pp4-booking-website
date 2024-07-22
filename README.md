# Classics and Cuisine

## Introduction

This project was created using Django. It is meant to emulate a restaurant website for customers to book a table.

It has been deployed on Heroku, the repository uses Code Institute's template.

[Link to Site](https://pp4-classics-cuisine-3b12317a4bfa.herokuapp.com)

Below I will outline key aspects of the project and its creation.

## Table of Contents

1. [UX](#ux)
    - Epics
    - User Stories
2. [Features](#features)
    - Home
    - Booking
    - User Profile
3. [Technologies Used](#technologies-used)
    - Python
    - Django
    - Heroku
    - HTML
    - Packages
4. [Testing](#testing-1)
    - 
5. [Deployment](#deployment)
    - Setting Up Repository
    - Deploying on Heroku
    - Clone Repository
    - Fork Repository
6. [Credits](#credits)
    - Code Institute
    - Other

## UX
### Epics

6 Epics were created for this project, these were expanded into user stories. The details of this can be found on the related kanban board [link](https://github.com/users/kevinoh45TuD/projects/1)

Epics:

1. Initial Project Setup
2. User Setup
3. User Functions
4. Movies Setup
5. Booking Setup
6. News Section

### User Stories

User Stories were created based on the above Epics:

1. 
    - Django Setup
    - Heroku Deployment
    - Database
2. 
    - Create Account
    - Account Login/ Logout
    - View Account
3. 
    - View Bookings
    - Change Details
    - Reset Password
4. 
    - Movie Section Layout
    - Movies / Menu data input
    - Change Day Function
5. 
    - Booking Section
    - Cancel Booking
    - Remove Unavailable

### Wireframes

Wireframes were created to initially plan the layout of different screens for the project.

The wireframes include a lot of details not later planned for the website.

- [Wireframe 1](/doc_files/pp4-wireframe1.png)
- [Wireframe 2](/doc_files/pp4-wireframe2.png)

## Features

### Home

Here the user will be able to see available movies. They will be able to click into a movie to go to the booking section.

### Booking

Here the user will select relevant options for making their booking.

### User Profile

Here the user will see their details and current bookings.

## Technologies Used

### Python

The following python modules were used:
- asgiref==3.8.1
- dj-database-url==2.2.0
- Django==4.2.14
- gunicorn==22.0.0
- packaging==24.1
- psycopg2==2.9.9
- sqlparse==0.5.1
- typing-extensions==4.12.2
- tzdata==2024.1
- whitenoise==6.7.0

### Django

- Django was used as the main framework for this project.

### Heroku

- Heroku was used to deploy this website online. [Heroku](https://www.heroku.com)

### HTML

- Html was used as the base language for the site templates.

### Packages

- VS Code was used to develop the code for this site.
- GitHub was used for version control. [Github](https://github.com)
- Balsamiq was used to create wireframes.

## Deployment

Code Insitute template was used for creation of repository of this site. [Template](https://github.com/Code-Institute-Org/ci-full-template)

### Setting Up Repository

I took these steps to setup my Github repository:
- Open the link to the Code Institute template mentioned above.
- At the top right corner click the button 'Use this template'.
- Click first option 'Create a new repository.
- Give the repository a relevant name and description.
- Make sure the repository remains public.
- At the bottom right click 'Create repository'.

### Clone Repository

Here I will outline the steps to clone a repository on GitHub.
This allows you to save a local copy.

Steps:
- Navigate to the GitHub page for the desired repository.
- Click on 'Code'
- Copy the link provided under HTTPS.
- Open Git Bash.
- Change the current working directory to the location where you want the cloned directory.
- Type 'git clone ' along with the copied link.
- Press Enter to create cloned repository.

Steps are based on GitHub documentation related to cloning repositories.

[GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui)

### Fork Repository

Here I will outline the steps to fork a repository on GitHub.
This allows you to have your own repository to make changes to based on an original repositories code/settings.
Additionally you may submit a pull request to the original repository owner.

Steps:
- Navigate to the GitHub page for the desired repository. 
- At the top right, below the search box, click 'Fork'.
- Leaving all the settings will be fine, but here you may apply a new name or description.
- Click 'Create fork'.

Steps are based on GitHub documentation related to forking repositories.

[GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

## Credits

### Code Institute

- Code Institute template used for repository [Template](https://github.com/Code-Institute-Org/ci-full-template)

- Code Institute learning modules used to learn different aspects of Python [Code Institute](https://codeinstitute.net/ie/)

### Other

- An article on GitHub was used to help with creating this README doc [Article](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
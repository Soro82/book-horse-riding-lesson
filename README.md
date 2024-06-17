# Book Horse Riding Lessons

Click [here](https://book-horse-riding-lesson-c2e71d72733b.herokuapp.com) for the live link.

## Introduction

The Horse Riding Lessons booking system allows users to book horse riding lessons. The user can set up a personal account by signing up to the site. When they are signed up they can login to their account to book a lesson. They can choose a date and time, whether they want the lesson indoor or outdoor, their level of experience and the horse they want for the lesson. When they book a lesson they can choose to edit the booking to make changes to it or they can delete the booking. There is a seperate page showing all the horse available and their details. The user can also see the three most popular horses on the Home page.

## Table of Contents

### [User Experience](#user-experience-ux)
* [Project Goals](#project-goals)
* [Target Audience](#target-audience)
* [New user](#first-time-user)
* [Registered user](#registered-user)
* [Admin user](#admin-user)
### [Agile Methodology](#agile-methodology)
* [Epics](#epics)
* [User Stories](#user-stories)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Horse Images](#horse-images)
* [Wireframes](#wireframes)
* [Data Model](#data-models)
* [Database Scheme](#database-scheme)
### [Features](#features-1)
* [Security Features](#security-features)
* [Existing Features](#existing-features)
* [Future Features](#future-features)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Deployment and Local developement](#deployment-and-local-developement-1)
* [Local Developement](#local-developement)
* [ElephantSQL Database](#elephantsql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)
### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgments](#acknowledgments)

## User Experience (UX)

### Project Goals

To allow users to:
* Book horse riding lessons.
* Create a personal account by signing up to the website.
* Set up a username and password for their account.
* Log in to their personal account.
* Choose a date and time for their lesson.
* Choose if they want their lesson indoor or outdoor.
* Choose their level of experience.
* Choose what horse they want for their lesson.
* Make changes to any bookings they have made.
* Delete a booking they made.
* See all the horses available with a picture of the horse and their height and color.
* See a list of available times for lessons.
* See the three most popular horses.
* Log out of their account.
* See a message confirming they are logged out.

### Target Audience

### New User

### Registered User

### Admin User

[Back to Top](#book-horse-riding-lessons)

## Agile Methodology

### Epics

* Set up Project
* Deployment
* Navbar Links
* User Registration
* Book a Lesson
* Add a Horses Page

### User Stories

#### Epic: Set up Project

* Create the project and book_lesson app
* Create the database
* Build the models
* Create the views
* Create the templates

#### Epic: Deployment

* Open a new Heroku application
* Add required Config Vars
* Set up a Procfile
* Set DEBUG to False

#### Epic: Navbar Links

* Links in navbar to login, log out, sign up and make a booking
* Log out and make a booking are disabled when no user is logged in
* Logged in username displayed when a user is logged in
* Burger icon replaces navbar on smaller screens

#### Epic: User Registration

* Set up account with a username, email and password
* Enter my age and height when registering
* See a message stating that I am logged in
* Have a logout button visible
* See a confirmation message when i logout

#### Epic: Book a Lesson

* Choose a date for a lesson
* Choose a time for a lesson
* Choose whether I want indoor or outdoor
* Choose my level of experience from a list of options
* See a list of possible lesson times
* See a confirmation message when i make a booking

#### Epic: Add a Horses Page

* See pictures of each horse on a page
* See details of each horse under their picture
* Have a "Book Now" button available under each horse in the Horses page

[Back to Top](#book-horse-riding-lessons)

## Design

### Color Scheme

### Horse Images

### Wireframes

### Data Model

### Database Scheme

[Back to Top](#book-horse-riding-lessons)

## Features

### Security Features

### Existing Features

### Future Features

[Back to Top](#book-horse-riding-lessons)

## Technologies Used

### Languages Used

### Databases Used

### Frameworks Used

### Programs Used

[Back to Top](#book-horse-riding-lessons)

## Deployment and Local Development

### Local Development

### ElephantSQL Database

### Cloudinary

### Heroku Deployment

[Back to Top](#book-horse-riding-lessons)

## Testing

| Location | Test | Expected Result | Result |
| :------: | :--: | :-------------: | :----: |
| Home Page | Click on Login | Opens the login page | Passed |
|  | Click on Sign Up | Opens the signup page | Passed |
|  | Click on Horses | Opens the horses page | Passed |
| Popular Horses | Click on Login | Opens the login page | Passed |
| Horses Page | Click on Login | Opens the login page | Passed |
|  | Click on Heading in navbar | Opens the home page | Passed |
|  | Click on Next | Display next 3 horses | Passed |
|  | Click on Previous | Display previous 3 horses | Passed |
| Login Page | enter invalid username | Error message displayed | Passed |
|  | Enter invalid password | Error message displayed | Passed |
|  | Click on Sign Up | Opens the signup page | Passed |
|  | No password entered | Please fill in this field | Passed |
|  | No username entered | Please fill in this field | Passed |
|  | Enter valid username and password | Successfully logged in message | Passed |


## References

### Docs

### Content

### Acknowledgments 

[Back to Top](#book-horse-riding-lessons)
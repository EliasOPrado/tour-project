# Tour Project

[![Build Status](https://travis-ci.org/EliasOPrado/tour-project.svg?branch=master)](https://travis-ci.org/EliasOPrado/tour-project)

<img src="/static/images/mockup.png" >

## Table of contents
<!--ts-->

1. [About](#about)
    1. [Goal](#Goal)
    2. [Functionality](#Functionality)
2. [UX](#UX)
    1. [Home Page](#Home-Page)
    2. [Categories](#Categories)
    3. [The Product View](#The-product-view)
    4. [The User Account Page](#The-User-Account-Page)
    5. [Font](#Font)
    6. [Mobile Display](#Mobile-Display)
    7. [Tablet Display](#Tablet-Display)
3. [Database Structure](#Database-Structure)
4. [Technologies](#Technologies)
5. [Coding challenges during development](#Coding-Challenges-During-Development)   
6. [Features](#Features)
7. [Features Left To Implement](#Features-Left-To-Implement)
8. [Testing](#Testing)
    1. [Mobile](#Mobile)
    2. [Tablets](#Tablets)
    3. [Laptops](#Laptops)
9. [Function Testing And Unsolved bugs](#Function-Testing-And-Unsolved-Bugs)
10. [Deployment](#Deployment)
11. [Credits](#Credits)
 <!--te-->

## About

Project Milestone Four - Code Institute

The Tour Store app was developed and deployed by Elias Prado as the last project for the Code Institute Software Development diploma.
This website is to emulate a touristic retreat webpage that provides for tourists different places to retreat and relax.

## Goal

The main goal of this project is to show the functionalities of an e-commerce using different technologies. Since this project is about retreat holidays, in this material I had a different approach in terms of showing to users full detail of the program or retreat. Therefore, in this project, the product or destination will be provided a full post to give users a good idea about what they will have in terms of trip.


## Functionality

Tour Store website is composed by five different applications: `accounts`, `cart`, `checkout`, `search` and `tour_store`. Using MVC architecture from the Django framework, each application holds its own model, view and controller that interacts all together into the `main_tour_folder` which basically is the controller of the overall application.

### Apps functionalities

#### The accounts app holds the functionality of `register`, `login`, `logout` and the `reset password`.
1. Register page

<div align="center">
<img src=/static/images/register.png">
</div>
- An username, email and password is required to create an account.
- Username must be unique.
- Password should not be short, must contain at least 8 characters and should not be common.
- As soon as the user creates its username they are redirected to home page.

2. Login page
- The login page is a normal page that will ask for for the name or email and the user password

3. Reset password
   - Step 1 and 2, at the login page, above of the button you can find the `forgot my password` link in which will lead to a form to add your account email.
   - Step 3, 4 and 5, You will receive an email with a link that will ask you to add a different password and finally setting your account.
  <img src="/static/images/passwordreset.png">
2. The cart app gives the user the ability to `view`, `add` and `adjust` the cart as they wish. Including more or less retreats to their trip package.
3. The checkout application holds and manipulates the `Stripe` API. In which empowers the overall application with the e-commerce functionality. In this application is developed and performed the forms users who are willing to buy any retreat, to plot their details into the checkout application forms and finalise the purchase.
4. Under the search application, a simple search functionality is used to find different destinations from the `Destinations` model.
5. `tour_store` app holds the important `models` that will be linked to the other applications as many-to-many using `ForeignKey()` method. Also, this application holds the main page as same as destination and detail page.


## UX:



##### Home Page


##### Destinations



##### The product view



##### The User Account Page


#### Font



#### Mobile Display

<img src="/static/images/mobile.png" width="200">

#### Tablet Display

<img src="/static/images/ipad.png" width="200">

## Database Structure

```

```

## Technologies

- HTML
- CSS
- Bootstrap
- Python
- Django
- Jinja 2
- Google fonts
- Font awesome

## Coding Challenges During Development



## Features

- Register and have its own page.
- Login.
- Add new product from user page based on its login.
- See product list on user page.
- Be able to visualize, edit and delete its own product.
- Navegate product pages.
- View product on its own page.
- Be able to add comments on product as well as delete it.

## Features Left To Implement



## Testing

The devices that the application was tested were:

### Mobile

- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6, 7 and 8
- iPhone 6, 7 and 8 Plus
- iPhone X

### Tablets

- iPad
- iPad Pro

### Laptops

- ThinkPad X1 Carbon
- ThinkPad T430


## Function Testing And Unsolved Bugs



### Unsolved bugs



## Deployment

To deploy to Heroku there are some steps to e followed:

1.
2.
3.
4.
5.
6.
7.
8.


9.
10.
11.

## Credits

[Mdbootstrap](https://mdbootstrap.com/snippets/jquery/marta-szymanska/1301459 )

## Tasks that should be accomplished

| Task           | Time required | Assigned to   | Current Status | Finished |
|----------------|---------------|---------------|----------------|-----------|
| 1. Add template | > two days  | Elias | done 24/02 | <ul><li>- [x] </li></ul>
| 2. Create tour_app | > A week  | Elias | done 26/02 | <ul><li>- [x] </li></ul>
| 3. Create shopping-cart app  | > two weeks  | Elias | done 10/03 | <ul><li>- [x] </li></ul>
| 4. Create authentication app | > A week  | Elias | done 09/03 | <ul><li>- [x] </li></ul>
| 5. Add pagination functionality | > One hour| Elias | done 13/03 | <ul><li>- [x] </li></ul>
| 6. Make deployment | > 3 weeks | Elias | done 23/03 | <ul><li>- [x] </li></ul>
| 7. Add WYSIWYG functionality | 2 weeks  | Elias | done 20/04 | <ul><li>- [x] </li></ul>
| 8. Exam and Exam preparantion (no code) | 2 months  | Elias | done 25/06 | :neckbeard:
| 9. Improve UI/UX | 2 or 3 weeks  | Elias | done 20/06 | <ul><li>- [x] </li></ul>
| 10. Initiate testing | 4 days  | Elias | done 25/06 | <ul><li>- [x] </li></ul>
| 11. readme file | a week  | Elias | in progress | <ul><li>- [ ] </li></ul>


1. ```Add template```: This task is simply add the template in the static folder and link within the code.
2. ```Create authentication app```: This task will be used the CI authentication app. (If it is not working should be created from scratch).
    1. This app have to have a form in which users can upload their photo, name, email and password.
3. ```Create in-house admin app```: It will be needed to be created a in-house page for the owner of the application.

    :paperclip: There will be needed to be added:
    1. login required.
    2. form that will add all the inputs for a new tour.
    3. List of different added tours.
    4. List of orders?
    5. ....
4. ```Create cart app```: This app will be the last and the hardest one.
5. ```Create authentication app```: This app has to have signup, signin and logout functionality.
6. ```Make deployment```: using AWS S3 and Heroku.
7. ```Add WYSIWYG functionality```: Use a third party app and install into the application to give a better look/UX in term of reading.
8. ```Exam and Exam preparation (no code)```: development stopped for two months.
9. ```Improve UI/UX```: Use a third party library to speed up the development and improvement of the project interface.
10. ```Initiate testing```: Add testing to all applications when needed.
11. ```Prep readme doc```: Include all features, bugs, testing, challenges, clicks and what you learned.

# Tour Project

[![Build Status](https://travis-ci.org/EliasOPrado/tour-project.svg?branch=master)](https://travis-ci.org/EliasOPrado/tour-project)

<img src="static/images/readme_images/mockup.png" >

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

# About

Project Milestone Four - Code Institute

The Tour Store app was developed and deployed by Elias Prado as the last project for the Code Institute Software Development diploma.
This website is to emulate a touristic retreat webpage that provides for tourists different places to retreat and relax.

# UX

## User goals
The target audience of Tour Project are:
- People who want to make a relax or spiritual trip.
- People who are looking for the best locations.
- Yoga practitioners who are looking for the best places to improve their spiritual, mind and body development.

User goals:
- Search for the retreat or destination by its keyword and receive a feedback by the website if it isn't available.
- Find information about the company such as address phone number and its mission.
- Finding the destination, the user can find details of it, such as text and picture based content related to the destination.
- The user can scroll on the retreat page and through different paginations.
- Also, be able to see a preview image of the destination, date and price on a card container.
- The user can also add comments to the destination they want.
- Add one or multiple trips to the shopping cart with the maximum ten people for each tour.
- Clicking on add he or she will be redirected to the cart page.
- If the user is not logged in they will be redirected to the login page before go to the cart page.
- Edit the shopping cart if required.
- Checkout using card payment.
- Once the payment is done a success message is sent below the navbar and disappear on three seconds after the user be redirected to the home page.

## Design choices
The Tour project website is a tour application that has its main customers, people who want to have a relax and spiritual retreat.
Therefore, the website design was designed to bring these characteristics to its users. In which all of its design details is aligned to its purpose.

### Fonts
- The font used in this project is [Roboto](https://fonts.google.com/specimen/Roboto#about) which is an user friendly mainly used by its creator Google to give a proper reading in different screen sizes.

### Colors
   - Cyan: ![#17a2b8](https://via.placeholder.com/15/17a2b8/000000?text=+) `#17a2b8`
   - Light-cyan: ![#D7FFFE](https://via.placeholder.com/15/D7FFFE/000000?text=+) `#D7FFFE`
   - Raven: ![#6c757d](https://via.placeholder.com/15/6c757d/000000?text=+) `#6c757d`
   - Dark-gray: ![#343a40](https://via.placeholder.com/15/343a40/000000?text=+) `#343a40`
   - Green: ![#28a745](https://via.placeholder.com/15/28a745/000000?text=+) `#28a745`
   - White: ![#fff](https://via.placeholder.com/15/fff/000000?text=+) `#fff`
   - Selago: ![#FFFEFF](https://via.placeholder.com/15/FFFEFF/000000?text=+) `#FFFEFF`
   - Light: ![#f8f9fa](https://via.placeholder.com/15/f8f9fa/000000?text=+) `#f8f9fa`
   - These set of colors were chosen to bring a smooth experience to the users as same as to match with the purpose of the application.

#### Styling
  - Box shadow in card to give a depth idea and contrast with the background.
  - Scroll effects to give a better experience to users.
  - Skew-y effect on index page to break standard pattern with linear gradient using light-cyan and Selago colors.

### Wireframes
The wireframes developed for this project was only taken three types of devices, desktop, tablet and mobile.
In addition, the tool used to develop this wireframes was [Balsamiq](https://balsamiq.com/) giving the ability to a rapid design.
  - [Mobile devices](https://tour-project.s3-eu-west-1.amazonaws.com/static/images/readme_images/Mobile_wireframes.png)
  - [Tablet devices](https://tour-project.s3-eu-west-1.amazonaws.com/static/images/readme_images/iPad_wireframes.png)
  - [Desktop devices](https://tour-project.s3-eu-west-1.amazonaws.com/static/images/readme_images/Desktop_wireframes.png)

# Features

Tour Store website is composed by five different applications: `accounts`, `cart`, `checkout`, `search` and `tour_store`. Using MVC architecture from the Django framework, each application holds its own model, view and controller that interacts all together into the `main_tour_folder` which basically is the controller of the overall application.

## Accounts
 The accounts app holds the functionality of register, login, logout and the reset password.

### Register page
<p align="center">
<img src="/static/images/readme_images/register.png" width="40%">
</p>
  - An username, email and password is required to create an account.
  - Username must be unique.
  - Password should not be short, must contain at least 8 characters and should not be common.
  - As soon as the user creates its username they are redirected to home page.

### Login page
<p align="center">
<img src="/static/images/readme_images/login.png" width="40%">
</p>
  - The login page is a normal page that will ask for the name or email and the user password who already registered their account.

### Reset password
  - Step 1: at the login page, above of the button you can find the `forgot my password` link in which will lead to a form to add your account email.
  - Step 2: Add the email from the account you need to reset the password.
  - Step 3: You will receive an email with a link that will allow you to add a different password sending you to a reset password form.
  - Step 4: Add a new password and confirm it.
  - Step 5: Once the password is set you can login with the new password.

  <img src="/static/images/readme_images/passwordreset.png">

## Tour_store

    <img src="/static/images/readme_images/transparent_navbar.png">

  tour_store app holds all the main pages in which the user will navigate. Such as:

#### home page
  - On the home page the navbar is displayed transparent to give a good UI to the project. However, once the user scroll the page down it becomes white to better contrast from the rest of the page and not confuse the user.

    <img src="/static/images/readme_images/top_locations.png">

  - The top location brings a set of three different location or retreats in which users can click and be redirect to the destination page.

    <img src="/static/images/readme_images/testimonials.png">

  - On the testimonials section the three different characters is displayed as one of the Tour Project past customers. Giving their experience to the user and how many stars the service bring in term of value to their lives.

    <img src="/static/images/readme_images/aboutus.png">

  - The about us section (on the right side) details the experience of the business (in which is fictitious) and display a contact form (on the left side) for users to send any query about the business.

   <img src="/static/images/readme_images/footer.png">

  - On the footer section the user will have a copy message, links for retreats and login or logout and the business contact such as phone numbers, email and address. Also icons of different social medias.

### Retreats
<p align="center">
 <img src="/static/images/readme_images/retreats_page.png" width="40%">
 </p>

  - The retreats page will display all of the retreats.
  - However, the pagination system will only display three destinations per page to not overload the page if there are a large amount of items.

### Retreat details  
  - The page that gives the full detail about the retreat as well as the possibility to add it to cart.
  - In addition, the formatting functionality that can be applied by the website admin.
  - The user can also on the top right corner add the destination to cart.

## Cart
 The cart app gives the user the ability to `view`, `add` and `adjust` the cart as they wish. Including more or less retreats to their trip package.
  - Besides the destination the user will have a card that will allow them to add how many people will go to the trip.
  - `Important`: Since this project is to provide the user to add retreats to card, they will not be able to book the trip. Where in an actual case, once it's paid the booking should have done directly to the business management. Therefore, in the future a book system will be developed to provide a better experience to customers.

<img src="/static/images/readme_images/cart_image.png">

## Checkout
  - The checkout application holds and manipulates the `Stripe` API. In which empowers the overall application with the e-commerce functionality.
  - In this application is developed and performed the forms users who are willing to buy any retreat, to plot their details into the checkout application forms and finalise the purchase.

<p align="center">
<img src="/static/images/readme_images/checkout_image.png" width="40%">
</p>

## Search
  - Under the search application, a simple search functionality is used to find different destinations from the `Destinations` model by the tour title as the key word retrieved.
  - If a user adds one or multiple destinations that is in the database, it will be retrieved and shown on destination page.
  - If the tour title plotted on the search bar doesn't have in the data base, a message will be displayed instead, describing that destination is not yet added in the database.

## Admin page

<p align="center">
<img src="/static/images/readme_images/admin_login.png" width="40%">
</p>

  - The admin login page was changed by the name of the website.

<p align="center">
<img src="/static/images/readme_images/admin.png" width="40%">
</p>

  - The admin page was separated by three sections:
     - Authentication and Authorization, where the admin can see and manage the users on the website.
     - Checkout, where the admin can see the orders done by the customers.
     - Tour store, where the admin will be able to check and approve comments and see the contacts done by prospects.

<p align="center">
<img src="/static/images/readme_images/wysiwyg.png" width="40%">
</p>
  - The WYSIWYG (what you see is what you get) functionality was implemented as a functionality from a third party application called [Ckeditor](https://ckeditor.com/). Where the normal text editor was changed to add more features such as:
     - Alignment
     - Tables
     - Images
     - Styling
     - Add more html elements
     - And much more.


## Features Left To Implement
  1. Admin page graphs to display data from comments, sales and views.
  2. Booking system to automate sales.
  3. Add multiple images on retreat preview such as horizontal carousel.
  4. Add tutor section for each retreat.
  5. Add real location with maps at the bottom of each retreat detail page.
  6. Add star based review.




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

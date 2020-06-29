# Graphic Designs

Graphic designs is a somewhat e-commerce platform that provides posters/logos and branding as well as custom quote to suit the customers needs
The project itself can be viewed here [https://adamwragg-graphic-designs.herokuapp.com/](https://adamwragg-graphic-designs.herokuapp.com/)
 
## UX

This website is for people looking for graphic design services. Whether it be for a logo/poster. Complete branding packaging and print to an entire website design

- As a user type, I want to perform an action, so that I can achieve a goal.
- As a user I want to see previous work carried out.
- As a user I want to be able to easily purchase logos/poster on the shop
- As a user I want to be able to easily obtain a quick estimate as to how it will cost to have a custom order done
- As a user I want to be able to easily send my project to the site owner.
- As a user I want to receive confirmation of my order.
- As a user I want to be able to view my previous orders
- As a user I want to have a profile on the website to review my details

## Features

The website is fully responsive. The user is easily able to create an account, purchase items from the shop and also ask for custom works.

## Features Left to Implement
- Allow users that submit an item for custom work to submit a round of changes
- Once the site has some users. I will be adding an testimonials page showcasing works completed and the users reviews

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Python](https://www.python.org/)
    - Python was used to create all the logic behind the application

- [Django](https://www.djangoproject.com/)
    - Django was used as the framework behind the application

- [HTML5](https://www.w3.org/TR/html/) & [CSS3](https://www.w3.org/Style/CSS/)
    - HTML5 & CSS3 were used to create the layout and styling of this site
    - Code validators were used to check for errors with the [HTML](https://validator.w3.org/) and [CSS](https://jigsaw.w3.org/css-validator/)

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Javascript and the selected external libraries have been used throughout this site.
    - Mainly [JQuery](https://jquery.com/)

- [Git & GitHub](https://github.com/)
    - Git used for version control. GitHub used as a remote repository and the hosting of this site.

- [Heroku](https://www.heroku.com)
    - Heroku used as a remote repository and the hosting of this site.


## Testing

Testing some of the above user stories:

1. Custom Quote Form:
    1. Go to bottom of the page click 'request quote' button
    2. You will be taken to a contact form
    3. Try to submit an empty form and verify that an error message about the required fields appears
    4. Try to submit the form with an invalid email address and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears.

2. Custom Estimate Generator:
    1. On the same page as above got to the estimate calculator
    2. Try to submit empty data and verify that an error message about the required fields appears
    3. Try to submit the form with all inputs valid and verify that a success message appears.

3. Checkout Form
    1. navigate to the shop click on product and add to cart.
    2. If you have signup previous your information will be there already prefilled out for other wise fill out the fields
    3. Try to submit an empty form and verify that an error message about the required fields appears
    4. Try to submit the form with an invalid email address and verify that a relevant error message appears
    5. Try to submit the form with all inputs valid and verify that a success message appears

The following physical devices tested with no issues found.
- Windows desktop HD & UHD
- Google Pixel 2
- Apple iPad Pro
- Apple MacBook Air

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Deployment 

The site was developed locally using Visual Studio Code and uses git for version control which is then pushed to GitHub and Heroku. The site is hosted on GitHub Pages and deployed there from the master branch on GitHub. There is no difference between the development version of this site, and the final version hosted on GitHub Pages.

To deploy this project, I took the following initial steps:

From my GitHub page I clicked on 'Repositories' and selected the required repository.

I then clicked on the 'settings' option, located on the top horizontal menu bar

Next, I scrolled down the page to the GitHub Pages section and located the dropdown box under 'Source'

From there I selected the 'master branch'

GitHub takes you back to the top of the page to allow you to rename the repository if desired. I kept it the same.

These steps resulted in the finished site being deployed at https://adammcadam.github.io/graphic_designsV2/.

Every subsequent push to GitHub on the master branch updates the deployed site to match.

A PostGres database is used and setup inside Heroku. 

A Procfile has also been used to help Heroku know what commands are run by the apps dyno's.

### Content
- All products are made up for the purposes of this store and do not actual exist. Any resemblance to an actual company is purely coincidence

### Media
- All images on the site including the favicon are from [https://www.pexels.com/](https://www.pexels.com/) and are therefore royalty free

### Acknowledgements
- Visual inspiration for the site came from [https://www.lynxandcompany.com/](https://www.lynxandcompany.com/)
- Functionality and functional inspiration for the site came from Code Institues Boutique Ado Site
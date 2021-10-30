# THE WINE SHOP

Milestone Project 4 - FULLSTACK FRAMEWORKS - Code Institute 

![MS4 The Wine Shop](https://github.com/MWatty/the-wine-shop/blob/main/media/Mock%20Up.png "MS4 - The Wine Shop")

## Demo 

A live demo can be found [here](https://mw-the-wine-shop.herokuapp.com/)

## UX 

### Strategy 

The Wine Shop - is, as the name suggests, a website that sells wine.This website aims to allow customers 
to simply and securely purchase wines of their choosing. This is aided by the fact the customer can search 
and sort products easily and provides a seamless shopping experience thus enticing the customer to return. 

### User Stories 

|   User Stories                   |   As a …            |   I want to be able to …                                                        |   So that I can …                                                             |
|----------------------------------|---------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|   Browse Products                |                     |                                                                                 |                                                                               |
|   1                              |   Customer          |   View all products for sale                                                    |   Make a purchase                                                             |
|   2                              |   Customer          |   Find out information about products                                           |   I can make an informed decision on what to purchase                         |
|   3                              |   Customer          |   View the products on any of my devices                                        |   I can make a purchase no matter where I am easily                           |
|   4                              |   Customer          |   Simply navigate through the website                                           |   Efficiently and effectively make my purchase                                |
|   Search & Sort Products         |                     |                                                                                 |                                                                               |
|   5                              |   Customer          |   Search for products by name or description                                    |   Quickly make a purchase                                                     |
|   6                              |   Customer          |   Sort the products by category                                                 |   Only view the products that I am interested in                              |
|   7                              |   Customer          |   Sort the products by price                                                    |   Make a purchase based on my budget                                          |
|   Register & Manage my Account   |                     |                                                                                 |                                                                               |
|   8                              |   Customer          |   Create an account                                                             |   Return to the site and easily purchase products                             |
|   9                              |   Return Customer   |   Login to my account                                                           |   return to the site and make purchases quickly                               |
|   10                             |   Return Customer   |   Login to my account                                                           |   Return to the site and look at my order history                             |
|   11                             |   Return Customer   |   Login and logout of my account                                                |   Acces my profile securely                                                   |
|   12                             |   Return Customer   |   Recover my account if I forget my password                                    |   Gain access to my profile                                                   |
|   13                             |   Return Customer   |   Access my profile                                                             |   Update my personal details if they change                                   |
|   Checkout & Pay                 |                     |                                                                                 |                                                                               |
|   14                             |   Customer          |   Select a quantity of items                                                    |   Add the items to my basket                                                  |
|   15                             |   Customer          |   Remove items from my basket                                                   |   Only purchase the products that I want                                      |
|   16                             |   Customer          |   View a list of the products in my basket and the individual and total costs   |   Figure out exactly what I am purchasing and the cost of the purchase        |
|   17                             |   Customer          |   Enter my details to make a payment                                            |   Pay for my items and ensure they are delivered to the correct address       |
|   18                             |   Customer          |   Pay for my items securely                                                     |   Be assured my details are safe and payment handled securely                 |
|   19                             |   Customer          |   Confirm that my order has been processed                                      |   Be sure that my purchase has gone through and I will receive the products   |
|   Site Administration            |                     |                                                                                 |                                                                               |
|   20                             |   Site Owner        |   Add and remove products from the site                                         |   Ensure all products details are up to date and correct                      |
|   21                            |   Site Owner        |   Edit product details                                                          |   Change product details where necessary                                      |
|                                  |                     |                                                                                 |                                                                               |
			


### Scope

* The site owner wants to create a website that acts as a one stop shop for a persons wine needs, that simply breaks down the categories and offers 
succinct and simple information relating to the wine. The site owner also wants to sell wines that are affordable. The site owner, through the 
new feature of the blog, wants to create a space where people can learn about wines and improve interaction through the use of comments. 
 

### Structure 

* In order to meet the expectation of "The Wine Shop" users, the website aims to stick to convention 
in its layout and architecture.

* There is a header section on each page, with a "The Wine Shop" title in the header. Clicking on this
title will take the user back to the landing page of the website and this is, as mentioned above, 
an expected and understood convention. 

* There is a Log In / Registration Feature which enables users to create an account.

* All elements of the website are easily discoverable and aim to ensure that the user can get to their desired destination within 3 clicks. 

* The colouring, theme and terminology used throughout the website is consistent.

* The website is interactive and provides lots of feedback to the user. 

* The architecture of this website has been carefully considered with the user in mind and allows for ease of movement through the content. 

* Information on this section has been inspired by the information on [Code Institute](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment)

### Skeleton 

All wireframes were created using [Balsamiq](http://balsamiq.com)

Please find full PDF versions of wireframes and sketches below:

* [Mobile Wireframe](https://github.com/MWatty/the-wine-shop/blob/main/media/wireframes/THE%20WINE%20SHOP%20MOBILE.pdf)

* [Tablet Wireframe](https://github.com/MWatty/the-wine-shop/blob/main/media/wireframes/THE%20WINE%20SHOP%20TABLET.pdf)

* [Desktop Wireframe](https://github.com/MWatty/the-wine-shop/blob/main/media/wireframes/THE%20WINE%20SHOP%20DESKTOP.pdf)

#### Database Architecture

* SQLLite3 was used during the development phase, this is an included feature in the Django installation. 

* Heroku Postgres is used in the production site. 

* Please see the database schema below:

![Database Schema]( "Database Schema")


### Surface 

#### Design 

* The overall design of the website is simple. The site owner wants the user to simply navigate and 
understand what is on offer without being inundated with information. Clear text and imagery are used to achieve this. 

#### Colour 

* The colour theme used throughout the website is simple and minimalist, the theme was specifically chosen to allow 
for the images to stand out and ensure that users can fully appreciate the products for sale. 

* When choosing the colours the [Colour Picker Tool](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool) was used to assist.

#### Typography

* Lato was chosen as this is a simple, classy and unfussy font which will be clear and easy to read. 
This was chosen using [google fonts](https://fonts.google.com/)

* font-family: 'Lato', sans-serif;

#### Images 

* The background image used on the website homepage has been carefully chosen to ensure the theme of the website is understood at first glance. 
  

### Final Project Variations 

#### Navigation Bar

* A navigation link "Blog" was added to the navigation bar. 

* The dropdown feature on the all wines section was added to the final site as this ensures user stories could be met and items can be filtered by price, origin and category. 


#### Main Container Landing Page

* The Banner with the information on deliveries was added as an additional feature. 

#### All Wines Page

* The additional sort by feature was added to allow for an enhanced user experience. 

* Also, the title at the top of the page under the banner was added ("WINES") to act as an additional signpost for the user.

* When a superuser is logged in there are also additional icons to edit and delete products, this feature was not shown on the 
initial wireframes and was considered an essential feature in development in order to meet the site owner user stories. 

* This page also shows the number of products on the page and what category page you are viewing. 

#### Sign In 

* The remember me feature was added to the sign in page, this is a nice feature to enhance the user experience. 

* The forgot password? prompt was also added in to ensure that user stories were met and to allow the user to reset their passwords should they need to. 

#### Shopping Bag 

* Update and remove buttons were added in to ensure that the user had the ability to update and remove as per the user stories. 

* The note with regard free delivery was also added in to this page to bring the offer to the attention of the user.

#### Blog 

* The add a blog post page was added to the site to allow superusers to create and add blog content. 

* Superusers can also edit the blog post by clicking on the edit button. 

#### Comments 

* The comment feature was added to the blog post to allow for increased interaction between users and the site owner. 

* Edit and Delete comment features are available for logged in users. 


## Features 

### Existing Features 

*	This website is responsive on all devices, please see testing document for one minor exception.
*	There are interactive elements throughout the website.

### Landing Page

#### Header

* The header is on every page throughout the site, to allow for ease of navigation. 

##### Navigation
* A navigation bar is, as expected, located across the top of the page, this notifies the user of the home, log in and registration pages, search functionality and the categories of products on offer. 

##### Log In / Registration 

* There are standard simple login and registration facilities on the home page allowing the user to simply create an account or log in to their own account. 

* The account will have to be verified, the user will receive an email to verify their account and once they do they can log in. 

##### Search 
 
* There is a search functionality within the header of the landing page allowing the user to quickly and easily search for products that they may be looking for. 
 
* There is also a shop now feature on the hero image, that takes the user to the All Wines Page. 

##### Shopping Cart

* As the user shops this cart will update with the products and price. 

### Wines Pages 

* The pages that showcase the wines allow the user to click on the product, find out further information and add the product to their basket in quantities of their choosing. 

* The products can also be sorted by price, origin, name or category. 

### Payment 

* Users can make payments through stripe. 

* Once payment has been completed, users will get a pop up order confirmation on screen together with an email confirming their order. 

### SuperUser

* The superuser has the ability to add, delete and edit products, blog posts and comments. 

### Comments 

* A logged in user has the ability to edit and delete their own posts. 


### Features left to implement 

* Guest Checkout.
* Payment options would be improved to include Apple Pay, Klarna etc. 
* Further products would be added to the store.
* Sign in would be enhanced to include Google, Apple etc. 
* Gift Cards would be an option to purchase as a gift. 
* Enhanced vetting on the age of customers to ensure they are over 18 years old. 


## Technologies Used 

### Languages

* [HTML5](https://www.graycelltech.com/why-use-html-5/) was used as this is the latest Hypertext Markup Language and this is the standard language for describing the contents and appearance of Web Pages.

* [CSS](https://www.w3schools.com/css/css_intro.asp) is used to define styles for web pages, including the design, layout and variations in display for different devices and screen sizes.

* [JavaScript](https://www.w3schools.com/js/DEFAULT.asp) is used to program the behaviour of webpages.

* [Python](https://www.python.org/) is used to ensure interaction between the webpages and the database. 

### Framework, Libraries & API

* [Google-Fonts](https://fonts.google.com/) were used to style the website fonts and ensure they complimented each other.

* [Balsamiq](https://balsamiq.com/) used to create the wireframes. 

* [Font Awesome](https://fontawesome.com/) was used to add font icons to the website. 

* [JQuery](https://jquery.com/) was used to make the use of JavaScript on the website easier. 

* [Django](https://www.djangoproject.com/) is used as main web framework for the website.

* [Django Crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/#) is used for simplifying forms through Python.

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) is used for user login and user registration.

* [Bootstrap](https://getbootstrap.com/) is used as this lends itself to quickly design and custokise mobile first sites. 

* [Stripe](https://stripe.com/) is used for the payment system in the checkout app.

* [Gunicorn](https://gunicorn.org/) is used for the deployment to Heroku.

* [Psycopg2](https://pypi.org/project/psycopg2/) is used as an adapter for PostgreSQL with Django. 



### Version Control 

* [GIT](https://git-scm.com/) was used as version control in utilising [Gitpod](https://gitpod.io) to add code, commit and push to [GitHub](https://github.com).

* [Gitpod](https://gitpod.io) was used as this is an open source platform for automated and ready to code development environments that blends into your existing workflow.

* [GitHub](https://github.com) was used as a hosting platform for version control.

### Tools and Other Resources 

* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) was used to edit pages and diagnose problems quickly. 

* [Browserling](https://www.browserling.com/) was used for cross browser testing.

* [Am I responsive](http://ami.responsivedesign.is) was used to create a mock up.

* [Web Formatter](https://webformatter.com/html) used to correctly indent files. 

* [Heroku](https://id.heroku.com) was used to delpoy the app. 

* [Amazon Web Services](https://aws.amazon.com/) used to store static files and images. 

* [PEP8 Online Check](http://pep8online.com/) was used to check Python syntax.

* [Extends Class](https://extendsclass.com/python-tester.html) was used to check Python syntax.

* [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables) was used to create the user stories table.

## Testing 

Details on testing are stored in a seperate file [here](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing.md)

### Testing User Stories from User Experience (UX) Section

For details on testing user stories from user experience please go [here](https://github.com/MWatty/the-wine-shop/blob/main/testing/user_stories/userstory.md)


## Deployment 

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MWatty/the-wine-shop)
2. Locate the "Fork" Button and Click it. 
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MWatty/the-wine-shop)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Deploying to Heroku from Gitpod

1. Open [Heroku](https://heroku.com) in the browser and login creating a new account if required.
2. On the Heroku Dashboard click New->Create New App.
3. Give the app a new name and choose a region closest to you. Click the Create App button.
4. On the resource tab provision a new Postgres database selecting the free Hobby Dev plan.
5. To use Postgres in the application two packages are required - these are dj-database-url and psycopg2. To install these in Gitpod type the following commands:
    * `pip3 install dj_database_url`
    * `pip3 install psycopg2-binary`
6. Freeze the requirements in Gitpod by typing `pip3 freeze > requirements.txt`. Heroku will use the requirements.txt file to install these packages during deployment.
7. Open the settings.py file and import the dj_database_url package by adding `import dj_database_url` at the top of the file underneath `import os`.
8. In the database section comment out the default configuration and replace with the code below. The DATABASE_URL can be found under the settings tab in Heroku in the Config Vars section.

```
    DATABASES = {
        'default': dj_database_url.parse('DATABASE_URL')
    }
```
9. As a new database has been connected the migrations will need to run again to setup the database. Type in the following commands in Gitpod to run the migrations.
    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`
10. The database can be populated using the fixtures and JSON files. Run the following commands to load the data into the Postgres database:
    * `python3 manage.py loaddata categories`
    * `python3 manage.py loaddata products`

11. Create a superuser account for Django Administrator Panel using command `python3 manage.py createsuperuser`. When prompted enter a username, email address and password.
12. To ensure the database URL doesn't end up in version control replace the database configuration as setup in step 8 with the code below. When running on Heroku the DATABSE_URL will be defined in the Config Vars and the correct URL will be parsed by dj_database_url. Otherwise the sqlite database will be used when running in the Gitpod development environment.
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
```
13. For the app to run the Gunicorn webserver package is required. To install this package run command `pip3 install gunicorn`.
14. Freeze the requirements by running command `pip3 freeze > requirements.txt`.
15. In the root directory of the project create a Procfile by running command `touch Procfile`. The Procfile is used to tell Heroku to create a web dyno to run gunicorn and serve our Django app.
16. Open the Procfile copy in the following text ensuring there is no blank line at the end of the file.
```
    web: gunicorn the_wine_shop.wsgi:application
```
17. Login to Heroku using the `heroku login -i` command.
18. As AWS will be used to host the static files we need to prevent Heroku from collecting static files during deployment. This can be done by setting DISABLE_COLLECTSTATIC to 1. Enter the following command to set DISABLE_COLLECTSTATIC:
    * `heroku config:set DISABLE_COLLECTSTATIC=1 --app app-name`
19. In the settings.py file add the Heroku app the list of allowed hosts. Also add in localhost to ensure the app still works in Gitpod.
    * `ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']`
20. Edit the .gitignore file (or create a new one if it doesn't exist) and add the following if required:
```
    core.Microsoft*
    core.mongo*
    core.python*
    env.py
    __pycache__/
    *.py[cod]
    node_modules/
    .github/
    *.sqlite3
    *.pyc
```
21. Commit the changes to the main Github repository using the following commands:
    * `git add .`
    * `git commit -m "Add commit message here"`
    * `git push`
22. Initialise the Heroku repository using command `heroku git:remote -a app-name`.
23. To deploy the app to Heroku push the changes to the remove Heroku repository using command `git push heroku main`. This will deploy the site without any static files.
24. To automatically deploy when any changes are committed to Github click in the Deploy tab in Heroku and set the Deployment method to Github.
25. In the Connect to GitHub section search for the repository and click connect when the correct one is found.
26. In the Automatic Deploys section click on the Automatic Deplots button. This ensures that every time we push any changes to Github the code will be automatically be deployed to heroku as well.
27. Create a new Django secret key using the [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) website.
28. In Heroku under the Settings tab create a new Config Var with a key name of SECRET_KEY with the value set to the key generated in the previous step.
29. To ensure the Heroku app picks up this key add the following to the settings.py file:
    * `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
30. Commit the changes to Github. Heroku should pickup the changes from Github and deploy the site to app-name.herokuapp.com.


### AWS S3 Configuration

The AWS S3 service will be used to host all static files and images.

1. Open [AWS](https://aws.amazon.com) in the browser and login creating a new account if required.
2. Open the AWS Management Console and search for the S3 service using the search box if it isn't listed in your recently accessed services.
3. Click 'Create New Bucket' to create a new bucket. It is recommended to give the bucket the same name as your Heroku app.
4. Select the region closet to you.
5. Uncheck 'Block all public access' and using the tick box below to acknowledge that the bucket will be public. Click 'Create bucket'.
6. Select your bucket from the bucket list. In the properties tab turn on static website hosting and set the following default values then click save.
    * Index document: `index.html`
    * Error document: `error.html`
7. In the Permissions tab paste in the following CORS configuration then click save.
```
    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
```
8. In the Permissions tab go to the Bucket policy section and click the Edit button. Click the Policy Generator button to create a new security policy. Select/enter the following:
    * Policy Type: S3 Bucket Policy
    * Principal: *
    * Actions: GetObject
    * ARN: Copy the ARN from the Bucket Policy tab and paste here.
    * Click Add Statement then Generate Policy.
    * Copy the new policy and paste into the Bucket Policy editor.
    * To allow access to all resources add a "/*" onto the end of the Resource key value.
    * Save the new policy.
9. In the Permissions tab go to the Access Control section and click the Edit button. On the "Everyone (public access)" line check the List checkbox and click Save changes.
10. Go back to the services and select Identity and Access Management (IAM) to add a new user. Use the search bar if IAM isn't listed. IAM will be used to create new group, create an access policy giving the group access to the S3 bucket and to assign a user to the group so they can use the policy to access the files in the S3 bucket.
11. Under User Groups click the Create Group button. Enter a group name then scroll to the bottom and click Create group.
12. Under Policies click the Create Policy button. Follow the steps below:
    * Go to the JSON tab and select Import managed policy.
    * Search for the `AmazonS3FullAccess` policy and Import this.
    * From the S3 Bucket Policy page copy the ARN and paste this twice into the Resource key as shown below:
    ```
        "Resource": [
            "arn:aws:s3:::s3-bucket-name",
            "arn:aws:s3:::s3--bucket-name/*"
        ]
    ```
13. Click the Review Policy button giving the policy a name and description. Click the Create Policy button to save all changes.
14. Under User Groups select the group that was created above. On the Permissions tab select Attach Policies from the Add permissions dropdown menu. Search for the policy that was created above, select it and click the Add permissions button.
15. Under Users click the Add Users button and give the user a name. Check the Access Key - Programmatic access option and click next. On the next page add the user to the new group that was created above. Click through to the end then click Create User.
16. Download the CSV file - this contains the user access key and secret access key which will be used by the Django app for authentication. Save the file in a secure location as this cannot be downloaded again once the user has been created.
17. To connect Django to the new S3 Bucket two new packages are required: boto3 and django-storages. In Gitpod type the following commands to install the packages:
    * `pip3 install boto3`
    * `pip3 install django-storages`
18. Freeze the requirements by running command `pip3 freeze > requirements.txt`.
19. In the settings.py file add 'storages' to the INSTALLED_APPS list.
20. Add the following configuration to the settings.py file. As the S3 Bucket is only required when using Heroku an if statement is used to check if the variable USE_AWS exists. 
```
    if 'USE_AWS' in os.environ:
        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'bucket-name'
        AWS_S3_REGION_NAME = 'eu-west-2'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```
21. In Heroku at the following Config Vars to the app. The AWS keys can be found in the csv file that was downloaded when creating the S3 user. The DISABLE_COLLECTSTATIC can also be removed as Heroku will get the static files from AWS for any future deploys.
    * `AWS_ACCESS_KEY_ID : From the csv file`
    * `AWS_SECRET_ACCESS_KEY : From the csv file`
    * `USE_AWS : True`
    * Remove variable `DISABLE_COLLECTSTATIC`
22. In the settings.py file add the following inside the USE_AWS if statement to tell Django where the static files will be sourced from in production.
    * `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'`
23. The next step is to configure Django to use S3 to store our static files whenever someone runs `collectstatic` and to also store any uploaded images in the S3 bucket.
24. In the root folder create a file by running `touch custom_storages.py`.
25. Copy the following configuration into the file and save:
```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
```
26. In the settings.py file add the following inside the USE_AWS if statement to configure Django to use our custom storage class for static file storage and to override the static and media URLs in production.
```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
27. In the settings.py add the following lines to the top of the USE_AWS if statement. These will configure the browser to cache static files for a long time as they don't change often.
```
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```
28. At this point all the changes can be committed to Github triggering Heroku to deploy the app. Confirm all the static files have been uploaded to the S3 bucket.
29. To add the media files to the S3 bucket go to AWS S3, select the bucket and click on Create folder. Create a folder called media.
30. Inside the media folder click Upload to upload all the media files to the S3 bucket. Under Permissions set the Predefined ACL to Grant public-read access.
31. The superuser email address for the Postgres database needs to be confirmed to allow the user to login to the application. To do this login to the Django admin panel and confirm the email address for the superuser by checking the Verified box.



### Stripe Configuration
1. Login to Stripe and in the Developers section click on API Keys. In Heroku add the publishable and secret keys as the following config variables.
    * `STRIPE_PUBLIC_KEY`
    * `STRIPE_SECRET_KEY`
2. Click on the Webhooks link in the Developers section. Click on Add Endpoint configure as follows:
    * `EndPoint URL: https://app-name.herokuapp.com/checkout/wh/`
    * Click receive all events in the Events to send section and click Add Endpoint.
3. On the webhook screen reveal the Signing Secret and copy this into Heroku as a config variable named `STRIPE_WH_SECRET`.
4. To confirm the webhook is working send a test webhook from Stripe to ensure the listener is working.



### Email Configuration
The following process assumes that GMail will be used for sending and receiving emails.
1. Open [GMail](https://gmail.com) in the browser and login creating a new account if required.
2. Open the account settings, select Accounts and Import and then other Google account settings.
3. Click on the Security tab and turn on 2-Step Verification under Signing in to Google.
4. Click Get Started and enter your Gmail password and then follow the 2-Step Verification as instructed.
5. Once the 2-Step Verification has completed go back to the Security tab and select App passwords under Signing in to Google.
6. On the App passwords screen select Mail for the app and other for the device giving it the name Django. Click Generate to complete.
7. Copy the password and create a new config variable in Heroku called `EMAIL_HOST_PASS` pasting in the password as the value.
8. Also create another config variable in Heroku called `EMAIL_HOST_USER` and set this to the Gmail account.
9. In settings.py add the following:
```
    if 'DEVELOPMENT' in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = 'app-name@example.com'
        EMAIL_SUBJECT_PREFIX = '[App-Name]'
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
        EMAIL_SUBJECT_PREFIX = '[App-Name]'
```
10. Confirm the email is functioning correctly by registering a new user and checking that the email confimration is received.


## Credits 

### Content 

* [Ireland Before you Die](https://www.irelandbeforeyoudie.com/five-irish-wines-you-must-try-before-you-die/) content 
and imagery was used from here for the blog post Irish Wine 2021. 

* [Super Valu](https://supervalu.ie/) imagery and notes were used for the wine content on this website. 

### Code 

* [Code Institute](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment) Full Stack Frameworks with Django Project Botique Ado was followed and used to assist in the creation of this website. This was modified to fit in with the requirements of this website. 

* [Docs Django Project](https://docs.djangoproject.com/en/3.2/intro/tutorial01/) information was used here to assist in the creation of this project. 

* [You Tube](https://www.youtube.com/watch?v=_uwucNViakk) was used as a tool to help understand datasets on Kaggle.

* [You Tube](https://www.youtube.com/watch?v=hZrlh4qU4eQ) was used to assist in creating the blog section.

* [You Tube](https://www.youtube.com/watch?v=hZrlh4qU4eQ) was used to assist in creating a blog comments section. 


### Media 

* Photo by <a href="https://unsplash.com/@scottiewarman?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Scott Warman</a> on <a href="https://unsplash.com/s/photos/wine?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

* [Super Valu](https://supervalu.ie/) imagery and notes were used for the wine content on this website. 
  
  
### Other 

* [Tables Generator](https://www.tablesgenerator.com/markdown_tables) was used in the creation of the table for the User Stories. 

* <i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

### Acknowledgements 

* Thank you to the tutors at Code Institute for their support and guidance in the creation of this website.

* Thank you to the Code Institute Slack Community for their tips and assistance throughout the course of creating this game.

* A big thank you to my mentor Sandeep Aggarwal for his help throughout this project.




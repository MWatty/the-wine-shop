## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. 

### HTML

* Validated each individual page using, example screenshots below. 

* [Landing Page](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/Landing%20Page%20HTML%20Validation.png "Landing Page")

* [Add a Product](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/HTML%20Validation%20Add%20a%20Product.png "Add a Product")

* [Edit a Product](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/HTML%20Validation%20Edit%20a%20Product.png "Edit a Product")

### CSS 

* Results - No errors identified 

* [CSS1 Results](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/CSS%20Validation%201.png "CSS1 Results")

* [CSS2 Results](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/CSS%20Validation%202.png "CSS2 Results")

### JavaScript

* [JShint](https://jshint.com/)  was used to detect errors and potential problems within the JavaScript Code. There are no errors identfied with 
the exception of "template literal syntax" which is only availble in ES6. Please see a screenshot of an example of the results for this site below. 

* [J Shint Results](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/JS%20Validation.png "J Shint Results")

### Python

* [Extends Class](https://extendsclass.com/python-tester.html) - 

#### Bag  

1. admin.py
2. apps.py
3. contexts.py
4. models.py
5. tests.py
6. urls.py
7. views.py 1

#### Blogs 

1. admin.py
2. apps.py
3. forms.py
4. models.py
5. tests.py
6. urls.py
7. views.py 1

#### Checkout

1. admin.py
2. apps.py
3. forms.py 1
4. models.py 1
5. signals.py
6. tests.py
7. urls.py
8. views.py 1
9. webhooks_handler.py 1
10. webhooks.py

#### Home

1. admin.py
2. apps.py
3. models.py 
3. signals.py
5. tests.py
6. urls.py
7. views.py 

#### Products

1. admin.py
2. apps.py
3. models.py 
4. tests.py
5. urls.py
6. views.py 1
7. widgets.py

#### Profiles

1. admin.py
2. apps.py
3. forms.py 1
4. models.py 
5. tests.py
6. urls.py
7. views.py 1

#### The Wine Shop

1. asgi.py
2. settings.py 1
3. urls.py 
4. wsgi.py  


1. custom_storages.py
2. manage.py


### Further Testing

* The Website was tested on Google Chrome, Firefox, Opera Microsoft Edge and Safari browsers.
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.


#### Devices 

Tested the game functionality on the devices listed below: 

* Mac Book Pro 
* iPhone 11 
* Honor 10 
* Lenovo Laptop (Windows 10) 


#### Issues identified during testing 

##### Delete Comment 

* Identified that delete comments was not working during testing. 

*  Assessed the code and identified that the incorrect ID was being used.

* The ID was updated and the Delete comment is not operating as expected. 

##### Font Colour 

* Feeback from users noted that the font was difficult to read particularly on mobile devices. 

* Changes the weight and colour of lato to improve the user experience. 

* Following the change feedback from users is that the content is much easier to read.  

##### Webhooks 

* Identified that webhooks were failing when carrying out a purchase. 

* Carried out an assessment and identified that webhooks were working less than 48hrs before this issue was identified.
Checked changes to GitHub within this time and identified that the return response had been accidentially deleted. 

* Return response was added to the webhooks.py file, and webhooks are operating successfully. Please see screeshot below. 

[Webhooks](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/Webhook%20Success.png "Webhooks")

##### Email 

* Identified that when an order was placed the user was not receiving their order confirmation email. 

* As above, this was working less than 48hrs before testing, identified that the DEVFELOPMENT Config var
was running. 

* Removed the DEVELOPMENT Config Var and confirmed that email confirmation is operational. 

##### Individual Product Page 

* Edit and Delete should ideally be changed to icons in keeping with the other edit and delete icons throughout. 

### Features Tested 

#### Header / Navigation Bar

* Tested all links on the header navigation bar and all are working and leading the user to the expected location. 
* The search functionality is also worked as expected. 
* "The Wine Shop" link also works are allows users to return to the home page. 

#### Hero Image / Shop Now 

* The "Shop now" link is working as expected and takes the user to the All Products page.

#### Log In 

* Clicked on My Account, Login and was brought to the Log In screen correctly. 
* Entered incorrect details are was greeted with a message "The username and/or password you specified are not correct."
* Confirmed the signposting to the sign up page is working. "If you have not created an account yet, then please sign up first."
* Password reset functionality is working as expected. 
* Using account details that had been set up, log in worked successfully. 
* Message pop up received "Successfully signed in as maura84"
* Remember me also worked as intended. 

#### Registration 

* Clicked on My Account, Register and was brought to the Sign Up screen correctly. 
* As expected Sign Up working correctly when detials were entered. 
* Back to log in button redirected as expected. 
* "Already have an account? Then please sign in." This also worked as expected. 
* Verify account worked as expected and email was received to verify. 


#### Shopping Bag 

* Cliked on individual product and was taken as expected to the individual product page. 
* Increase and decreasing quantiy of the product was successful. 
* The keep shopping link redirected to the correct page. 
* For Superuser both the edit and delete functionality operated successfully. 
* When clicked Add to Bag, a pop up appeared showing the bad was updated with the details and product price. 
* Clicked on Shopping Bag icon in the top right corner as this directed me to the Shopping Bag as required. 
* Products available to view within the shopping bag. 
* Correct costs availabe to view on this page also. 
* Free Delivery notification contains the correct information.
* The option to update and remove products working as expected. 
* Message received for both update and remove advising action has been successful. 
* Keep shopping link redirects to the correct page. 
* Clicked on Secure Checkout and this redirected to the Checkout as expected. 

#### Checkout 

* Completed the checkout form with missing details and as expected received warnings. 
* Order summary available to view on the right hand side for desktop and on top for smaller devices. 
* Adjust bag directing to the correct page. 
* Incorrect card details entered and error message received. 
* Correct card details entered and payment successful. 

#### Order Confirmation 

* Onscreen order confirmation details correctly shown. 
* Confirmation email received. 
* Pop up message also recived. 
* "Maybe you should order some more!" button working and redirecting as expected. 

#### Stripe 

* Webhooks succeeded follwoing order. 

#### Product Management 

* Superuser, product management adding, editing and deleting products working successfully. 
* Messages appearing as expected.
* Logged in regular users cannot as expected access this feature. 

#### Blog Management 

* Superuser, blog management adding, editing and deleting products working successfully. 
* Messages appearing as expected.
* Logged in regular users could not access this feature. 

#### Comment Management 

* Superuser, comment managemnt adding, editing and deleting comments working successfully. 
* Messages appearing as expected.
* Logged in user had correct permissions to edit and delete their comments. 

#### Logout 

* Logout working successful and lead to the sign out screen which also works. 
* Messages appearing as expected.



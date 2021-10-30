## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. 

### HTML

* Validated each individual page using, example screenshots below. 

* [WC3 Markup Validation Serivce]()

* [WC3 Markup Validation Serivce]()

* [WC3 Markup Validation Serivce]()

### CSS 

* Results - No errors identified 

* [W3C CSS Validation Service](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/CSS%20Validation%201.png "CSS1")

* [W3C CSS Validation Service](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/CSS%20Validation%202.png "CSS2")

### JavaScript

* [JShint](https://jshint.com/)  was used to detect errors and potential problems within the JavaScript Code. There are no errors identfied with 
the exception of "template literal syntax" which is only availble in ES6. Please see a screenshot of an example of the results for this site below. 

* [J Shint]()

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



#### Devices 



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

### Features Tested 
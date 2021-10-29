## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. 

### HTML

* Validated code from "view page source" in Chrome. 


    1. Landing Page - 0 errors
    2. All Products - 0 errors
    3. Wines By price, Origin, Category, Red, White, Rose & Bubbles - 0 errors
    4. Blog & Comment - 0 errors
    5. Add New Blog - 0 errors
    6. Edit Blog - 0 errors
    7. Add Comment - 0 errors
    8. Edit Comment - 0 errors
    9. Edit Product - 1 errors  
    10. Add a Product - 1 errors 
    11. My Profile - 0 errors
    12. Individual Product Page - 0 errors
    13. Shopping Bag - 4 errors (Duplicate ID's)
    14. Checkout - 0 errors
    15. Order Confirmation - 0 errors 
    16. Sign Out Page - 0 errors 

* [WC3 Markup Validation Serivce]()


### CSS 

* Results - No errors identified 

* [W3C CSS Validation Service](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/CSS%20Validation%201.png "CSS1")

* [W3C CSS Validation Service](https://github.com/MWatty/the-wine-shop/blob/main/testing/testing_screenshots/CSS%20Validation%202.png "CSS2")

### JavaScript

* [JShint](https://jshint.com/)  was used to detect errors and potential problems within the JavaScript Code. There are no errors identfied with 
the exception of "template literal syntax" which is only availble in ES6.

### Python

* [PEP8](http://pep8online.com/checkresult) - 

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
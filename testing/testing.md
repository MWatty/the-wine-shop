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
## Testing 

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. 

### HTML

* Unclosed div and duplicate ID found on landing during validation of HTML, errors rectified. 

* [WC3 Markup Validation Serivce]()


### CSS 

* Results - No errors identified 

* [W3C CSS Validation Service]()

### JavaScript

JShint was used to detect errors and potential problems within the JavaScript Code. The only issues identified in JShint as per 
the results below related to the use of 'let' which are is available in ES6, this is not a cause for concern. 

* [JShint](https://jshint.com/) - [

### Python

* [PEP8](http://pep8online.com/checkresult) - 

### Further Testing



#### Devices 



#### Issues identified during testing 

* Delete Comment functionality within the Blog Posts was not working, after checking through code there 
was an error blog id was being used instead of comment id. 

* Font color was too light and some users adivsed it was difficult to read therefore changes the colour to black to 
improve the user experience. 

##### Webhooks 

* Identified that webhooks were failing when carrying out a purchase. 

* Carried out an assessment and identified that webhooks were working less than 48hrs before this issue was identified.
Checked changes to GitHub within this time and identified that the return response had been accidentially deleted. 

* Return response was added to the webhooks.py file, and webhooks are operating successfully. Please see screeshot below. 

ADD SCREENSHOT

### Features Tested 
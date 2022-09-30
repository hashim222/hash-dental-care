## Testings

* ## This project was tested manually several times throughout develepment.

    Access✅
    No Access❌ 
    * ## Guest user's testings 
    * ### All these functionalities have been tested for a guest users, and they work fine.
        * User's have access to Home Page✅
        * In the Home page user's can click the `Book Appointment` button to make an appointment❌
        * User's have access to Treatments page✅
        * To make an appointment, users can click the treatment they are interested in on the Treatments page❌
        * User's have access to Contact Us page✅
        * Users's have access to Manage Booking Page❌
        * By filling out the form, users can contact us✅
        * User's have access to login/register page✅
        * User's Have access to logout page❌

    * ## Logged In user's testings 
    * ### All these functionalities have been tested for a Logged In users, and they work fine.
        * User's have access to Home Page✅
        * In the Home page user's can click the `Book Appointment` button to make an appointment✅
        * User's have access to Treatments page✅
        * To make an appointment, users can click the treatment they are interested in on the Treatments page✅
        * User's have access to Contact Us page✅
        * Users's have access to Manage Booking Page✅
        * Despite not having booked an appointment yet, users can see their appointments on the manage booking page❌
        * manage booking page allows users to update and delete their appointments even if they have not yet booked any appointments yet❌
        * By filling out the form, users can contact us✅
        * User's have access to login/register page❌
        * User's Have access to logout page✅    


    * ### Due to a problem with the PEP8 Python code validator, I have to rely on Pylint which was installed in my project. So there is a problems section in the terminal that will display any errors that needs to be fixing, so it was very easy to use.
        ![pylint problem in the terminal](static/images/readme-file-images/pylint-problems.png)

    * Even after fixing many of the small pylint errors and warnings, some related to built-in Django code that I couldn't fix.  
        * booking_app app
            ![booking app pylint errors](/static/images/readme-file-images/booking_app-pylint-errors.png)

        * contact app
            ![contact app pylint errors](/static/images/readme-file-images/contact-pylint-errors.png)

        * treatments app
            ![treatments app pylint errors](/static/images/readme-file-images/treatments-pylint-errors.png)

* ### Html Code Validator
    * All the HTML pages code ran through [html code validator](https://validator.w3.org/#validate_by_input) individually and there were no issues found.     

* ### CSS Code Validator
    * All the CSS code ran through using [css code validator](https://jigsaw.w3.org/css-validator/#validate_by_input) and there were no issue found.
        ![css code validator](/static/images/readme-file-images/css-code-validator.png)

* ### Javascript Code Validator
    * Using [jshint](https://jshint.com/), I ran my jquery/javascript code and found no errors.  


* ## Lighthouse Check
    All the pages were run through using Google's lighthouse.
    Best practice and performance were the main reasons for the low score.  
    I tried to fix the security vulnerability issue by signing into [SNYK](https://security.snyk.io/package/npm/moment). However, it failed to find any issues, so I just noted it in the readme file.
        ![security vulnerability issue](/static/images/readme-file-images/best-practice-error.png) 
        ![snyk app](/static/images/readme-file-images/vulnerable-check-up.png)


    * ### Home Page

        * Desktop  
            ![desktop home page image](/static/images/readme-file-images/desktop-home-page.png)

        * Mobile  
            ![mobile home page image](/static/images/readme-file-images/mobile-home-page.png)

    * ### Treatments Page

        * Desktop  
            ![desktop treatments page image](/static/images/readme-file-images/desktop-treatments-page.png)  

        * Mobile  
            ![mobile treatments page image](/static/images/readme-file-images/mobile-treatments-page.png)
    
    * ### Book Appointment Page

        * Desktop  
            ![desktop booking page image](/static/images/readme-file-images/desktop-booking-page.png)  

        * Mobile  
            ![mobile booking page image](/static/images/readme-file-images/mobile-booking-page.png)  

    * ### Contact Us Page  

        * Desktop  
            ![desktop contact page image](/static/images/readme-file-images/desktop-contact-page.png)  

        * Mobile  
            ![mobile contact page image](/static/images/readme-file-images/mobile-contact-page.png)

    * ### Manage Booking  

        * Desktop  
            ![desktop manage booking page image](/static/images/readme-file-images/desktop-manage-booking-page.png)  

        * Mobile  
            ![mobile manage booking page image](/static/images/readme-file-images/mobile-manage-booking-page.png)
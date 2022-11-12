### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
> Key differences between Javascript and Python are that while Python is more versatile on the back end especially in scientific applications, JS allows for both front-end and back-end functionality allowing for direct user interation and server application in web development. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
> Two ways I'd look for missing keys would be to either create a if else statement where if the key exists, my function would return the key, else, return something like "Key Not Found". Another method that I think would work would be using get. Similarly, if the key exists, it'll print the key and if not, it'll return a different response rather than an error. Both shouldn't return any errors or cause the program to crash. 

- What is a unit test?  
> A unit test is a test that is created in order to test a small function or portion of code.

- What is an integration test?  
> An integration test tests groups of developed units into one connected, integrated test. 

- What is the role of web application framework, like Flask?  
> Flask is a web framework that allows developers to develop their web projects better, faster, and overall more efficiently. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
> Personally, if there is any type of search function with a data set, I'd utilize a URL query parameter since the = will define the search based off of the given parameter. If anything is routed to a new page, I'd use a route URL instead.  

- How do you collect data from a URL placeholder parameter using Flask?  
> With Flask, you can use request.args.

- How do you collect data from the query string using Flask?  
> You can use a request query string function using Flask.

- How do you collect data from the body of the request using Flask?  
> With Flask, you can use request.form and request the specific key. 

- What is a cookie and what kinds of things are they commonly used for?  
> Cookies are small pieces of data that are created as a user interacts with a program. Cookies remember user preferences and cater to users as the program is intended to.

- What is the session object in Flask?  
> The session object in Flask are keys and associated values that are created during a session to track data. Within each session, on the client-side, these keys and values are stored until the session is cleared.

- What does Flask's `jsonify()` do?  
> jsonify returns a useable response object from JSON rather than just a string of JSON data. This allows us to receieve an object vs a string in which we can impliment directly into our code. 
# springbard homework

## Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is a serverside coding language, while JavaScript is a browser read language

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
 `.get('c')` or `if 'c' in dictionary.keys():`
- What is a unit test?
A unit test seeks to validate the functionality of on piece of the program, usually a signle function or view

- What is an integration test?
An integration test seeks to test the functionality of the whole program by looking at the interconnectability of each piece to its connected pieces

- What is the role of web application framework, like Flask?
Flask streamlines the the repetitive processes like requests and redirects as well as adding functionality like templating and sessions

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
common convention is that for more permanent web spaces like a specific product for an ecomm company would warrant a url path, while variations like size and color would be better served with a query parameter
- How do you collect data from a URL placeholder parameter using Flask?
add the contents of `<placeholder>` *placeholder* to the view functions arguments like `def view_func(placeholder)` so then placeholder acts like a string variable for whatever was in the url placeholder
- How do you collect data from the query string using Flask?
`request.args["query_param"]` or `request.args.get("query_param")` would pull value from `/someurl?query_param=value` as a string to be assigned to a variable
- How do you collect data from the body of the request using Flask?
`request.form["key"]` would pull the data for key from the form with input name equal to key
- What is a cookie and what kinds of things are they commonly used for?
cookies make the browser statefull by sending information to the server that are specific to the client or user. What this means is a shopping cart can be saved or settings for user preferences once logged in.
- What is the session object in Flask?
session is built on cookies, that flask gives us as an easier way to create stateful content in the browser as long as the browser is open
- What does Flask's `jsonify()` do?
`jsonify()` formats data as JSON to send toa browser
- What was the hardest part of this past week for you?
getting the logic behond the unit tests right. Testing a simple function like adder is not bad, but it took a lot of refactoring to get working tests
  What was the most interesting?
getting into cookies and session was the most interesting for me. I've been with an ecommerce company for several years now and I was always curious how our email software would get abandoned cart information for those emails

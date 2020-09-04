### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - Python is more object-oriented than JavaScript and uses indentation to define blocks. Python also raises errors in many instances where JavaScript would not, such as when an index is out of range.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  - Use `.get()` instead of bracket notation or use an `if...in` statement to check if the key is in the dictionary

- What is a unit test?
  - A unit test tests a single piece of code, like a function.

- What is an integration test?
  - An integration test tests how different pieces of code work together.

- What is the role of web application framework, like Flask?
  - Web application frameworks streamline the "conversation" between the browswer and the server, making it easier and less tedious to write the code for requests and responses, and in the case of Flask, allows us to use templating.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - Routes should be for information that is related to the page as a whole, while query params would be for pieces of information that are used by the page.
  
- How do you collect data from a URL placeholder parameter using Flask?
  - Use angle brackets when you write the route, e.g., `@app.route('/<data>')`

- How do you collect data from the query string using Flask?
  - Get it from `request.args`

- How do you collect data from the body of the request using Flask?
  - Get it from `request.form`

- What is a cookie and what kinds of things are they commonly used for?
  - Cookies are pieces of data stored locally in the browser, commonly used store information for/about the user that will be needed repeatedly.

- What is the session object in Flask?
  - The session object is a data structure stored as an encoded cookie that can contain many smaller pieces of data that would otherwise be stored as individual cookies.

- What does Flask's `jsonify()` do?
  - It signals that a response is being sent as JSON.

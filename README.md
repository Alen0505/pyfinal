Hello there. This is my final project for Python subject.
In this project, I made a "Valorant" website, which uses flask and db.
First, lets check "main.py" file.

![image](https://github.com/Alen0505/pyfinal/assets/131423741/133b3aca-9901-47db-a184-59504fb247dc)

This piece of code represents a small web application built on Flask, enabling interaction with a SQLite database to store email addresses. 

Library Imports:

Flask: Used for creating and configuring the web application.
render_template: To render HTML templates.
request: Allows handling data sent by the client.
SQLAlchemy: ORM (Object-Relational Mapping) for database operations in Flask.

And, we have App Configuration, Definition of Data Model, Creating Tables and Route '/' (index) here.

![image](https://github.com/Alen0505/pyfinal/assets/131423741/b674903a-dbeb-445c-90f2-00a7eaef04c1)

This code defines several routes in a Flask application:

/skins route: Renders the skins.html template when accessed.

/maps route: Renders the maps.html template when accessed.

/support route: Handles both GET and POST requests. If a POST request is received (indicating form submission), it retrieves the user's email from the form data. It checks if the email already exists in the database using SQLAlchemy. If the email doesn't exist, it creates a new Email object and adds it to the database.

At the end of the script:

The create_tables() function is called to create necessary tables in the database.
The Flask application is run with debug mode enabled.

Then, lets quickly review the rest of the project.

![image](https://github.com/Alen0505/pyfinal/assets/131423741/437e7b1d-a782-41f4-bf2b-6de85110c05c)

It's a basic layout featuring information about the game, its characters, and recent updates. The news section highlights key additions or events in Valorant, providing a glimpse into the latest developments for interested visitors.

![image](https://github.com/Alen0505/pyfinal/assets/131423741/89f608bc-dacb-49e0-b94c-ee7eb3205c96)

This HTML code structures a page dedicated to Valorant maps. The HTML layout utilizes a clean structure with sections dedicated to each map, presenting relevant details and descriptions. The embedded styles define the appearance of the map information bundles, arranging images and text to create a visually appealing and informative layout for each map.

![image](https://github.com/Alen0505/pyfinal/assets/131423741/1b262cd6-7738-4118-8c46-d42b42fc772e)

This HTML code represents a webpage dedicated to skins in the game Valorant. The HTML markup creates a well-structured page that delivers information about three distinct skin bundles available in Valorant. Embedded styles define the appearance of elements on the page to ensure consistency and readability of the content.

![image](https://github.com/Alen0505/pyfinal/assets/131423741/14540eb3-fb3d-4b74-a01f-17b26b5ba0af)

This HTML code creates a simple support/contact form webpage. The HTML structure offers a straightforward contact form for users to submit their email addresses for support or inquiries. The embedded styles define the appearance of the form fields, aligning with the overall design and layout of the webpage.

In general, the whole project is based on saving email data of site visitors.






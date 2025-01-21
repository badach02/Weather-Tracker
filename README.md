# Daniel Badach Final Project CIS119

**Description:**
Pull the weather using API and given coordinates to generate a 7 day forecast from the current date
that gives temperature min/max, UV index max, precipitation chance max.
____

**Plan:** 
Using tkinter, make a window that instructs the user to enter coordinates. Create a class that makes a tkinter window.
In the class, setup the windows title, an entry label, a text label describing how to use, and a button that will generate 
the weather report. Use the button to call a function that will pull from open-meteo API that will grab the necessary weather information.
Iterate over each day in the given response to make a tkinter frame for each day that will have an individual label for each weather aspect.
Allow the user to enter another coordinate if wanted, so clear the frame that contains the weather report each call.
____
**Test cases:**
Given in the program is the coordinates for Erie, Pennsylvania.
In test cases, I tried Orlando, Florida and New York City, New York Coordinates.
NYC: 40.7128,-74.0060
Orlando: 28.5384,-81.3789
____
**Future additions:**
Add the ability to search for specific cities. I'm sure there is a library that has coordinates of majors cities.
Start the forecast from Sunday rather than the first day.


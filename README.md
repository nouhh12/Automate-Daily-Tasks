                                    Automate Daily Tasks

The script automates some of my daily tasks by means of an audible weather report and access to certain files and websites.

Firstly, the script goes to the location of the Spotify app on my computer and runs it to allow me to play music.

During the wait period of the Spotify app opening up, an audible weather report is played to make use of the waitihg time. 
Selenium Webdriver is used to run Google Chrome in order to get the current weather by searching on “Google.com”. Once the page loads with all the weather data, the information - Temperature, Humidity, Precipitation, Wind Speed - is stored in variables. Those variables are then pasted in the text box found on the website “TTSreader.com” where the play button is then clicked so that the gathered data about the weather can be played out loud.

Finally, the Selenium Webdriver opens Microsoft Outlook’s webpage where the email and password of user are sent to so that the user can sign in into his email account to view the inbox.
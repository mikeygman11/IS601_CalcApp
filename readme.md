Michael Galanaugh
HW 4

Faker, Generating test data, and adding your package to command line app.
For this homework. what you need to do is add the following features to your own calculator project:

Add the "faker" libary with the command "pip install faker" and then do a pip freeze > requirements.txt. Tip: First Deactivate the virtual environment with the command "deactivate" and then activate it again This is so that you will only add faker to the requirements and that your virtual environent is the current one that your working on when faker is installed. Review the faker website here. Once you add the library you need to update your tests to use the fake data. Do a basic implementation first and understand how it works. Review the faker library documentation, its important that you learn how faker works because it's an invaluable tool for development.

Add a new command to pytest to generate N number of records, so that you can run the following command: pytest --num_records=100 to generate 100 records. The code to do this is in the tests/conftest.py file and is a little complicated but ask ChatGPT, or me and study it a bit. Basically what happens is that records are generated and in the background the parameters for a,b,operation, expected result are created and there is a special method to generate test data that is automaticly called when these variables are passed in, so it just keeps calling the test function to test it. You kinda just need to have a leap of faith that its going to work, since the pytest library is doing all the work in the background.

Add a main.py file to serve as an entry point to your program and add the code from my main.py, so that you can have some exception handling to your program. Review the code in main.py to see how exceptions are caught when bad input is submitted by the user of your program.

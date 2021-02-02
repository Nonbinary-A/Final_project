# Final_project

This project is an application used to manage the workers of a company.

The workers are stored in a mySQL database, including their salary, department, etc.
The data is displayed in a HTML and in JSON format, using Django framework and Django restframework.

In addition, there is an external app - not connected to the database, which uses the API data to calculate the average salary.
The app returns a file with all the workers who work more than a year in the company, and their salary is below the average.

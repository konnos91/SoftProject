The exercise is divided into two parts:

The first part is the server:

The user has to go into the app folder open a terminal and run the following python programs:
	->python sq.py     -> it creates the database which is called todo.db
	->python server.py -> it starts the server (bottle framework)

The second part is the Ember.js front-end framework

The user has to download the file and open a new terminal to start the project
	->The command to start the project is: ember serve --proxy http://localhost:8080 (attach the server) avoid issues and errors

Finally the system will show the home page on the screen. The system offers some basic features such as:
	->Manage tab: Display all the students in the database file
	->New student: it creates new student entry into the system
	->Graph student: it creates the student’s general average per Quarter
		note: to use this feature the user must give the suitable id for the student
			For example: http://localhost:4200/statistic/1
	—>Subject Average: it produce the subject average for the three subjects(MATH,IT,LITERACTURE)
	—>Quarter:it creates the average of a specific Quarter and Year for example: Quarter 1 for the 2001 year

End and Enjoy!!!

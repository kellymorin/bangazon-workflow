# Bangazon-Workflow

## Installation
- Create an empty directory to house your new project
- run `virtualenv env` to create a virtual environment within that directory
- run `source env/bin/activate` to initialize a virtual environment (`deactivate` to exit environment)
- run `git clone [repository id]`
- run `cd bangazon-workflow`
- run `pip install -r requirements.txt`

## Seed a Starter Database
- Run `python manage.py makemigrations agileHR`
- Run `python manage.py migrate`
- If you want some data to play with, run `python manage.py seeder`
- Then run `python manage.py training_seeder`
- Initialize the project using the command line by typing `python manage.py runserver` in the main directory.
- Access the application in a browser at `http://localhost:8000/bangazon`.
- A navbar at the top of the page can be used to visit each of Bangazon's four Human Resources focus areas (employees, departments, trainings, and computers).

## Employees
- Employees can be accessed via the navbar. A list of all Employees and their departments is visible.
- Clicking <em>New Employee</em> will open a form that prompts the user to create a new employee including full name, department, whether or not they are a supervisor, and start date. Submitting the form will take the user back to the Employee page and will display a success message.
- Clicking on an employee will take the user to the employee detail page, where the user can see the employee's department, assigned computer, and assigned training sessions.
- Clicking <em>Edit Employee</em> will open a form with pre-populated data for that employee-- from there the user can edit any of the employee details.
- On that edit form, the user can assign a new/different computer to an employee. If the employee already has a computer listed, assigning a new computer will unassign the employee's current computer.
- The edit form also shows all upcoming trainings for the employee-- these can be deleted by clicking the delete checkboxes for any desired removals, and will be deleted upon submit.
- Finally, the user can add new training programs for the employee by selecting all desired trainings from the given options-- to select multiple, use ctrl+click for windows and cmd+click for mac.
- After making all edits to employee data, data will be updated upon submit and the user will be taken back to the employee page with a success message

## Departments
- Departments can be accessed via the navbar. A list of all departments' titles, budgets, and sizes (number of assigned employees) is visible.
- Clicking on a department will display a list of all assigned employees' names. The user can return to the departments list by clicking <em>Go Back</em>
- Clicking <em>Add a New Department</em> will open a form that prompts the user to submit a new department name and budget. Saving the form data will return the user to the list of departments. The user can find the department in the list alphabetically.
- Alternatively, the user can click <em>Go Back</em> to return to the departments list without saving new data.

## Trainings
- Training sessions can be accessed via the navbar. A list of all training sessions' titles and start date is visible.
- Clicking <em>Add New Training</em> will open a form that prompts the user to submit a new training session title, start and end date and maximum number of attendees. Saving the session will return the user to the list of training sesssions. The user can find their training session in the list sorted by date.
- Alternatively, the user can click <em>Go Back</em> to return to the training session list without saving new data.
- Clicking on a training session will display the training sessions title, start and end date, maximum number of attendees, available seats as well as a list of all employees that are currently registered for that session. The user can return to the training session list by clicking <em>View all Training Sessions</em>.
- The user can click <em>Edit Details</em> button to be taken to a form that allows the user to edit the details of the training session. Upon saving the session, the user will be returned to the updated training session detail page where their changes will be displayed.
- Alternatively, the user can select <em>Go Back</em> to return to the training session list without saving changes.
- From the training session list, if the user scrolls to the bottom and selects <em>View Past Programs</em>, they will be taken to a list of all training sessions with end dates prior to today, clicking on a training session will display the training sessions title, start and end date, maximum number of attendees and a list of all employees that attended that session. The user can return to the training session list by clicking <em>View All Training Sessions</em>


## Computers

## Summary
- Installation Steps
  - Execute 'dbScript.sql' that contains database and table schema used in the project
  - Modify connection details in Import_To_DB.py to use your mssql server
  - Run command 'pip install requirements.txt' (Make sure python is already installed on your system)

- How to run code
  - Run command 'bash import.sh capterra feed-products/capterra.yaml' in command prompt for capterra
  - Run command 'bash import.sh softwareadvice feed-products/softwareadvice.json' in command prompt for softwareadvice

- If I had more time
  - Used environment variables for connectors etc
  - Included better exception handling
  - Cleaned the data properly to import better
  - Covered all the boundary cases that might fail
  - Learned more sh scripting and implemented the whole process using that right now I have used python

* * * 

## SaaS Products Import

We update our inventory of SaaS products from several sources.  Each source provides its content to us in a different format.  Write a command line script to import the products.

Input/output should be something like this:
 
````bash
$ import capterra feed-products/capterra.yaml

importing: Name: "GitHub";  Categories: Bugs & Issue Tracking, Development Tools; Twitter: @github
importing: Name: "Slack"; Categories: Instant Messaging & Chat, Web Collaboration, Productivity; Twitter: @slackhq
````

Considerations:

- Currently, we are importing products from 2 sites: capterra and softwareadvice.  They send us their weekly feed via email.  This weeks files are in /feed-products
- We plan to add a third provider soon who will make their feed available via csv output online via a url (you don't need to implement this, just keep it mind)
- Do not implement any data persistence code, just provide some dummy classes that echo what they are doing.  Keep in mind that the company is planning to switch from MySQL to MongoDB in 3 months.
- The focus here should be on design, more than implementation.  We are less interested in seeing that this works than in seeing how you approach the problem.
- Please provide at least some unit tests (it is not required to write them for every class). Functional tests are also a plus.
- Please provide a short summary detailing anything you think is relevant, for example:
  - Installation steps
  - How to run your code / tests
  - Where to find your code
  - Was it your first time writing a unit test, using a particular framework, etc?
  - What would you have done differently if you had had more time
  - Etc.
* * * 

## Code Submission

As a result of this assignment we expect to recieve a link to your shared git repository (i.e. Bitbucket or Gitlab offer free private repos).
Having full commit history is optional but would be considered as a plus.

# AutomationChallenge
Exercise 2.

#Prerequisites#

1. Latest Python version installed download from here: https://www.python.org/downloads/.
2. Pycharm IDE installed.
3. install unittest in Pycharm terminal as: pip install unittest2 if required.

#Set up from tar.gz file#
1. Navigate to File and unzip project folder 
2. Install the project using pip by running:

   `pip install /path/to/your_project_name-version.tar.gz`

3. Replace /path/to/your_project_name-version.tar.gz with the actual path to your distribution package.

#Set up from cloning repository#
1. Clone repository from gitHub https://github.com/CesarCSC/AutomationPractice.git.

#Usage#
1. Set up Python interpreter in Pycharm File->Settings->Project->Python Interpreter more information: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html.
 
      1.1. Select Python interpreter from drop down list.
  
2. Install selenium and webdriver-manager if required from File->Settings->Project->Python Interpreter. 
  
      1.1. Click on plus icon and search for selenium then install package.
 
      1.2. Do the above step for webdriver-manager, both should be displayed in the package installed list.
 
3. Navigate to Run/ Debug configurations and add an unittest configuration with name 'test_Search.py' and target folder as ...testCases/test_Search.py. 
  
      1.1. Select Python interpreter as default one. Click on Apply and Ok.

4. Navigate to file test_ContactUsForm.py located under testCases folder and right click over it to Run unittest.

 
 





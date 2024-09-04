#### Exploring automation using Python with Selenium

This is a simple demo project for exploring Python + Selenium Automation Testing (with a little exploration into Behave testing framework).  The project folder structure and packaging is pretty rough I would say, and not yet following best practices.  But if you just need a base code to get a quick demo on how Python with Selenium works, this project should work for you.  You will need to download Python, Visual Studio Code, other python related libraries, and selenium web drivers.

I have elected to use "The Perth Mint" website as the site for testing.
As of current time, we are only testing one feature which is searching for a product from the home page.
The testing will not require log-in so as other users of this project could also try out running the code.

#### PREREQUISITES
1) Install Python
    https://www.python.org/downloads/
    You will also need to set Python in your system environment variables > Path
2) Install IDE (e.g. Visual Studio Code, Pycharm)
    Visual Studio Code > https://code.visualstudio.com/
        NOTE : If you will explore Behave, it seems it is easier to use Pycharm, but I opted to use Visual Studio Code
3) Install Selenium libraries
    You could check your Python related libraries that are already installed
        pip list
    Then you could install selenium : https://selenium-python.readthedocs.io/installation.html
        pip install selenium
4) Download web drivers (e.g. chromedriver.exe, geckodriver.exe)
5) If you will explore the Page Factory implementation. Install Selenium Page Factory (optional).
    pip install selenium-page-factory
6) If you will explore Behave. Install Behave (optional)
    To install behave : https://behave.readthedocs.io/en/stable/install.html
    pip install behave
        NOTE : For Behave exploration, I installed "Cucumber (Gherkin) Full Support". No other extensions were installed

#### HOW TO RUN
A) Exploring Python with Selenium only
    You could focus on stand alone file jd_python_selenium_example.py
    Open Terminal
    Then type in: python jd_python_selenium_example.py
B) Exploring Python with Selenium (implementing Page Factory)
    You could focus on the pages folder and its contents + jd_pagefactory_example.py
    Open Terminal
    Then type in: python jd_pagefactory_example.py 
C) Exploring Python with Selenium (implementing Behave)
    You could focus on the features folder and its contents
    Open Terminal
    Then type in: behave features\product_search.feature

#### REFERENCES
BDD feature file writing :
    https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/

Behave :
    https://medium.com/@moraneus/pythons-behave-framework-essential-tips-and-tricks-for-efficient-testing-faa89469d41c

Behave Youtube Tutorial:
    https://www.youtube.com/watch?v=JIyvAFBx2Fw&list=PLUDwpEzHYYLsARXz1o3Ldt1FnvRbvlxsS&index=2

TO BE EXPLORED - NOT APPLIED ON CURRENT PROJECT : Additional setup for Visual Studio Code and Behave 
    https://stackoverflow.com/questions/52725150/how-to-debug-behave-bdd-scenario-using-python-debugger-and-visual-studio-code

    https://spurqlabs.com/using-visual-studio-code-for-behave-bdd-tests-in-python/
    
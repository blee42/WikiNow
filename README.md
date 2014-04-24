README file for {{ project_name }}

###USAGE

Create a new Django project using this template:

    django-admin.py startproject --template=https://github.com/NUKnightLab/django-project-template/archive/master.zip <project_name>

Delete this USAGE section after creating the project. The remainder of this
README is for the created project.


###REQUIREMENTS

[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)


###DEVELOPMENT
    
    # Change into project directory
    cd <project_name>
    
    # Make virtual environment
    mkvirtualenv <project_name>
    
    # Activate virtual environment
    workon <project_name>
    
    # Install requirements
    pip install -r requirements.txt
    
    # Setup
    python manage.py syncdb
    
    # Start the development server
    python manage.py runserver
    






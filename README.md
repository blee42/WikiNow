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
    cd wikinow
    
    # Make virtual environment
	(source "/usr/local/bin/virtualenvwrapper.sh") 
	mkvirtualenv wikinow
    
    # Activate virtual environment
    workon wikinow
    
    # Install requirements
    pip install -r requirements.txt
    
    # Setup
    python manage.py syncdb
    
    # Start the development server
    python manage.py runserver
    






 #!/bin/bash
source "/usr/local/bin/virtualenvwrapper.sh"
mkvirtualenv wikinow
workon wikinow
python manage.py runserver

## [WikiNow](http://testwikinow.herokuapp.com/) - What's happening on Wikipedia
WikiNow builds a "front page" for Wikipedia. It shows trending articles on Wikipedia. In the front page it will show a lead story, and some secondary stories, images and news links. There are also sidebars for downtrends and most visited pages. 

People can discover what is interesting to people on the internet, what is trending, what is dropping in popularity and stumble upon news articles that interests them. External news links can serve the purpose of showing the reason why a certain page is popular and the categories provide context as well. WikiNow is the news front page for the Wikipedia community.

We are using the Django framework to build our website. For basic design, we are using the “[blueline](http://blueline.knightlab.com/)” web style guide created by the [Knight Lab](http://knightlab.northwestern.edu/). We grabbed uptrends articles (daily, weekly, monthly), most visited articles (weekly), and downtrends articles (weekly) from [Wikitrends](http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html). The visual experience is enhanced with better images from Google, external news links, and category for each article. 

## Installation and Usage

  Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) first

    Download WikiNow source code
    $ git clone git@github.com:blee42/WikiNow.git

    Enter into project directory
    $ cd WikiNow

    Activate the virtual environment 
    $ mkvirtualenv env
    If prompt error:"-bash: mkvirtualenv: command not found"
    $ source "/usr/local/bin/virtualenvwrapper.sh"
    $ mkvirtualenv env

    Activate virtual environment
    $ source env/bin/activate

    Install requirements
    $ pip install -r requirements.txt

    Start the development server
    $ python manage.py runserver

## Authors
* [Rebecca Lai](https://github.com/kklai) - Journalism major, Junior, Medill School of Journalism
* [Brittany Lee](https://github.com/blee42) - Computer Science, Junior, McCormick School of Engineering
* [Yuchao Zhou](https://github.com/yuchaozh) - Computer Science, master, McCormick School of Engineering

## Acknowledgements
* [Johan Gunnarsson](http://johan.gunnarsson.name/) - Built the [Wikitrends](http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html) as our source data


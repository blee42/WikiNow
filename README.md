## [WikiNow](http://testwikinow.herokuapp.com/) - What's happening on Wikipedia
WikiNow builds a "front page" for Wikipedia. It shows trending articles on Wikipedia. In the front page it will show a lead story, and some secondary stories, images and news links. There are also sidebars for downtrends and most visited pages. 

People can discover what is interesting to people on the internet, what is trending, what is dropping in popularity and stumble upon news articles that interests them. External news links can serve the purpose of showing the reason why a certain page is popular and the categories provide context as well. WikiNow is the news front page for the Wikipedia community.

We are using the Django framework to build our website. For basic design, we are using the “[blueline](http://blueline.knightlab.com/)” web style guide created by the [Knight Lab](http://knightlab.northwestern.edu/). We grabbed uptrends articles (daily, weekly, monthly), most visited articles (weekly), and downtrends articles (weekly) from [Wikitrends](http://tools.wmflabs.org/wikitrends/english-uptrends-this-week.html). The visual experience is enhanced with better images from Google, external news links, and category for each article. 

## Installation and Usage

Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

	
Download WikiNow source code
```console
$ git clone git@github.com:blee42/WikiNow.git
```
Enter into project directory
```console
$ cd WikiNow
```
Activate the virtual environment
```console
$ (source "/usr/local/bin/virtualenvwrapper.sh") 
$ mkvirtualenv wikinow
```
Activate virtual environment
```console
$ workon wikinow
```    
Install requirements
```console
$ pip install -r requirements.txt
```    
Start the development server
```console
$ python manage.py runserver
```    






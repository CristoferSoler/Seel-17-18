# BSI@Django-Wiki project

This project uses django-wiki as external dependency. We are not going to develop inside the django-wiki core project. Follow these steps to install django-wiki

### Installation
Basically its this

    pip install wiki

If you are missing some dependencies, follow the "Pre-requisite: Pillow" and "Installing" in the [docs](http://django-wiki.readthedocs.io/en/master/installation.html)

### Development
All our code will go into a django application. You find it as a subfolder called "bsi".

To develop in our wiki each working group creates a new branch out of the branch "django-wiki". At least we need these two feature-branches:
* templates
* importer

### Errors

#### HTTPError root article missing
This error is simple. You need a root article to actually use the search.
For this you have to log in as a user. You can create a superuser (admin)
through the terminal. Just type in
    
    python manage.py createsuperuser

After that just run the server, log in and visit
    
    localhost:8000/wiki/
    
Here you can create a root article. Do that and you are good to go. Now you can
use every search bar :D 
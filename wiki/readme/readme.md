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


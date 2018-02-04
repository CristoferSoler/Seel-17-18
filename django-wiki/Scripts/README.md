### Run the importer locally  
##### Migrate the database in django-wiki directory
    sudo python manage.py makemigartions archive
    sudo python manage.py makemigartions bsi
    sudo python manage.py migrate
##### In Script directory    
1. For importing the articles i the database, in the Script directory run

        `sudo python bsiImporter.py`
    
2.  For test the update, in the Script directory run
    
    `sudo python bsiImporter.py --update ../../programming/bsiComparator/example_modified_files.txt`
    

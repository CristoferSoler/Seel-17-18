### Run the importer
##### append the cross reference tables to the db 
##### then go into Script folder
     create CRF and Cross_References_Files directories 
##### then     
     sudo python Cross_References.py
##### migrate the database in django-wiki directory
    sudo python manage.py makemigartions
    sudo python manage.py migrate
##### then go into Script folder
    sudo pyhton bsiImporter.py
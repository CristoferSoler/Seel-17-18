### Run the importer locally  
##### Append the cross reference tables to the db 
###### If not created
     create CRF and Cross_References_Files directories 
##### then     
     sudo python Cross_References.py
##### Migrate the database in django-wiki directory
    sudo python manage.py makemigartions bsi
    sudo python manage.py migrate
##### then go into Script folder
    sudo pyhton bsiImporter.py
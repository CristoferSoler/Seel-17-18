### Run the importer locally  
##### Migrate the database in django-wiki directory
    sudo python manage.py makemigartions archive
    sudo python manage.py makemigartions bsi
    sudo python manage.py migrate
##### In Script directory    
1.  Append the cross reference tables to the db, if not created 
     - create CRF and Cross_References_Files directories in the Script directory
     - then     
        `sudo python Cross_References.py`
2. For importing the articles i the database, in the Script directory run

        `sudo python bsiImporter.py`
    
3.  For test the update, in the Script directory run
    
    `sudo python bsiImporter.py --update ../../programming/bsiComparator/example_modified_files.txt`
    

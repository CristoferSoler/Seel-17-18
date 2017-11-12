import os 

def BSI_db_import():
BSI_description = []
file_description = []

for dirpath, dirnames, filenames in os.walk("C:/Users/Master/Desktop/BSI"):
    for filename in [f for f in filenames if f.endswith(".txt")]:
    #get the drive and the filepath
        drive, path_and_file = os.path.splitdrive(os.path.join(dirpath, filename))
    #get the path and file name
        location, file = os.path.split(path_and_file)
    #get the type of the file    
        if os.path.basename(location) == "C_MEASURE":
            action_type = 'CM'
        elif os.path.basename(location) == "COMPONENT":
             action_type = 'C'
        elif os.path.basename(location) == "THREAT":
            action_type = 'T'  
        else:  action_type = 'G' 
    #git the file id and the titel   
        file_name = os.path.splitext(file)[0]
        id  = file_name.split(" ", 1)[0]
        titel = file_name.split(" ", 1)[1]  
       
        file_description= [id, titel, location,action_type]
        BSI_description = BSI_description + [file_description]
        print(file_description, '\n')
    
#print(dirpath)
# print (os.path.join(dirpath, filename))

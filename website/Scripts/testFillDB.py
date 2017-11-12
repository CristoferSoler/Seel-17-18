import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        if conn == None:
            raise Exception("The database connection cannot be null at this point")
        
        return conn 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
 
def emptyTables(conn):
    try:
        # create a new cursor
        cur = conn.cursor()
        
        # delete tables content
        cur.execute("TRUNCATE model_role CASCADE;")
        cur.execute("DELETE FROM model_checking WHERE countermeasure_id='M 1.1';")
        cur.execute("DELETE FROM model_countermeasure WHERE id='M 1.1';")

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()
        print("Tables were emptied");

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertDummy(conn):
    try:
        role_names = ["Administrator", "User"]
        role_desc = ["The administrator can do almost everything :)", "The user cannot do a lot of things :)"]
        roles = (role_names, role_desc)

        cmeasure = ["M 1.1", "Compliance with relevant standards and regulations", "There are guidelines, standards or regulations for almost all areas of technology. These may have been issued by standardization organizations, industry associations, user groups or government institutions, eg. B. DIN (German Institute for Standardization), ISO (International Standards Organization), VDE (Association of Electrical Engineering, Electronics and Information Technology), VDMA (German Engineering Federation), VdS (Association of Property Insurers). These rules help ensure that technical equipment provides a sufficient level of protection for users and safety during operation. When planning and constructing buildings, during their operation and conversion, and when installing technical building equipment (eg internal supply networks such as telephone or data networks) and when purchasing and operating equipment, it is essential to comply with the relevant standards and regulations. The observance of standards is not a safety measure per se. It means that minimum requirements are met and the current state of the art and knowledge is respected."]

        checking = ["Are all relevant standards and regulations taken into account in the planning, construction and reconstruction of buildings and the installation of technical equipment?", "M 1.1"]
    
        # create a new cursor
        cur = conn.cursor()

        # execute INSERT statements
        cur.executemany("INSERT INTO model_role(name, description) VALUES (%s, %s);", roles)
        cur.execute("INSERT INTO model_countermeasure(id, name, description) VALUES (%s, %s, %s);", cmeasure)
        cur.execute("INSERT INTO model_checking(description, countermeasure_id) VALUES (%s, %s);", checking)

        # commit the changes to the database
        conn.commit()
    
        # close communication with the database
        cur.close()    
        print("Dummy data inserted")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
 
if __name__ == '__main__':
    try:
        conn = connect()
        emptyTables(conn)
        insertDummy(conn)
    finally:
        conn.close()

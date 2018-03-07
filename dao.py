import pyodbc


class DAO(object):

    driver = ''
    server = r'' 
    db = '' 
    usr = '' 
    pwd = '' 
    connection_string = '''DRIVER={0};
                        SERVER={1};
                        DATABASE={2};
                        UID={3};
                        PWD={4}'''.format(driver, server, db, usr, pwd)
    connection = None

    def __init__(self):
        pass

    def open_connection(self):
        try:
            DAO.connection = pyodbc.connect(DAO.connection_string)
            print("SUCCESS")
        except Exception as e:
            print("Error: " + str(e))


    def close_connection(self):
        DAO.connection.close()


    def is_pnr_blacklisted(self, pnr):
        
        cursor = DAO.connection.cursor()

        cursor.execute('''SELECT * FROM [dbo].[table] 
                        WHERE cprnr = {pnr}'''.format(pnr))

        row = cursor.fetchone()

        return row[0]

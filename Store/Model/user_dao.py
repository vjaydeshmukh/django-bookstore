from Store.Model.user import User 
from Store.Model.dbconfig import read_db_config
from Store.Model.abc_dao import AbcDao
from mysql.connector import MySQLConnection, Error

class UserDao(AbcDao):
    def create(self, p_user):
        try:
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = (p_user.password, p_user.is_superuser, p_user.username, p_user.first_name, p_user.last_name, p_user.email, p_user.is_staff,
                    p_user.is_active)
            cursor.callproc('createUser', args)
            conn.commit()

            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)

    def update(self, p_user):
        try:
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = (p_user.id, p_user.password, p_user.is_superuser, p_user.username, p_user.first_name, p_user.last_name, p_user.email, p_user.is_staff,
                    p_user.is_active)
            cursor.callproc('updateUser', args)
            conn.commit()

            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
    def delete(self, p_user):
        try:
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = (p_user.id)
            cursor.callproc('deleteUser', args)
            conn.commit()

            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
    def updateLastLogin(self,id):
        try:
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = [id]
            cursor.callproc('updateLastLogin', args)
            conn.commit()

            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
    def get_all(self):
        try:
            
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            
            
            cursor.callproc('getAllUsers')
            for result in cursor.stored_results():
                user = result.fetchall()
            users = []
            for x in user:
                u = User()
                u.id = x[0]
                u.password = x[1]
                u.last_login = x[2]
                u.is_superuser = x[3]
                u.username = x[4]
                u.first_name = x[5]
                u.last_name = x[6]
                u.email = x[7]
                u.is_staff = x[8]
                u.is_active = x[9]
                u.date_joined = x[10]
                users.append(u)
            conn.commit()
            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
        return users
    def get_byid(self, id):
        u = None
        try:
            
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            
            args = [id]
            cursor.callproc('getUserById', args)
            for result in cursor.stored_results():
                user = result.fetchall()

            for x in user:
                u = User()
                u.id = x[0]
                u.password = x[1]
                u.last_login = x[2]
                u.is_superuser = x[3]
                u.username = x[4]
                u.first_name = x[5]
                u.last_name = x[6]
                u.email = x[7]
                u.is_staff = x[8]
                u.is_active = x[9]
                u.date_joined = x[10]
               
            conn.commit()
            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
        return u
    def get_byusername(self,username):
        u = None
        try:
            
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            
            args = [username]
            cursor.callproc('getUserByUserName', args)
            for result in cursor.stored_results():
                user = result.fetchall()

            for x in user:
                u = User()
                u.id = x[0]
                u.password = x[1]
                u.last_login = x[2]
                u.is_superuser = x[3]
                u.username = x[4]
                u.first_name = x[5]
                u.last_name = x[6]
                u.email = x[7]
                u.is_staff = x[8]
                u.is_active = x[9]
                u.date_joined = x[10]
               
            conn.commit()
            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
        return u
    def updateUserPass(self,p_user):
        try:
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = (p_user.id, p_user.username,  p_user.password)
            cursor.callproc('updateUserPass', args)
            conn.commit()

            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
    def deactivateUser(self,id):
        try:
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = [id]
            cursor.callproc('deactivateUser', args)
            conn.commit()

            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
    def activateUser(self,id):
        try:
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = [id]
            cursor.callproc('activateUser', args)
            conn.commit()

            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
    
    def getAllNonStaffUsers(self):
        try:
            
            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            
            
            cursor.callproc('getAllNonStaffUsers')
            for result in cursor.stored_results():
                user = result.fetchall()
            users = []
            for x in user:
                u = User()
                u.id = x[0]
                u.password = x[1]
                u.last_login = x[2]
                u.is_superuser = x[3]
                u.username = x[4]
                u.first_name = x[5]
                u.last_name = x[6]
                u.email = x[7]
                u.is_staff = x[8]
                u.is_active = x[9]
                u.date_joined = x[10]
                users.append(u)
            conn.commit()
            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
        return users
    
    def getUsersByState(self):
        try:

            db_config = read_db_config()        
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            
            
            cursor.callproc('getCustomersByState')
            for result in cursor.stored_results():
                user = result.fetchall()
            users = []
            for x in user:
                u = User()
                u.id = x[0]
                u.password = x[1]
                u.last_login = x[2]
                u.is_superuser = x[3]
                u.username = x[4]
                u.first_name = x[5]
                u.last_name = x[6]
                u.email = x[7]
                u.is_staff = x[8]
                u.is_active = x[9]
                u.date_joined = x[10]
                u.state_code = x[11]
                users.append(u)
            conn.commit()
            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
        return users
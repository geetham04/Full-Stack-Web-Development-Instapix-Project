from .Model import Model
import sqlite3
import os
from datetime import datetime

DATABASE = 'Instagram_db'

class model_sqlite3(Model):
    
    def sign_up(self, user_input, file_key):
        """
        add a new row(user information) to the database with the provided user input
        :param conn: database connection object
        :param user_input: dictionary
        """

        # TODO: check if the user already exsits in the databse from the given user input
        # TODO: if user already present return error, else insert the new user information
        
        user_info = ''' INSERT INTO user_info(user_id, name, email, date_created, profile_photo)
                VALUES(?,?,?,?,?) '''
        user_credentials = ''' INSERT INTO user_credentials(user_id, password)
                VALUES(?,?) '''

        try:
            connection = sqlite3.connect(DATABASE)
            cur = connection.cursor()
            date_created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            cur.execute(user_info, (user_input["username"], user_input["name"], user_input["email"], date_created, file_key))
            cur.execute(user_credentials, (user_input["username"], user_input["password"]))
            connection.commit()
        except:
            print("db insert queries failed inside sign_up")
            connection.rollback()
        finally:
            connection.close()
# -------------------------------------------------------------------------------------------------------------------------------------

    def login(self, user_input):
        isVerified = False
        user_credentials = '''SELECT * FROM user_credentials WHERE user_id=? AND password=?'''
        
        try:
            connection = sqlite3.connect(DATABASE)
            cur = connection.cursor()

            cur.execute(user_credentials, (user_input["username"], user_input["password"]))
            user = cur.fetchall()

            if user:
                isVerified = True

                update_last_login = '''UPDATE user_credentials SET last_login=? WHERE user_id=? AND password=?'''
                last_login = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                cur.execute(update_last_login, (last_login, user_input["username"], user_input["password"]))
                connection.commit()
        except:
            print("db fetch queries failed inside login() method")
            connection.rollback()
        finally:
            connection.close()
        return isVerified

    def get_profile_photo(self, user_id):
        fetch_profile_photo = '''SELECT profile_photo FROM user_info WHERE user_id=?'''
        try:
            connection = sqlite3.connect(DATABASE)
            cur = connection.cursor()
            cur.execute(fetch_profile_photo, (user_id,))
            profile_photo = cur.fetchone()
        except:
            print("db fetch queries failed inside login() method")
        finally:
            connection.close()
        return profile_photo

# -----------------------------------------------------------------------------------------------------------------

    def get_suggested_followees(self, current_user):
        """
        read information of all user registeresd on the app
        :param conn: database connection object
        :param stores: list of tuples
        """
        
        # fetch_all_users = '''SELECT * FROM user_info WHERE user_id!=?'''
        # users = {}
        fetch_followees = '''SELECT * FROM user_info WHERE user_id!=? AND user_id NOT IN 
                                    (SELECT followee_id FROM user_follow WHERE user_id=?)'''
        try:
            connection = sqlite3.connect(DATABASE)
            cur = connection.cursor()
            cur.execute(fetch_followees, (current_user, current_user))
            users = cur.fetchall()
        except:
            print("db fetch queries failed inside get_suggested_followees()")
        finally:
            connection.close()
        return users
# -----------------------------------------------------------------------------------------------------------------

    def store_media_id(self, file_key):
        pass
# -----------------------------------------------------------------------------------------------------------------

    def store_media_metadata(self, file_key, user_id, description):
        media_metadata = '''INSERT INTO media_metadata(media_id, user_id, date_created, description)
                VALUES(?,?,?,?)'''
        try:
            connection = sqlite3.connect(DATABASE)
            cur = connection.cursor()
            date_created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            cur.execute(media_metadata, (file_key, user_id, date_created, description))
            connection.commit()
        except:
            print("db insert media_metadata queries failed")
            connection.rollback()
        finally:
            connection.close()
# -----------------------------------------------------------------------------------------------------------------

    def add_to_user_follow(self, follower, followee):
        user_follow = '''INSERT INTO user_follow(user_id, followee_id) 
                VALUES(?,?)'''
        try:
            connection = sqlite3.connect(DATABASE)
            cur = connection.cursor()
            cur.execute(user_follow, (follower, followee))
            connection.commit()
        except:
            print("db query failed inside add_to_user_follow().")
            connection.rollback()
        finally:
            connection.close()
# -----------------------------------------------------------------------------------------------------------------

    def get_all_followees(self, current_user):
        get_followees = '''SELECT * FROM user_follow WHERE user_id=?'''
        try:
            connection = sqlite3.connect(DATABASE)
            cur = connection.cursor()
            cur.execute(get_followees, (current_user,))
            followees = cur.fetchall()
        except:
            print("db query failed inside get_all_followees().")
            connection.rollback()
        finally:
            connection.close()
        return followees
# -----------------------------------------------------------------------------------------------------------------

    def get_media_metadata(self, user_id):
        get_metadata = '''SELECT * FROM media_metadata WHERE user_id=?'''
        try:
            connection = sqlite3.connect(DATABASE)
            cur = connection.cursor()
            cur.execute(get_metadata, (user_id,))
            metadata_list = cur.fetchall()
        except:
            print("db query failed inside get_media_metadata().")
            connection.rollback()
        finally:
            connection.close()
        return metadata_list
# -----------------------------------------------------------------------------------------------------------------

        


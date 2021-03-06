from Store.Model.abc_dao import AbcDao
from Store.Model.image import Image
from Store.Model.book import Book
from Store.Model.inventory import Inventory
from Store.Model.dbconfig import read_db_config
from mysql.connector import MySQLConnection, Error

class ImageDao(AbcDao):

    def create(self, image):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            
            args = (image.image_url, image.caption, image.book.book_id)
            cursor.callproc('createImage', args)

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
    
    def get_byid(self, book_id):
        images = []
        try:
            # Setup connection to the DB
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            # Calls the stored procedure
            cursor.callproc('getImageByBookID', (book_id,))         
            
            # This loop iterates through the resultsets
            for result in cursor.stored_results():
                # This loop iterates through the rows in each resultset
                for image_row in result.fetchall():
                    image = Image()
                    image.image_id = image_row[0]
                    image.image_url = image_row[1]
                    image.caption = image_row[2]
                    image.book.book_id = image_row[3]
                    images.append(image)

            # Close the connection to the DB
            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)

        return images

    def get_all(self, limit):
        images = []
        try:
            # Setup connection to the DB
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            # Calls the stored procedure
            cursor.callproc('getAllImages', (limit,))         
            
            # This loop iterates through the resultsets
            for result in cursor.stored_results():
                # This loop iterates through the rows in each resultset
                for image_row in result.fetchall():
                    image = Image()
                    image.image_id = image_row[0]
                    image.image_url = image_row[1]
                    image.caption = image_row[2]
                    image.book.book_id = image_row[3]
                    image.book.title = image_row[4]
                    image.book.inventory.retail_price = image_row[5]
                    image.book.inventory.quantity_ordered = image_row[6]
                    image.book.inventory.quantity_on_hand = image_row[7]
                    images.append(image)

            # Close the connection to the DB
            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)

        return images

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
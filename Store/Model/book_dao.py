from Store.Model.book import Book
from Store.Model.publisher import Publisher
from Store.Model.author import Author
from Store.Model.genre import Genre
from Store.Model.dbconfig import read_db_config
from Store.Model.abc_dao import AbcDao
from mysql.connector import MySQLConnection, Error

class BookDao(AbcDao):

    def create(self, b):

        args = (b.get_isbn13(),b.get_isbn10(), b.get_title(),b.get_copyRightDate(),
                b.get_type(),b.get_edition(),b.get_numberOfPages(),b.get_size(),b.get_weight(),
                b.get_image(),b.get_genre(),b.get_authorID(),b.get_publisherID())
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            cursor.callproc('createBook',args)

            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()


    def update(self, b):
        args = (b.get_bookID(), b.get_isbn13(), b.get_isbn10(), b.get_title(), b.get_copyRightDate(),
                b.get_type(), b.get_edition(), b.get_numberOfPages(), b.get_size(), b.get_weight(),
                b.get_image(), b.get_genre(), b.get_authorID(), b.get_publisherID())
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            cursor.callproc('updateBook', args)

            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def get_byid(self, book_id):    
        book = Book()
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = (book_id,)
            cursor.callproc('getBookByID', args)                
            # This gets the first resultset
            result = next(cursor.stored_results())
            # This gets the first row in the resultset
            book_row = result.fetchone()
            book.set_bookID(x[0])
            book.set_isbn13(x[1])
            book.set_isbn10(x[2])
            book.set_title(x[3])
            book.set_copyRightDate(x[4])
            book.set_type(x[5])
            book.set_edition(x[6])
            book.set_numberOfPages(x[7])
            book.set_size(x[8])
            book.set_weight(x[9])
            book.set_image(x[10])

            genre = Genre()
            genre.genre_id = x[11]
            genre.genre = x[17]
            author = Author()
            author.author_id = x[12]
            author.first_name = x[15]
            author.last_name = x[16]
            publisher = Publisher()
            publisher.publisher_id = x[13]
            publisher.company_name = x[14]
            book.set_genre(genre)
            book.set_author(author)
            book.set_publisher(publisher)

            cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)

        return book

    def get_all(self):
        allBooks = []
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            cursor.callproc('getAllBooks')            

            for result in cursor.stored_results():
                books = result.fetchall()

            for x in books:

                currentbook = Book()
                currentbook.set_bookID(x[0])
                currentbook.set_isbn13(x[1])
                currentbook.set_isbn10(x[2])
                currentbook.set_title(x[3])
                currentbook.set_copyRightDate(x[4])
                currentbook.set_type(x[5])
                currentbook.set_edition(x[6])
                currentbook.set_numberOfPages(x[7])
                currentbook.set_size(x[8])
                currentbook.set_weight(x[9])
                currentbook.set_image(x[10])

                genre = Genre()
                genre.genre_id = x[11]
                genre.genre = x[17]
                author = Author()
                author.author_id = x[12]
                author.first_name = x[15]
                author.last_name = x[16]
                publisher = Publisher()
                publisher.publisher_id = x[13]
                publisher.company_name = x[14]
                currentbook.set_genre(genre)
                currentbook.set_author(author)
                currentbook.set_publisher(publisher)

                allBooks.append(currentbook)

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
        return allBooks

    
    def getBooksByGenre(self, b):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            args = [b]
            cursor.callproc('getBooksByGenre', args)
            allBooks = []

            for result in cursor.stored_results():
                books = result.fetchall()

            for x in books:

                currentbook = Book()
                currentbook.set_bookID(x[2])
                currentbook.set_isbn13(x[3])
                currentbook.set_isbn10(x[4])
                currentbook.set_title(x[5])
                currentbook.set_copyRightDate(x[6])
                currentbook.set_type(x[7])
                currentbook.set_edition(x[8])
                currentbook.set_numberOfPages(x[9])
                currentbook.set_size(x[10])
                currentbook.set_weight(x[11])
                currentbook.set_image(x[12])
                currentbook.set_genre(x[13])
                currentbook.set_authorID(x[14])
                currentbook.set_publisherID(x[15])
                allBooks.append(currentbook)



            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
        return allBooks

    
    def getBooksByAuthor(self, b,c):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            args = [b,c]
            cursor.callproc('getBooksByAuthor', args)
            allBooks = []

            for result in cursor.stored_results():
                books = result.fetchall()

            for x in books:

                currentbook = Book()
                currentbook.set_bookID(x[3])
                currentbook.set_isbn13(x[4])
                currentbook.set_isbn10(x[5])
                currentbook.set_title(x[6])
                currentbook.set_copyRightDate(x[7])
                currentbook.set_type(x[8])
                currentbook.set_edition(x[9])
                currentbook.set_numberOfPages(x[10])
                currentbook.set_size(x[11])
                currentbook.set_weight(x[12])
                currentbook.set_image(x[13])
                currentbook.set_genre(x[14])
                currentbook.set_authorID(x[15])
                currentbook.set_publisherID(x[16])
                allBooks.append(currentbook)



            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
        return allBooks


    def getBookbyTitle(self, title):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()

            args = [title]

            cursor.callproc('getBookByTitle', args)

            for result in cursor.stored_results():
                books = result.fetchall()

            for x in cursor.stored_results():
                currentbook = Book()
                currentbook.set_bookID(x[0])
                currentbook.set_isbn13(x[1])
                currentbook.set_isbn10(x[2])
                currentbook.set_title(x[3])
                currentbook.set_copyRightDate(x[4])
                currentbook.set_type(x[5])
                currentbook.set_edition(x[6])
                currentbook.set_numberOfPages(x[7])
                currentbook.set_size(x[8])
                currentbook.set_weight(x[9])
                currentbook.set_image(x[10])
                currentbook.set_genre(x[11])
                currentbook.set_authorID(x[12])
                currentbook.set_publisherID(x[13])



            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
        return currentbook


    def searchBooks(python, b):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            args = [b]
            cursor.callproc('searchBooks', args)
            allBooks = []

            for result in cursor.stored_results():
                books = result.fetchall()

            for x in books:

                currentbook = Book()
                currentbook.set_bookID(x[0])
                currentbook.set_isbn13(x[1])
                currentbook.set_isbn10(x[2])
                currentbook.set_title(x[3])
                currentbook.set_copyRightDate(x[4])
                currentbook.set_type(x[5])
                currentbook.set_edition(x[6])
                currentbook.set_numberOfPages(x[7])
                currentbook.set_size(x[8])
                currentbook.set_weight(x[9])
                currentbook.set_image(x[10])
                currentbook.set_genre(x[11])
                currentbook.set_authorID(x[12])
                currentbook.set_publisherID(x[13])
                allBooks.append(currentbook)



            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
        return allBooks

    def delete(self, b):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            args = [b]
            cursor.callproc('deleteBook', args)

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()

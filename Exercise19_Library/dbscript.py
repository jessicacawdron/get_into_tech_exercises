# import sqlalchemy
# print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+pymysql://Library_Member:password@localhost/group_d_library", echo=False, future=True)

search = 'y'
while search != 'x':
    print("Welcome to the library search. Would you like to search books via genre or author?")
    searchtype = input("Please type g for genre, a for author: ")

    while searchtype not in ['g','a']:
        print("Sorry that is not a valid search.")
        searchtype = input("Please type g for genre, a for author: ")

    if searchtype == 'g':
        print("What genre of books would you like to search for?")
        print(""" 1 - Fantasy\n 2 - Sci-fi\n 3 - Travel\n 4 - Romance\n 5 - Biography\n 6 - Poetry\n 7 - Thriller
8 - Adventure\n 9 - Horror\n 10 - Historical\n 11 - Crime\n 12 - Cookery\n 13 - Travel
14 - Self-help\n 15 - Young Adult""")
        genre = int(input("Type the number relating to the genre you would like to view: "))
        with engine.connect() as conn:
            result = conn.execute(text(f"select book_title, author from books where genre_id = {genre};"))
            print("Books in your chosen genre:")
            for row in result:
                print(f" {row.book_title} by {row.author}")
    elif searchtype == 'a':
        author = input("Enter the author you would like to search for: ")
        with engine.connect() as conn:
            result = conn.execute(text(f"select book_title from books where author like :param;"), {"param": author})
            print("Books by ", author, ":")
            for row in result:
                print(f" Title: {row.book_title}")

    search = input("To search again type 'y' to exit type 'x' :")

# with engine.connect() as conn:
#     result = conn.execute(text("select book_title from books where genre_id = 11;"))
#     print("Crime Titles:")
#     for row in result:
#         print(f" {row.book_title}")

print("----------------------------------------------------------------------")

with engine.connect() as conn:
    result = conn.execute(text("select book_title, author, release_date from books order by release_date desc;"))
    print("Latest Releases:")
    for row in result:
        print(f"Title: {row.book_title}  Author: {row.author} Release Date: {row.release_date}")

print("----------------------------------------------------------------------")

with engine.connect() as conn:
    result = conn.execute(text("select book_title, author, release_date from books where class = 'electronic';"))
    print("Electronic Books available to you:")
    for row in result:
        print(f" {row.book_title}  Release Date: {row.release_date}")

print("----------------------------------------------------------------------")

engine = create_engine("mysql+pymysql://Library_Staff:password@localhost/group_d_library", echo=False, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select first_name, last_name, return_date from library_members inner join loans on library_members.id= loans.person_id where loan_status = 'not-returned';"))
    for row in result:
        print(f" {row.first_name} {row.last_name} Expected return date:{row.return_date}")

print("----------------------------------------------------------------------")

engine = create_engine("mysql+pymysql://Library_Council:password@localhost/group_d_library", echo=False, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select dob, user_cat, gender from personal_details;"))
    print("User Details")
    for row in result:
        print(f"DOB: {row.dob}   Membership Type: {row.user_cat}   Gender: {row.gender}")


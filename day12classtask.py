import re
book_title = input("Enter the Title of the Book")
publication_year = (input("Enter the Publication Year"))

try:
    if not re.fullmatch(r"[A-Za-z ]+",book_title):
        raise ValueError("There is no Book mathing to your search or try avoiding numbers")
    if not re.fullmatch(r"(19|20)\d{2}",publication_year):
        raise ValueError("The Year must start with either '19' or '20'")
except  ValueError as e:
    print(e)

else:
    print(f"The Book {book_title} published on {publication_year} is Aprooved")

finally:
    print("Thank You")
   
    
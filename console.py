import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("George Orwell")
author_repository.save(author1)
author2 = Author("George R. R. Martin")
author_repository.save(author2)

author_repository.select_all()

book_1 = Book("1984","A dystopian social science fiction novel ", author1, "Science fiction")
book_repository.save(book_1)

book_2 = Book("Game of Thrones", "A war for the throne", author2, "Fantasy")
book_repository.save(book_2)


pdb.set_trace()
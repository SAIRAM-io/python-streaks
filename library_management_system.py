''' Library Management system using OOPS '''

class Library:
    books = []
    def __init__(self, name, role):
        self.name = name
        self.role = role
        if role == 'student':
            self.book_bank = []

    def show_user(self):
        print('\nName: {}\nRole: {}\n'.format(self.name, self.role.capitalize()))

    def check_if_book_exists(self):
        pass

    def add_new_book(self, new_book):
        if self.role == 'librarian':
            Library.books.append(new_book)
        else:
            print('A student cannot add a new book to the library. Please contact librarian.')

    def remove_existing_book(self, book_id):
        if self.role == 'librarian':
            Library.books = list(filter(lambda book_dict: book_dict['book_id'] != book_id, Library.books))
        else:
            print('A student cannot remove book from the library. Please contact librarian.')

    def show_books(self, ):
        for ind, book_dict in enumerate(Library.books):
            print('\n{}. {}\nEdition: {}'.format(ind+1, book_dict['book_name'], book_dict['book_edition']))

    def show_issued_books(self):
        if len(self.book_bank)>0:
            print('Issued books...')
            for ind, book_dict in enumerate(self.book_bank):
                print('\n{}. {}\nEdition: {}'.format(ind+1, book_dict['book_name'], book_dict['book_edition']))
        else:
            print('You didnt issued any book...')

    def issue_book(self, book_id):
        if self.role == 'student':
            for book_dict in Library.books:
                if book_dict['book_id'] == book_id:
                    self.book_bank.append(book_dict)
                    return 1
            return 0
        return -1

    # def return_book(self, book_id):
    #     if self.role == 'student':
    #         for book_dict in self.book_bank:
    #             if book_dict['book_id'] == book_id:
    #                 self.book_bank.append(book_dict)
    #                 return 1
    #         return 0
    #     return -1

librarian = Library('Harsh', 'librarian')
new_book = {
    'book_id':  101,
    'book_name': 'Geometry',
    'book_edition': 2
}
librarian.add_new_book(new_book)
new_book = {
    'book_id':  102,
    'book_name': 'Science',
    'book_edition': 1
}
librarian.add_new_book(new_book)
new_book = {
    'book_id':  103,
    'book_name': 'Trignometry',
    'book_edition': 3
}
librarian.add_new_book(new_book)
new_book = {
    'book_id':  104,
    'book_name': 'History',
    'book_edition': 1
}
librarian.add_new_book(new_book)
new_book = {
    'book_id':  105,
    'book_name': 'Physics',
    'book_edition': 2
}
librarian.add_new_book(new_book)
print(Library.books)
print()

# librarian.remove_existing_book(102)
# print(Library.books)
# print()

stud_1 = Library('Raja', 'student')
print('Book bank: ', stud_1.book_bank)
stud_1.show_books()
is_issued = stud_1.issue_book(102)
if is_issued == 1:
    print('\nBook is issued...\n')
elif is_issued == 0:
    print('\nBook is not issued...\n')
else:
    print('\nOnly student can issue a book...\n')
stud_1.show_user()
stud_1.show_issued_books()
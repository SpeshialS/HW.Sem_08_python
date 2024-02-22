from func import *

books = None  
while True:
    entry_menu.show()
    answer = get_answer(entry_menu)
    books = manage_files(answer, books)
    if not books:
        break
BYTES_ONE_CHARS = 4
pages = 100
lines = 50
chars = 25
volume = 1.44
total_chars = pages * lines * chars
book_volume = BYTES_ONE_CHARS * total_chars
disk_size = volume * 1024 * 1024
num_books = disk_size // book_volume
print(f'Количество книг:', num_books)
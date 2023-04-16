#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

text = "This School is so cool!\n"
nb_characters_added = append_write("file_append.txt", text)
print(nb_characters_added)

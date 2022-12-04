#!/usr/bin/env python3

print("hello")

def read_line(line):
    line = line.strip()
    if not line:
        return
    if not line[0].isdigit():
        return
    if 'Not Available' in line:
        return

    line = line.replace(' ', '')
    columns = line.split(";")

    print(columns)


data = open("in.txt", "r")
for line in data:
    read_line(line)

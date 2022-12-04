#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print("usage: index_of_column")
    exit(1)

which_column=int(sys.argv[1])

our_element=[]

def read_line(line, our_element):
    line = line.strip()
    if not line:
        return
    if not line[0].isdigit():
        return
    if 'Not Available' in line:
        return

    line = line.replace(' ', '')
    line = line.replace(',', '.')
    columns = line.split(";")

    wavelength = columns[0]
    magic_element = float(columns[which_column])
    our_element.append(magic_element)


data = open("in.txt", "r")
for line in data:
    read_line(line, our_element)

plt.plot(our_element)
plt.ylabel('spectra')
plt.show()

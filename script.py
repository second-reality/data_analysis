#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

which_file=filedialog.askopenfilename()
which_column=tk.simpledialog.askinteger(title="", prompt='Which column do you want (starts at 1)')

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

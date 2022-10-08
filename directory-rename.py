# Python program to rename all file
# names in your directory
import os
from datetime import date, timedelta, datetime
import calendar

dir_path = input("Please enter path of directory: ")
os.chdir(dir_path)
folders = os.listdir()
print(folders)

folders.sort(key=lambda x: os.path.getmtime(x))
print(folders)

first_date = date(2022, 10, 1)
for count, f in enumerate(folders):
	directory_name = os.path.splitext(f)
	new_directory_name = (first_date + timedelta(days=count)).strftime('%d-%m-%y')

	if os.path.exists(new_directory_name):
		continue

	os.rename(f, new_directory_name)

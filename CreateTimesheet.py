import openpyxl
import datetime
from Config import *
import os

def ClearAllEntries():
    return

# Get the current date information
today = datetime.date.today()
CurrentWeek = datetime.datetime.now().isocalendar()[1]
CurrentYear = datetime.datetime.now().isocalendar()[0]
WeekStart = today - datetime.timedelta(days=today.weekday())
WeekEnd = WeekStart + datetime.timedelta(days=6)

# Create a new workbook
workbook = openpyxl.Workbook()

# Select the active worksheet
worksheet = workbook.active

# Add some data to the worksheet
worksheet['A1'] = 'Name'
worksheet['B1'] = 'Age'
worksheet['A2'] = 'John'
worksheet['B2'] = 30
worksheet['A3'] = 'Jane'
worksheet['B3'] = 25

# Save the workbook to disk
workbook.save('example.xlsx')

TimesheetFile = os.path.join("Timesheets", UserInitial + "_WE" + WeekEnd.strftime("%m-%d-%Y") + ".xlsx")

workbook.save(TimesheetFile)

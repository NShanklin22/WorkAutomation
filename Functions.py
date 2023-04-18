import json
import Config
import os
import datetime

DataPath = Config.DataPath

def CreateDateDataFile(Date, DateData):

    DateData = json.dumps(DateData)

    with open("{}.json".format(Date), "w") as json_file:
         json_file.write(DateData)

# Open the file in write mode to create it
def CreateDataFile(WeekDataPath, DataFile):
    filename = os.path.join(WeekDataPath,DataFile)
    with open(filename, "w") as f:
        f.write("Nate")

# Open data file in read + write mode
def OpenDataFile(WeekDataPath, DataFile):
    filename = os.path.join(WeekDataPath,DataFile)
    with open(filename, "r+") as f:
        # Create an empty dictionary
        GetUserInput(f)

# Get the user input and create a data entry
def GetUserInput(file):
    JobsWorked = input("How many jobs did you work on today? ")
    DateData = {}

    for i in range(int(JobsWorked)):
        JobNum = input("What is the job number for the {} job? ".format(get_place(i+1)))
        JobName = input("What is the name of the job? ")
        HoursWorked = input("How many hours did you spend on {}? ".format(JobName))
        DataEntry = dict(jobNum=JobNum, jobName=JobName, hoursWorked=HoursWorked)
        DateData[i + 1] = DataEntry

    DateData = json.dumps(DateData)

    file.write(DateData)

def CheckForDataDirectory():
    # Get the current date information
    today = datetime.date.today()
    CurrentWeek = datetime.datetime.now().isocalendar()[1]
    CurrentYear = datetime.datetime.now().isocalendar()[0]
    WeekStart = today - datetime.timedelta(days=today.weekday())
    WeekEnd = WeekStart + datetime.timedelta(days=6)

    print("Week {}: {} to {}".format(CurrentWeek, WeekStart.strftime("%m-%d-%Y"), WeekEnd.strftime("%m-%d-%Y")))

    # Define the name of the directory
    WeekDataPath = os.path.join(DataPath, "WE" + WeekEnd.strftime("%m-%d-%Y"))
    DataFile = today.strftime("%m-%d-%Y") + ".json"

    if os.path.exists(WeekDataPath):
        return [True,WeekDataPath]
    else:
        os.mkdir(directory)

def CheckDataFile():
    # Get the current date information
    today = datetime.date.today()
    CurrentWeek = datetime.datetime.now().isocalendar()[1]
    CurrentYear = datetime.datetime.now().isocalendar()[0]
    WeekStart = today - datetime.timedelta(days=today.weekday())
    WeekEnd = WeekStart + datetime.timedelta(days=6)

    print("Week {}: {} to {}".format(CurrentWeek, WeekStart.strftime("%m-%d-%Y"), WeekEnd.strftime("%m-%d-%Y")))

    # Define the name of the directory
    WeekDataPath = os.path.join(DataPath, "WE" + WeekEnd.strftime("%m-%d-%Y"))
    DataFile = today.strftime("%m-%d-%Y") + ".json"

    for i in range((today - WeekStart).days + 1):
        # Store the data date and file names
        DataDate = (WeekStart + datetime.timedelta(days=i)).strftime("%m-%d-%Y")
        DataDateFile = DataDate + ".json"
        # Check if the file exists
        if not (os.path.isfile(os.path.join(WeekDataPath, DataDateFile))):
            # if the file does not exist ask the user if they want to make one
            print("Data file for {} does not exist.".format(DataDate))
            # CreateFileReq = input("Would you like to create the file? (Y/N) ")
            # # If yes open a new file with the DataDateFile name otherwise curse at them
            # if (CreateFileReq == "Y"):
            #     CreateDataFile(WeekDataPath, DataDateFile)
            # else:
            #     print("Fuck you")

# Function to convert an integer to it's "place" equivelant
def get_place(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        last_digit = num % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    return str(num) + suffix
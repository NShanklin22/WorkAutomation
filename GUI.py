
# importing libraries
import random

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtGui import *
from PyQt5 import QtTest
from PyQt5.QtCore import *
from screeninfo import get_monitors
import os
from Functions import *

import time

current_file_path = os.getcwd()
path_to_exports = os.path.join(current_file_path, "exports")

HavelBlue = "#007474"
HavelBlueBackground = "#02c2c2"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.fname = ""
        self.Grade = 0

        ##############################
        ### Seting up the window #####
        ##############################
        # Determine the size of the PC window
        screen = get_monitors()[0]

        # Define the x and y size of the screen
        sizeX = int(screen.width/8)
        sizeY = int(screen.height/2)

        # Deine the location of the window so that it is at the center of the screen
        locX = int(sizeX/2)
        locY = int(sizeY/2)

        # Define the geometry of the window
        self.setGeometry(locX,locY,sizeX,sizeY)

        # Add a title
        self.setWindowTitle("Havel Paperwork Tool")

        self.setStyleSheet("background-color : {};".format(HavelBlueBackground))

        ##############################
        ## Setting up the menubar ####
        ##############################


        ##############################
        ## Setting up the layout #####
        ##############################

        # Create a vertical layout for the buttons
        ButtonLayout = QVBoxLayout()

        # Frame for app updates)
        my_frame01 = QFrame()
        my_frame01.setFrameShape(QFrame.StyledPanel)

        # FontSize stores the default font size for the window
        FontSize = 18
        LabelSeparation = int(FontSize * 2.0)

        # Add three vertical buttons with spacers between, before, and after them
        spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        load_database_button = QPushButton("Add Entry", clicked = self.CheckForDataDirectory)
        load_database_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        load_database_button.setStyleSheet("background-color : #007474; color: white; font-size: 24px;")

        spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        results_button = QPushButton("Update Entry")
        results_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        results_button.setStyleSheet("background-color : #007474; color: white; font-size: 24px;")

        spacer3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        analyze_database_button = QPushButton("Generate Timesheet")
        analyze_database_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        analyze_database_button.setStyleSheet("background-color : #007474; color: white; font-size: 24px;")

        spacer4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Add all items to the vertical layout
        ButtonLayout.addItem(spacer1)
        ButtonLayout.addWidget(load_database_button)
        ButtonLayout.addItem(spacer2)
        ButtonLayout.addWidget(results_button)
        ButtonLayout.addItem(spacer3)
        ButtonLayout.addWidget(analyze_database_button)
        ButtonLayout.addItem(spacer4)

        self.other_window = None

        self.setLayout(ButtonLayout)

        self.show()

    def CheckForDataDirectory(self):
            ReturnedValues = CheckForDataDirectory()
            WeekDataPath = ReturnedValues[1]
            print(ReturnedValues)
            if ReturnedValues[0]:
                self.NewEntryMessageBox(WeekDataPath)
            else:
                self.DirectoryCreatedMessageBox()

    def DirectoryCreatedMessageBox(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle('New Week Directory')
        msg_box.setText('No directory detect for current week, a new directory has been created')
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)
        button_reply = msg_box.exec_()

    def NewEntryMessageBox(self,WeekDataPath):
        # Get the current date information
        today = datetime.date.today()
        CurrentWeek = datetime.datetime.now().isocalendar()[1]
        CurrentYear = datetime.datetime.now().isocalendar()[0]
        WeekStart = today - datetime.timedelta(days=today.weekday())
        WeekEnd = WeekStart + datetime.timedelta(days=6)
        for i in range((today - WeekStart).days + 1):
            # Store the data date and file names
            DataDate = (WeekStart + datetime.timedelta(days=i)).strftime("%m-%d-%Y")
            DataDateFile = DataDate + ".json"
            # Check if the file exists, if not ask the user if they would like to make a new entry
            if not (os.path.isfile(os.path.join(WeekDataPath, DataDateFile))):
                msg_box = QMessageBox()
                msg_box.setWindowTitle('New Date Entry')
                msg_box.setText('No data was found for {},\n would you like to make a new entry?'.format(DataDate))
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg_box.setDefaultButton(QMessageBox.No)
                button_reply = msg_box.exec_()
                if button_reply == QMessageBox.Yes:
                    other_window = OtherWindow()
                    other_window.exec_()
            else:
                print("Existing Data for {}".format(DataDate))

class OtherWindow(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Create the input widgets
        self.job_num_input = QLineEdit()
        self.job_name_input = QLineEdit()
        self.hours_worked_input = QLineEdit()

        # Create the labels for the input widgets
        job_num_label = QLabel('Job Number:',self)
        job_name_label = QLabel('Job Name:')
        hours_worked_label = QLabel('Hours Worked:')

        # Create the "Save" button
        save_button = QPushButton('Save')
        save_button.clicked.connect(self.save_data)

        # Create the layout for the input widgets and labels
        input_layout = QVBoxLayout()
        input_layout.addWidget(job_num_label)
        input_layout.addWidget(self.job_num_input)
        input_layout.addWidget(job_name_label)
        input_layout.addWidget(self.job_name_input)
        input_layout.addWidget(hours_worked_label)
        input_layout.addWidget(self.hours_worked_input)
        input_layout.addWidget(save_button)

        # Create a widget to hold the input layout
        widget = QWidget()
        widget.setLayout(input_layout)

    def save_data(self):
        # Open a file dialog to choose a directory to save the file in
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        directory = file_dialog.getExistingDirectory(self, 'Select Directory')

        # Create a filename for the CSV file based on the job number
        filename = f'{self.job_num_input.text()}.csv'

        # Write the data to the CSV file
        with open(f'{directory}/{filename}', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Job Number', 'Job Name', 'Hours Worked'])
            writer.writerow([self.job_num_input.text(), self.job_name_input.text(), self.hours_worked_input.text()])

app = QApplication([])
mw = MainWindow()

# Run the app
app.exec_()
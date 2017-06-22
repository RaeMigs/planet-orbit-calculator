#!/usr/bin/env python3

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import solarcode

# Author: Rae M.
# 6/22/2017

# GUI for solarcode.py
# Uses orbitDays QLineEdit for user input instead of command line

class App(QApplication):

    def __init__(self):
        # Initialize the parent widget
        QApplication.__init__(self, sys.argv)

        # Set the application name
        self.setApplicationName("Planet Orbit Calculator")

        # Create the main window
        self.mainWindow = MainWindow()
        # Creates a linear gradient background
        self.pal = QPalette()
        self.grad = QLinearGradient(0, 0, 0, 500)
        self.grad.setColorAt(0.0, QColor(244, 244, 244))
        self.grad.setColorAt(1.0, QColor(201, 224, 243))
        self.pal.setBrush(QPalette.Window, QBrush(self.grad))
        self.mainWindow.setPalette(self.pal)
        # Show the main window
        self.mainWindow.show()


class MainWindow(QMainWindow):
    """This is the main GUI window.  This is what contains all the QWidgets seen in the application."""

    def __init__(self):

        # Initialize the parent widget
        QMainWindow.__init__(self)

        self.setWindowTitle("Planetary Orbit Calculator")

        # Set the size of the main window
        self.resize(500, 300)

        # Create a main widget object (the central widget)
        self.mainWidget = MainWidget()
        # close button functionality
        self.mainWidget.bclose.clicked.connect(self.close)

        #  Set the main widget object as the central widget of the main window
        self.setCentralWidget(self.mainWidget)

class MainWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        # Create the main layout and button layout
        self.mainLayout = QVBoxLayout(self)
        self.inputLayout = QHBoxLayout()
        self.boxLayout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Sunken)

        # Create a bold font
        self.boldFont = QFont()
        self.boldFont.setBold(True)

        # Label for orbitdays input
        self.inLabel = QLabel("Days in Orbit:")
        self.inLabel.setFont(self.boldFont)

        # Orbitdays input w/intValidator to prevent non-int characters
        self.orbitdays = QLineEdit()
        self.orbitdays.setValidator(QIntValidator(1,2147483647))
        self.orbitdays.setStyleSheet("border-radius: 2px;"
                                       "border: 1px solid #2F2F2F;")

        # Create TextEdit output for the ordays function
        self.orbitoutput = QTextEdit()
        self.orbitoutput.setReadOnly(True)
        self.orbitoutput.setStyleSheet("border-radius: 2px;"
                                       "border: 1px solid #2F2F2F;")

        # Create run and quit pushbuttons
        self.brun = QPushButton("Run")
        self.brun.setIcon(QIcon("go.png"))
        self.bclose = QPushButton("Close")
        self.bclose.setIcon(QIcon("power.png"))


        # Add layouts and widgets
        self.mainLayout.addLayout(self.inputLayout)
        self.inputLayout.addWidget(self.inLabel)
        self.inputLayout.addWidget(self.orbitdays)
        self.mainLayout.addStretch(0)
        self.mainLayout.addLayout(self.boxLayout)
        self.boxLayout.addWidget(self.orbitoutput)

        self.mainLayout.addStretch(0)

        self.mainLayout.addLayout(self.buttonLayout)

        # Add B-Run: when clicked(or when 'enter' is pressed while orbitdays is active), runs orbitCalc function
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(self.brun)
        self.brun.clicked.connect(self.orbitCalc)
        self.brun.setAutoDefault(True)
        self.orbitdays.returnPressed.connect(self.brun.click)
        self.buttonLayout.addWidget(self.bclose)

        # SolarSystem class from the solarcode File.
        self.solarsystem = solarcode.SolarSystem()


    def orbitCalc(self):
        """
        calls getNumOrbits method from SolarSystem class in solarcode.py
        input: orbitdays lineedit <int>
        output: orbitoutput textedit

        """
        result = str(self.solarsystem.getNumOrbits(int(self.orbitdays.text())))
        self.orbitoutput.setText(result)


def main():
    # Create the application
    app = App()
    sys.exit(app.exec_())


if (__name__ == "__main__"):
    main()

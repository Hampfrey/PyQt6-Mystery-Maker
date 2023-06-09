import sys
import random
import controller

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.names = ["null"]
        self.weights = [1] 
        self.position = 0
        self.setWindowTitle("Mystery Maker")

        # Create our Layouts
        layout_main = QVBoxLayout()

        # QLable Example
        lable_title = QLabel(" Mystery Maker ")
        font = lable_title.font()
        font.setPointSize(30)
        lable_title.setFont(font)
        lable_title.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)
        layout_main.addWidget(lable_title)

        # Line Edit
        self.input_name = QLineEdit("Name")
        layout_name = QVBoxLayout()
        layout_name.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                       Qt.AlignmentFlag.AlignTop)
        layout_name.addWidget(self.input_name)

        # Spin Box
        self.input_weight = QSpinBox()
        label_weight = QLabel("Weight")
        label_weight.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout_weight = QHBoxLayout()
        layout_weight.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_weight.addWidget(self.input_weight)
        layout_weight.addWidget(label_weight)

        # Curent
        self.output_current_name = QLabel("Name")
        self.output_current_weight = QLabel("Weight")
        self.output_position = QLabel(str(self.position))
        self.output_names_length = QLabel("Total : 0-" + str(len(self.names) - 1))
        layout_current = QHBoxLayout()
        layout_current.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_current.addWidget(self.output_current_name)
        layout_current.addWidget(self.output_current_weight)
        layout_current.addWidget(self.output_position)
        layout_current.addWidget(self.output_names_length)

        # Change Space Buttons
        self.input_left = QPushButton("Previous Character") 
        self.input_save = QPushButton("Save") 
        self.input_right = QPushButton("Next Character")
        self.input_new = QPushButton("New Character")

        # Change Space Functions
        self.input_left.clicked.connect(self.previous_character)
        self.input_save.clicked.connect(self.save)
        self.input_right.clicked.connect(self.next_character)
        self.input_new.clicked.connect(self.new_character)

        # Add to Layout
        layout_position = QHBoxLayout()
        layout_position.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_position.addWidget(self.input_left)
        layout_position.addWidget(self.input_save)
        layout_position.addWidget(self.input_right)
        layout_position.addWidget(self.input_new)

        # Get Character
        self.input_stage = QPushButton("Get Character")

        # Get Character Function
        self.input_stage.clicked.connect(self.stage)
        layout_stage = QHBoxLayout()
        layout_stage.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_stage.addWidget(self.input_stage)

        # Break
        label_format = QLabel("------------------------------ Output ------------------------------")
        label_format.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)
        layout_format = QVBoxLayout()
        layout_format.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                       Qt.AlignmentFlag.AlignTop)
        layout_format.addWidget(label_format)

        # Ouptut
        self.output_names = QLabel()
        self.output_names.setAlignment(Qt.AlignmentFlag.AlignLeft | 
                                 Qt.AlignmentFlag.AlignTop)
        layout_ouput = QVBoxLayout()
        layout_ouput.setAlignment(Qt.AlignmentFlag.AlignLeft | 
                                       Qt.AlignmentFlag.AlignTop)
        layout_ouput.addWidget(self.output_names)

        # Add to vertical layout
        layout_main.addLayout(layout_name)
        layout_main.addLayout(layout_weight)
        layout_main.addLayout(layout_current)
        layout_main.addLayout(layout_position)
        layout_main.addLayout(layout_stage)
        layout_main.addLayout(layout_format)
        layout_main.addLayout(layout_ouput)

        # Set the main layout
        gui = QWidget()
        gui.setLayout(layout_main)
        self.setCentralWidget(gui)

    def save(self):
        """Save to current positon"""
        # Get Variables
        saving_name = self.input_name.text()
        saving_weight = self.input_weight.value()

        # Print details
        print(saving_name)
        print(saving_weight)
        self.output_names.setText(f"Saved name [{saving_name}] with weight [{saving_weight}] at positon [{self.position}]")

        # Save to arrays
        self.names[self.position] = saving_name
        self.weights[self.position] = saving_weight

        # Update
        self.update_labels()

    def update_labels(self):
        """Update Labels"""
        # Change
        self.output_position.setText(str(self.position))
        self.output_current_name.setText(str(self.names[self.position]))
        self.output_current_weight.setText(str(self.weights[self.position]))
        self.output_names_length.setText("Total : 0-" + str(len(self.names) - 1))
         
    def previous_character(self):
        """Move positon back one"""
        # Move
        self.position -= 1
        if self.position < 0:
            self.position = len(self.names) - 1
        self.update_labels()
    
    def next_character(self):
        """Move positon back one"""
        # Move
        self.position += 1
        if self.position > len(self.names) - 1:
            self.position = 0

        print(self.names)
        self.update_labels()

    def new_character(self):
        """Add a new character"""
        self.names.append("null")
        self.weights.append(0)
        self.update_labels()

    def stage(self):
        """Get a new charcter"""
        # Define Variables
        total = 0
        ranges = []
        i = 0
        I = 0
        chosen = 0
        print("------")

        # Create the ranges
        while i < len(self.names):
            ranges.append(total)
            total += self.weights[i]
            i += 1
        print(ranges)
        print(total)

        # Get random
        rand = random.randint(1, total)
        print(str(rand) + "-R")
        while I < len(self.names):
            print(str(rand <= ranges[I]) + " " + str(I))
            if not(rand <= ranges[I]):
                chosen = I
            I += 1
        print(str(chosen) + "-C")
        print(self.names[chosen])

        # Display
        self.output_names.setText(self.names[chosen])

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
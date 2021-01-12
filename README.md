# Electronic-Chess-Board

Welcome to the Electronic Chess Board Project!


A Chess Board was created which detects moves made on the board, and displays them onto a Python Based GUI. Moves through the game are stored and are furtherly analyzed post match to improve tactics and detect avoidable mistakes for future games.



# Code Structure
- [Data Collection](https://github.com/BaselOmari/DigiBoard/blob/main/DataCollection.ino) [Arduino (C++)]: 
In this stage, data from the Hall Effect Sensors are collected using the Arduino and are printed onto the Serial to allow for the Data Organization Stage to take place

- [Serial Port Reader](https://github.com/BaselOmari/DigiBoard/blob/main/GUI%20%2B%20Serial%20Reader.py) [Python]: 
Data in this stage is read from the Serial Port

- [Data Organization](https://github.com/BaselOmari/DigiBoard/blob/main/DataOrganization.py) [Python]: 
Data Collected for each move is then organized using Python and are translated to chess notation

- [Chess Game GUI](https://github.com/BaselOmari/DigiBoard/blob/main/GUI%20%2B%20Serial%20Reader.py) [Python]: 
Moves documented in the Data Organization Stage are displayed onto the screen for viewers to observe


# Work left for future iterations:

- Post Match Analysis [Python]:
Moves made during match are analyzed using the Stockfish Chess Engine API

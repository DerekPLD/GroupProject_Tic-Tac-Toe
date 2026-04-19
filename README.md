🎮 Tic-Tac-Toe Game
A simple implementation of the classic Tic-Tac-Toe game in Python. This project demonstrates basic game logic, turn-based interaction, and win/draw detection, making it suitable for beginners learning programming fundamentals or user interaction design.

Two versions are provided:

Console-based version: Implemented with Python standard libraries, no external dependencies:
<img width="902" height="921" alt="image" src="https://github.com/user-attachments/assets/d9f5dbe4-6032-40ef-aeb2-8832e0ab4760" />

Graphical version: Implemented with pygame, offering a GUI-based experience:
<img width="1011" height="1059" alt="image" src="https://github.com/user-attachments/assets/80b4684d-270f-49f1-b5ca-ea8618b99991" />


1. Project Overview

1.1 Purpose
This project recreates the classic Tic-Tac-Toe game with two-player local gameplay (X vs O). It supports:

Real-time board updates

Player alternation of moves

Automatic win/draw detection

Game replay/reset functionality

1.2 Development Model
The project adopts the Waterfall Model, progressing through five sequential stages:

Requirement analysis

Code implementation

Functional testing

Documentation optimization

Project delivery

This ensures a structured and standardized development process.

1.3 Target Users
Beginners learning Python programming

Enthusiasts of classic casual mini-games

2. Development Plan
2.1 Process
Requirement Analysis – Define core functions (move validation, win/draw detection, restart).

Code Implementation – Build board display, input handling, win judgment, and game loop.

Functional Testing – Test gameplay, invalid inputs, win/draw scenarios.

Documentation – Write README.md and add code comments.

Delivery – Record demo video and publish on GitHub.

2.2 Team Responsibilities
Person 1: Core development (game logic, win/draw algorithms).

Person 2: UI design (enhancements beyond basic program).

Person 3: Testing & optimization (debugging, input validation).

CHAN HIOKIN: Documentation & delivery (README, demo video, GitHub repo).

2.3 Schedule
Requirement Analysis – 1 day

Code Writing – 1 day

UI Design – 1 day

Testing – 2 days

Documentation & Video – 1 day

2.4 Algorithm
Board stored as a list (console version) or grid of rectangles (pygame version).

Win detection by checking rows, columns, and diagonals.

Draw detection when board is full with no winner.

Input validation prevents invalid moves and crashes.

2.5 Current Progress
Two-player local gameplay (X vs O)

Automatic win/draw detection

Clear board UI (console & GUI)

Restart/reset functionality

2.6 Future Improvements
Add AI opponent (easy/hard modes).

Enhance GUI with animations and scoring.

Record match history and statistics.

3. Operating Environment & Usage
3.1 Environment
OS: Windows, macOS, Linux (cross-platform)

Python: 3.6+

Dependencies:

Console version: None (pure Python)

GUI version: pygame

3.2 Instructions
Clone or download the repository.

For console version:

bash
python tic_tac_toe.py
For GUI version:

bash
python tic_tac_toe_pygame.py
4. Demonstration Video
(Insert YouTube link here)

5. License & Declaration
This project was independently developed by the team for the Software Engineering course assignment (COMP2116).

No external open-source code was used.

All algorithms, code, and documentation were created by the team.

pygame is declared as the only external library dependency.





<<<<<<< HEAD
# Theme Park Navigation System

## Project Overview
This project implements a theme park navigation system that helps visitors explore and navigate through the Habib University Theme Park. The system uses Dijkstra's algorithm to find the shortest paths between attractions and provides various features to enhance the visitor experience.

## Features

### 1. Tour Options
- **Complete Tour**: Start from the entrance and visit all attractions systematically
- **Custom Start**: Begin the tour from any location in the park

### 2. Navigation Features
- View all unvisited rides
- Find the nearest unvisited ride
- Find rides by type preference:
  - Kids
  - Thrill
  - Adventure
  - Water
  - Horror
  - Utilities

### 3. Path Finding
- Shows optimal paths between attractions using Dijkstra's algorithm
- Displays distance information
- Handles multiple equidistant options

## Ride Types
The park features various types of attractions:
- **Kids**: Family-friendly attractions (e.g., Arcade, Shrek)
- **Thrill**: High-excitement rides (e.g., Blinding Lights, Cylon)
- **Adventure**: Exploration-based attractions (e.g., XOChella, Fight Club)
- **Water**: Water-based rides (e.g., Bikini Bottom)
- **Horror**: Scary attractions (e.g., Screaming Sharky)
- **Utilities**: Service locations (e.g., Food Court, Bathrooms)

## Technical Implementation

### Data Structures
- Graph representation using adjacency lists
- Queue implementation for BFS traversal
- Dictionary-based data storage

### Algorithms
- **Dijkstra's Algorithm**: Used for finding shortest paths between attractions
- **Breadth-First Search**: Implemented for complete tour functionality

### Input Validation
- Numeric input validation
- Location input validation
- Ride type validation

## How to Use

1. Run the program:
```python
python projfile.py
```

2. Choose your tour type:
   - Enter 1 for Complete Tour (starts from entrance)
   - Enter 2 to start from a custom location

3. If you chose Complete Tour:
   - Follow the guided tour
   - Choose to continue (1) or exit (2) at each stop

4. If you chose Custom Start:
   - Enter your current location
   - Choose from available options:
     1. View all unvisited rides
     2. Find nearest unvisited ride
     3. Find nearest preferred ride type

5. For preferred rides:
   - Select a ride type
   - Choose from available rides of that type
   - Follow the suggested path

## Project Structure
- `projfile.py`: Main project file containing all functionality
- Data structures:
  - `nodes`: List of all locations
  - `rides_data`: Dictionary containing ride information
  - `Graph`: Adjacency list representation of the park layout

## Error Handling
- Invalid input handling for all user inputs
- Path validation
- Location verification
- Ride type validation

## Dependencies
- Python 3.x
- Standard libraries:
  - `math`: For infinity values in Dijkstra's algorithm

## Authors
- Umar Shaikh
- Habib University
- Data Structures and Algorithms Project
=======
# DSAproj

A backend algorithm written for a tour guide application of an imaginary amusement park. No work has been done on the UI yet, so the results are shown on the terminal.
The application provides the user with multiple options, i.e to start the tour from the entrance of the park, to begin the tour from a random position, guide the user
to the nearest ride, guide the tour to the nearest ride from the selected ride type, guide the user to nearest Bathrooms and utilities, guide the user to a specific ride
and etc etc. For all the options, algorithms with best time complexities have been used. The data structure used is an undirected graph and it uses algorithms like
BFS, DFS , Dijskttra's algorithm and so on.

The code can be easily run on any python compiler.
>>>>>>> 391ea0e719cb7c31e7ce729f5a365fa6f9ad5e0c

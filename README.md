# Theme Park Navigation System

## Project Overview
This project implements a theme park navigation system that helps visitors explore and navigate through the Habib University Theme Park. The system uses Dijkstra's algorithm to find the shortest paths between attractions and provides various features to enhance the visitor experience. The project includes both a command-line interface and a graphical user interface for better user interaction.

## Features

### 1. Graphical User Interface
- Interactive map visualization showing all rides and paths
- Color-coded nodes for different states:
  - Green: Current location
  - Blue: Unvisited rides
  - Gray: Visited rides
  - Light Gray: Utilities (bathrooms, food court)
- Distance labels showing actual distances between rides in meters
- Left panel for controls and ride selection
- List of visited rides
- Reset functionality

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
- Visual feedback for current location and visited rides

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
- NetworkX graph for visualization

### Algorithms
- **Dijkstra's Algorithm**: Used for finding shortest paths between attractions
- **Breadth-First Search**: Implemented for complete tour functionality

### Input Validation
- Numeric input validation
- Location input validation
- Ride type validation

## How to Use

### Graphical Interface
1. Run the GUI program:
```python
python gui.py
```

2. Use the interface:
   - View the map on the right panel
   - Use navigation buttons on the left panel
   - Select ride types from the dropdown
   - Track visited rides in the list
   - Reset tour when needed

### Command Line Interface
1. Run the command-line program:
```python
python projfile.py
```

2. Choose your tour type:
   - Enter 1 for Complete Tour (starts from entrance)
   - Enter 2 to start from a custom location

3. Follow the text-based prompts to navigate through the park

## Project Structure
- `gui.py`: Graphical user interface implementation
- `projfile.py`: Core functionality and command-line interface
- Data structures:
  - `nodes`: List of all locations
  - `rides_data`: Dictionary containing ride information
  - `Graph`: Adjacency list representation of the park layout

## Dependencies
- Python 3.x
- Required libraries:
  - `tkinter`: For GUI components
  - `matplotlib`: For visualization
  - `networkx`: For graph visualization
  - `math`: For infinity values in Dijkstra's algorithm



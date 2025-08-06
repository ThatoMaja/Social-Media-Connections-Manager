# Social Media Connections Manager

A Python-based application that simulates a basic **social network analysis** system using **graph theory**. Each user is represented as a node and friendships (connections) are represented as edges between nodes. This tool visualizes the structure of a network and helps discover patterns in user relationships.

---

## Features

**Add Users**  
**Add Connections** between existing users  
**View All Users** currently in the network  
**View All Connections** (friendships)  
**Visualize the Network Graphically** using `matplotlib`  
**Menu-driven Console Interface** that runs until the user exits

---

## OOP Structure

### `ConnectionsManager` Class  
Handles the core logic for managing users and connections.

**Methods:**
- `add_user(username)`
- `add_connection(user1, user2)`
- `view_all_users()`
- `view_all_connections()`
- `display_graph()`

### `MainMenu` Class  
Manages user interaction through a looping menu system.

**Menu Options:**
1. Add User  
2. Add Connection  
3. View All Users  
4. View All Connections  
5. Display Graph  
6. Exit

---

## Technologies Used

- **Python 3.x**
- **NetworkX** – for graph structures
- **Matplotlib** – for visualizing social graphs
- **OOP Principles** – to structure classes and methods

---

## How to Run

1. **Install Required Libraries**  
   ```bash
   pip install networkx matplotlib

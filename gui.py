import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from projfile import (
    nodes, rides_data, show_unvisited, dijkstra_for_desired, rideTypes,
    addnodes, my_graph
)

class ThemeParkGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Theme Park Navigation System")
        self.root.geometry("1200x800")
        
        # Initialize data
        self.current_location = "Entrance"
        self.visited = []
        
        # Create both graphs - one for visualization, one for pathfinding
        self.nx_graph = self.create_networkx_graph()
        self.graph = {}
        self.graph = addnodes(self.graph, nodes)
        self.graph = my_graph(self.graph, rides_data)
        
        # Create main frames
        self.create_frames()
        self.create_controls()
        self.create_map()
        self.update_status()

    def create_frames(self):
        # Left panel for controls
        self.control_frame = ttk.Frame(self.root, padding="10")
        self.control_frame.grid(row=0, column=0, sticky="nsew")
        
        # Right panel for map
        self.map_frame = ttk.Frame(self.root, padding="10")
        self.map_frame.grid(row=0, column=1, sticky="nsew")
        
        # Configure grid weights
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

    def create_controls(self):
        # Current Location
        ttk.Label(self.control_frame, text="Current Location:").grid(row=0, column=0, pady=5)
        self.location_label = ttk.Label(self.control_frame, text=self.current_location)
        self.location_label.grid(row=0, column=1, pady=5)
        
        # Navigation Options
        ttk.Label(self.control_frame, text="Navigation Options:").grid(row=1, column=0, columnspan=2, pady=10)
        
        # View All Unvisited Button
        ttk.Button(self.control_frame, text="View All Unvisited Rides", 
                  command=self.show_unvisited_rides).grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
        
        # Find Nearest Ride Button
        ttk.Button(self.control_frame, text="Find Nearest Unvisited Ride", 
                  command=self.find_nearest_ride).grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
        
        # Preferred Ride Type
        ttk.Label(self.control_frame, text="Preferred Ride Type:").grid(row=4, column=0, pady=5)
        self.ride_type_var = tk.StringVar()
        self.ride_type_combo = ttk.Combobox(self.control_frame, textvariable=self.ride_type_var, values=rideTypes)
        self.ride_type_combo.grid(row=4, column=1, pady=5, padx=5, sticky="ew")
        
        # Find Preferred Ride Button
        ttk.Button(self.control_frame, text="Find Preferred Ride", 
                  command=self.find_preferred_ride).grid(row=5, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
        
        # Visited Rides List
        ttk.Label(self.control_frame, text="Visited Rides:").grid(row=6, column=0, columnspan=2, pady=5)
        self.visited_listbox = tk.Listbox(self.control_frame, height=10)
        self.visited_listbox.grid(row=7, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
        
        # Reset Button
        ttk.Button(self.control_frame, text="Reset Tour", 
                  command=self.reset_tour).grid(row=8, column=0, columnspan=2, pady=20, padx=5, sticky="ew")

    def create_networkx_graph(self):
        G = nx.Graph()
        
        # Add nodes
        for node in nodes:
            G.add_node(node)
        
        # Add edges
        for node, data in rides_data.items():
            for neighbor, distance in data['neighbours']:
                G.add_edge(node, neighbor, weight=distance)
        
        return G

    def create_map(self):
        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.map_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.update_map()

    def update_map(self):
        self.ax.clear()
        
        # Create layout with fixed distances based on edge weights
        pos = nx.kamada_kawai_layout(self.nx_graph, weight='weight')
        
        # Draw edges with length labels
        edge_labels = {}
        for node, data in rides_data.items():
            for neighbor, distance in data['neighbours']:
                edge_labels[(node, neighbor)] = str(distance)
        
        # Draw edges first
        nx.draw_networkx_edges(self.nx_graph, pos, edge_color='gray', alpha=0.5)
        nx.draw_networkx_edge_labels(self.nx_graph, pos, edge_labels=edge_labels, font_size=6)
        
        # Color nodes based on type
        utility_nodes = [node for node in self.nx_graph.nodes() if rides_data[node]["ride_type"] == ["Utilities"]]
        ride_nodes = [node for node in self.nx_graph.nodes() if node not in utility_nodes 
                     and node != self.current_location 
                     and node not in self.visited]
        visited_nodes = [node for node in self.visited if node != self.current_location]
        
        # Draw nodes in correct order: utilities, unvisited, visited, and current location last
        nx.draw_networkx_nodes(self.nx_graph, pos, nodelist=utility_nodes, 
                             node_color='lightgray', node_size=300, alpha=0.7)
        nx.draw_networkx_nodes(self.nx_graph, pos, nodelist=ride_nodes,
                             node_color='lightblue', node_size=500)
        nx.draw_networkx_nodes(self.nx_graph, pos, nodelist=visited_nodes,
                             node_color='gray', node_size=500)
        # Draw current location last so it's always on top
        nx.draw_networkx_nodes(self.nx_graph, pos, nodelist=[self.current_location],
                             node_color='green', node_size=700)
        
        # Draw labels with better formatting
        nx.draw_networkx_labels(self.nx_graph, pos, font_size=8,
                              font_weight='bold')
        
        # Add a title and legend
        self.ax.set_title("Theme Park Map\nGreen: Current Location, Blue: Unvisited, Gray: Visited\nNumbers show distances in meters")
        
        # Remove axis
        plt.axis('off')
        
        # Adjust layout to prevent label overlap
        plt.tight_layout()
        
        self.canvas.draw()

    def update_status(self):
        self.location_label.config(text=self.current_location)
        self.visited_listbox.delete(0, tk.END)
        for ride in self.visited:
            self.visited_listbox.insert(tk.END, ride)
        self.update_map()
        
    def get_path_and_distance(self, start, end):
        try:
            path, distance = dijkstra_for_desired(self.graph, start, end)
            return path, distance
        except Exception as e:
            print(f"Error finding path: {e}")
            return None, float('inf')

    def show_unvisited_rides(self):
        unvisited = show_unvisited(self.visited, nodes)
        if not unvisited:
            messagebox.showinfo("Info", "All rides have been visited!")
            return
            
        ride = self.select_from_list("Select Ride", unvisited)
        if ride:
            try:
                path, distance = self.get_path_and_distance(self.current_location, ride)
                if path:
                    messagebox.showinfo("Path", 
                        f"Distance: {distance} meters\n\nFollow this path:\n{path}")
                    self.current_location = ride
                    if ride not in self.visited:
                        self.visited.append(ride)
                    self.update_status()
            except Exception as e:
                messagebox.showerror("Error", f"Could not find path: {str(e)}")

    def find_nearest_ride(self):
        unvisited = show_unvisited(self.visited, nodes)
        if not unvisited:
            messagebox.showinfo("Info", "All rides have been visited!")
            return
            
        nearest_rides = []
        min_cost = float('inf')
        
        for ride in unvisited:
            path, cost = self.get_path_and_distance(self.current_location, ride)
            if path and cost < min_cost:
                nearest_rides = [ride]
                min_cost = cost
            elif path and cost == min_cost:
                nearest_rides.append(ride)
        
        if not nearest_rides:
            messagebox.showerror("Error", "Could not find any reachable rides!")
            return
            
        ride = self.select_from_list("Select Nearest Ride", nearest_rides)
        if ride:
            path, distance = self.get_path_and_distance(self.current_location, ride)
            if path:
                messagebox.showinfo("Path", 
                    f"Distance: {distance} meters\n\nFollow this path:\n{path}")
                self.current_location = ride
                if ride not in self.visited:
                    self.visited.append(ride)
                self.update_status()

    def find_preferred_ride(self):
        preferred_type = self.ride_type_var.get()
        if not preferred_type:
            messagebox.showerror("Error", "Please select a ride type!")
            return
            
        preferred_rides = []
        unvisited = show_unvisited(self.visited, nodes)
        
        for ride in unvisited:
            if preferred_type in rides_data[ride]["ride_type"]:
                preferred_rides.append(ride)
        
        if not preferred_rides:
            messagebox.showinfo("Info", "No unvisited rides of this type!")
            return
            
        ride = self.select_from_list("Select Preferred Ride", preferred_rides)
        if ride:
            path, distance = self.get_path_and_distance(self.current_location, ride)
            if path:
                messagebox.showinfo("Path", 
                    f"Distance: {distance} meters\n\nFollow this path:\n{path}")
                self.current_location = ride
                if ride not in self.visited:
                    self.visited.append(ride)
                self.update_status()

    def select_from_list(self, title, items):
        select_window = tk.Toplevel(self.root)
        select_window.title(title)
        select_window.geometry("300x400")
        
        listbox = tk.Listbox(select_window)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for item in items:
            listbox.insert(tk.END, item)
        
        selected_item = [None]
        
        def on_select():
            selection = listbox.curselection()
            if selection:
                selected_item[0] = items[selection[0]]
                select_window.destroy()
        
        ttk.Button(select_window, text="Select", command=on_select).pack(pady=10)
        
        self.root.wait_window(select_window)
        return selected_item[0]

    def reset_tour(self):
        if messagebox.askyesno("Reset Tour", "Are you sure you want to reset the tour?"):
            self.current_location = "Entrance"
            self.visited = []
            self.update_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = ThemeParkGUI(root)
    root.mainloop()

import math
import pprint

# Helper function for validating numeric input
def get_numeric_input(prompt, valid_options=None):
    while True:
        try:
            value = int(input(prompt))
            if valid_options is None or value in valid_options:
                return value
            print(f"Invalid choice. Please choose from {valid_options}")
        except ValueError:
            print("Please enter a valid number.")

def get_location_input(prompt, valid_locations):
    while True:
        location = input(prompt)
        if location in valid_locations:
            return location
        print("Invalid location. Please try again.")

def get_ride_type_input(prompt, valid_types):
    while True:
        ride_type = input(prompt)
        if ride_type in valid_types:
            return ride_type
        print("Invalid ride type. Please try again.")

#DATA
nodes = [
    'Entrance',
    'Ticket Counter',
    'XOChella',
    'Vuzuvela',
    'Blinding Lights',
    'Cylon',
    'Arcade',
    'Bikini Bottom',
    'The Fall',
    'F2 Circuits',
    'Food Court',
    'The Heart River',
    'Screaming Sharky',
    "Heisenberg's Math Lab",
    'The Mom',
    'Car-O-Sail',
    'Calling For Duty',
    'Shrek',
    'Secure The Bag',
    'Bathroom 1',
    'Bathroom 2',
    'Bathroom 3',
    'Bathroom 4',
    'Bathroom 5',
    'The Palms',
    'Fight Club',
    'Krusty Krabs',
    "Heaven's Bridge Entrance 2",
    'Astroworld',
    'Babatunde',
    "Heaven's Bridge Entrance 1",
    'The After Hours',
    'Finding Jesse',
    'Tilted Towers',
]
rides_data = {
    'Entrance':{"visited": False, "ride_type": [""], "neighbours": [("Ticket Counter", 80)]},
    'Ticket Counter':{"visited": False, "ride_type": [""], "neighbours": [("Bathroom 4", 20), ("The Fall", 50), ("Fight Club", 40), ("Cylon", 100), ("Astroworld", 50)]},
    'XOChella':{"visited": False, "ride_type": ["Water", "Adventure"], "neighbours": [("Arcade", 30), ("Food Court", 40), ("The Heart River", 30), ("Secure The Bag", 20), ("Bathroom 2", 10), ("Krusty Krabs", 30), ("Tilted Towers", 20)]},
    'Vuzuvela':{"visited": False, "ride_type": ["Thrill", "Water"], "neighbours": [("The Fall", 40), ("Heaven's Bridge Entrance 1", 40)]},
    'Blinding Lights':{"visited": False, "ride_type": ["Thrill"], "neighbours": [("Cylon", 50), ("The Mom", 90), ("Shrek", 10)]},
    'Cylon':{"visited": False, "ride_type": ["Thrill"], "neighbours": [("Astroworld", 60), ("The Heart River", 10), ("Screaming Sharky", 40), ("Krusty Krabs", 30)]},
    'Arcade':{"visited": False, "ride_type": ["Kids"], "neighbours": [("Finding Jesse", 10)]},
    'Bikini Bottom':{"visited": False, "ride_type": ["Water", "Adventure"], "neighbours": [('Finding Jesse', 10), ("Secure The Bag", 20)]},
    'The Fall':{"visited": False, "ride_type": ["Thrill"], "neighbours": [("The Mom", 100), ("Heaven's Bridge Entrance 1", 20)]},
    'F2 Circuits':{"visited": False, "ride_type": ["Thrill", "Adventure"], "neighbours": [("Screaming Sharky", 50), ("The Heart River", 40)]},
    'Food Court':{"visited": False, "ride_type": ["Utilities"], "neighbours": [("Calling For Duty", 40), ("The Heart River", 40)]},
    'The Heart River':{"visited": False, "ride_type": ["Water", "Kids"], "neighbours": [("Bathroom 5", 10), ("Calling For Duty", 40)]},
    'Screaming Sharky':{"visited": False, "ride_type": ["Horror"], "neighbours": [("Heisenberg's Math Lab", 30), ("Astroworld", 50)]},
    "Heisenberg's Math Lab":{"visited": False, "ride_type": ["Thrill", "Water", "Horror"], "neighbours": [("The Mom", 30)]},
    'The Mom':{"visited": False, "ride_type": ["Thrill", "Horror"], "neighbours": [("Ticket Counter", 80)]},
    'Car-O-Sail':{"visited": False, "ride_type": ["Kids"], "neighbours": [("Astroworld", 50), ("Krusty Krabs", 50), ("Bathroom 1", 10), ("Fight Club", 30)]},
    'Calling For Duty':{"visited": False, "ride_type": ["Adventure"], "neighbours": [("The Palms", 40)]},
    'Shrek':{"visited": False, "ride_type": ["Kids"], "neighbours": []},
    'Secure The Bag':{"visited": False, "ride_type": ["Adventure", "Horror"], "neighbours": []},
    'Bathroom 1':{"visited": False, "ride_type": ["Utilities"], "neighbours": []},
    'Bathroom 2':{"visited": False, "ride_type": ["Utilities"], "neighbours": []},
    'Bathroom 3':{"visited": False, "ride_type": ["Utilities"], "neighbours": [("Babatunde", 10)]},
    'Bathroom 4':{"visited": False, "ride_type": ["Utilities"], "neighbours": []},
    'Bathroom 5':{"visited": False, "ride_type": ["Utilities"], "neighbours": []},
    'The Palms':{"visited": False, "ride_type": ["Kids", "Adventure"], "neighbours": []},
    'Fight Club':{"visited": False, "ride_type": ["Adventure"], "neighbours": []},
    'Krusty Krabs':{"visited": False, "ride_type": ["Utilities"], "neighbours": [("Heaven's Bridge Entrance 2", 10)]},
    "Heaven's Bridge Entrance 2":{"visited": False, "ride_type": ["Adventure"], "neighbours": [("Heaven's Bridge Entrance 1", 70)]},
    'Astroworld':{"visited": False, "ride_type": ["Adventure", "Horror"], "neighbours": [("Babatunde", 10)]},
    'Babatunde':{"visited": False, "ride_type": ["Horror"], "neighbours": [("Heaven's Bridge Entrance 1", 10)]},
    "Heaven's Bridge Entrance 1":{"visited": False, "ride_type": ["Adventure"], "neighbours": [("The After Hours", 20)]},
    'The After Hours':{"visited": False, "ride_type": ["Thrill", "Horror"], "neighbours": []},
    'Finding Jesse':{"visited": False, "ride_type": ["Kids", "Adventure"], "neighbours": []},
    'Tilted Towers':{"visited": False, "ride_type": ["Thrill", "Adventure"], "neighbours": []},
}
rideTypes= ["Utilities", "Kids", "Thrill", "Adventure", "Water", "Horror"]

#MAKING THE GRAPH
def addnodes(G,nodes):
    for i in nodes:
        G[i]=[]
    return G
def my_graph(G,rides):
    for key,value in rides.items():
        for connection in value["neighbours"]: 
            G[key].append((connection[0],connection[1]))
            G[connection[0]].append((key,connection[1]))
    return G

#HELPER FUNCTIONS
def show_unvisited(visited,nodes):
    lst=[]
    for i in nodes:
        if i not in visited and rides_data[i]["ride_type"] != ["Utilities"]:
            if rides_data[i]["ride_type"] != [""]:
                lst.append(i)
            
    return lst

def dijkstra_for_desired(graph,start,end):
    table,visited={},[]
    table[start]=[start,0]

    #Table with all values infinite except starting node
    for key in graph:
        if key!=start:
            table[key] = ["",math.inf]    

    # print(table)

    #Code begin
    while len(visited) < len(graph):

        #choose minimum value node in table to know which node to continue with
        minval,node=math.inf,""
        for key,val in table.items():
            if key not in visited and val[1] < minval:
                minval=val[1]
                node=key

        #go into the neighbours of minimum value node in table
        for neighbour in graph[node]: 
            cost,thenode = neighbour[1]+minval,neighbour[0]
            #check if the value should be updated in table, then update    
            if thenode not in visited and cost < table[thenode][1]:
                table[thenode][0],table[thenode][1] =node, cost
    

        visited.append(node)

    # print(visited)
    # print(table)

    # backtracking
    mynode,path=end,[]
    
    while mynode!=start:
        path.append((table[mynode][0],mynode))
        mynode = table[mynode][0]
    ans = ""
    for i in path[::-1]:
        if i == path[0]:
            ans += i[0]+" -> "+i[1]
        else:
            ans += i[0]+" -> "
        
    return(ans, table[end][1])






def enqueue(queue,char):
    queue.append(char)
def dequeue(queue):
    return queue.pop(0)
def isempty(queue):
    return len(queue) == 0

def option3(Graph, visited, prefer, current):
    preferred_rides = []
    outputlst = show_unvisited(visited,nodes)
    for ride in outputlst:
        if prefer in rides_data[ride]["ride_type"]:
            preferred_rides.append(ride)
    if len(preferred_rides) == 0:
        print("All preferred rides visited.")
    else:
        (min_path, min_cost) = [], 100000
        for ride in preferred_rides:
            path, cost = dijkstra_for_desired(Graph,current,ride)
            if cost < min_cost:
                min_path, min_cost = [(ride, path)], cost
            elif cost == min_cost:
                min_path.append((ride, path))
        if len(min_path) == 1:
            print()
            print("Path:", min_path[0][1])
            return min_path[0][0]
        else:
            print("Multiple nearest preferred rides found:")
            rides = []
            for ride in min_path:
                rides.append(ride[0])
                if ride == min_path[-1]:
                    print(ride[0])
                else:
                    print(ride[0], end=", ")
            chosen = get_location_input("Choose any one of the following nearest preferred rides: ", rides)
            for ride in min_path:
                if ride[0] == chosen:
                    print()
                    print("Path:", ride[1])
                    return ride[0]

def option2(Graph, visited, current):
    outputlst = show_unvisited(visited,nodes)
    (min_path, min_cost) = [], 100000
    if len(outputlst) == 0:
        return
    for ride in outputlst:
        path, cost = dijkstra_for_desired(Graph,current,ride)
        if cost < min_cost:
            min_path, min_cost = [(ride, path)], cost
        elif cost == min_cost:
            min_path.append((ride, path))
    if len(min_path) == 1:
        print("Path:", min_path[0][1])
        return min_path[0][0]
    else:
        print("Multiple nearest rides found:")
        rides = []
        for ride in min_path:
            rides.append(ride[0])
            if ride == min_path[-1]:
                print(ride[0])
            else:
                print(ride[0], end=", ")
        chosen = get_location_input("Choose any one of the following nearest rides: ", rides)
        for ride in min_path:
            if ride[0] == chosen:
                print("Path:", ride[1])
                return ride[0]

def main():
    Graph={}
    Graph = addnodes(Graph,nodes)
    Graph= my_graph(Graph,rides_data) 

    print("Welcome To Habib University Theme Park")
    print("input 1 for Complete Tour")
    print("input 2 to start from a random position")

    starting = get_numeric_input("Select: ", [1, 2])
    if starting == 1:
        visited=[]
        current = "Entrance"
        queue = [current]
    
        while not isempty(queue):
            node = dequeue(queue)
            if node not in visited:
                current = node
                print("New location: ",current)
                visited.append(node)
                print("visited",visited)
                print("1 to continue")
                print("2 for exit")
                cont = get_numeric_input("Choose: ", [1, 2])
                if cont == 2:
                    break
                for neighbour in Graph[node]:
                    if neighbour[0] not in visited and rides_data[neighbour[0]]["ride_type"] != ["Utilities"]:
                        enqueue(queue,neighbour[0])

            print()

    else:
        visited = []
        current = get_location_input("Current location: ", nodes)

        while len(visited) <= len(Graph):
            print("New location: ",current)
            visited.append(current)
            print("visited",visited)
            # Show Options

            print("1 to see all unvisited rides")
            print("2 to see nearest unvisited ride")
            print("3 to see nearest preferred unvisited ride")

            option = get_numeric_input("Choose: ", [1, 2, 3])

            if option==1:
                outputlst = show_unvisited(visited,nodes)
                print(outputlst)
                while True:
                    chosen = get_location_input("Choose Ride: ", outputlst)
                    if chosen in outputlst:
                        path = dijkstra_for_desired(Graph,current,chosen)[0]
                        print()
                        print("Path:",path)
                        current = chosen
                        break
                    else:
                        print("Invalid Input")
            elif option==2:
                    check = option2(Graph, visited, current)
                    if check != None:
                        current = check  
                    else:
                        print("All rides visited.")

            elif option==3:
                while True:
                    print("Ride Types:")
                    for type in rideTypes:
                        if type == rideTypes[-1]:
                            print(type)
                        else:
                            print(type, end=", ")
                    prefer = get_ride_type_input("Choose Preferred Ride Type: ", rideTypes)
                    if prefer in rideTypes:
                        check = option3(Graph, visited, prefer, current)
                        if check != None:
                            current = check
                        break
                    print("Invalid ride type. Try again.")

            print()             

if __name__ == "__main__":
    main()

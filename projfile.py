import math
import pprint

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
    'Entrance':{"visited": False, "ride_type": ["Utilities"], "neighbours": [("Ticket Counter", 80)]},
    'Ticket Counter':{"visited": False, "ride_type": ["Utilities"], "neighbours": [("Bathroom 4", 20), ("The Fall", 50), ("Fight Club", 40), ("Cylon", 100), ("Astroworld", 50)]},
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

def show_unvisited(visited,nodes):
    lst=[]
    for i in nodes:
        if i not in visited and rides_data[i]["ride_type"] != ["Utilities"]:
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
    mynode,ans=end,[]
    
    while mynode!=start:
        ans.append((table[mynode][0],mynode))
        mynode = table[mynode][0]

    return(ans[::-1])


def main():
    Graph={}
    Graph = addnodes(Graph,nodes)
    Graph= my_graph(Graph,rides_data)
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(Graph)
    # print(Graph)

    print("Welcome To Habib University Theme Park")
    print("input 1 for Complete Tour")
    print("input 2 to start from a random position")

    starting = int(input("Select: "))
    if starting == 1:
        current = "Gate"
    else:
        visited = []
        current = input("Current location: ")

        while len(visited) <= len(Graph):
            print("New location: ",current)
            visited.append(current)
            print("visited",visited)
            # Show Options
            print("1 to see all unvisited rides")
            print("2 to see nearest unvisited ride")
            print("3 to see nearest preferred unvisited ride")

            option = int(input("Choose: "))

            if option==1:
                outputlst = show_unvisited(visited,nodes)
                print(outputlst)
                while True:
                    chosen = input("Choose Ride: ")
                    if chosen in outputlst:
                        path = dijkstra_for_desired(Graph,current,chosen)
                        print(path)
                        current = chosen
                        break
                    else:
                        print("Invalid Input")
                        
            print()

main()

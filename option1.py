# # if option==1:
# #     outputlst = show_unvisited(visited,nodes)
# #     print(outputlst)
# #     while True:
# #         chosen = input("Choose Ride: ")
# #         if chosen in outputlst:
# #             path = dijkstra_for_desired(Graph,current,chosen)[0]
# #             print("path= ",path)
# #             current = chosen
# #             break
# #         else:
# #             print("Invalid Input")


# def dijkstra_for_desired(graph,start,end):
#     table,visited={},[]
#     table[start]=[start,0]

#     #Table with all values infinite except starting node
#     for key in graph:
#         if key!=start:
#             table[key] = ["",math.inf]    

#     # print(table)

#     #Code begin
#     while len(visited) < len(graph):

#         #choose minimum value node in table to know which node to continue with
#         minval,node=math.inf,""
#         for key,val in table.items():
#             if key not in visited and val[1] < minval:
#                 minval=val[1]
#                 node=key

#         #go into the neighbours of minimum value node in table
#         for neighbour in graph[node]: 
#             cost,thenode = neighbour[1]+minval,neighbour[0]
#             #check if the value should be updated in table, then update    
#             if thenode not in visited and cost < table[thenode][1]:
#                 table[thenode][0],table[thenode][1] =node, cost
    

#         visited.append(node)

#     # print(visited)
#     # print(table)

#     # backtracking
#     mynode,path=end,[]
    
#     while mynode!=start:
#         path.append((table[mynode][0],mynode))
#         mynode = table[mynode][0]
#     ans = ""
#     for i in path[::-1]:
#         if i == path[0]:
#             ans += i[0]+" -> "+i[1]
#         else:
#             ans += i[0]+" -> "
        
#     return(ans, table[end][1])


# def option3(Graph, visited, prefer, current):
#     preferred_rides = []
#     outputlst = show_unvisited(visited,nodes)
#     for ride in outputlst:
#         if prefer in rides_data[ride]["ride_type"]:
#             preferred_rides.append(ride)
#     if len(preferred_rides) == 0:
#         print("All preferred rides visited.")
#     else:
#         (min_path, min_cost) = [], 100000
#         for ride in preferred_rides:
#             path, cost = dijkstra_for_desired(Graph,current,ride)
#             if cost < min_cost:
#                 min_path, min_cost = [(ride, path)], cost
#             elif cost == min_cost:
#                 min_path.append((ride, path))
#         if len(min_path) == 1:
#             print("Path:", min_path[0][1])
#             return min_path[0][0]
#         else:
#             print("Multiple nearest preferred rides found:")
#             rides = []
#             for ride in min_path:
#                 rides.append(ride[0])
#                 if ride == min_path[-1]:
#                     print(ride[0])
#                 else:
#                     print(ride[0], end=", ")
#             while True:
#                 chosen = input("Choose any one of the following nearest preferred rides: ")
#                 if chosen in rides:
#                     break
#                 print("Invalid ride. Try again.")
#             for ride in min_path:
#                 if ride[0] == chosen:
#                     print("Path:", ride[1])
#                     return ride[0]

# def option2(Graph, visited, current):
#     outputlst = show_unvisited(visited,nodes)
#     (min_path, min_cost) = [], 100000
#     if len(outputlst) == 0:
#         return
#     for ride in outputlst:
#         path, cost = dijkstra_for_desired(Graph,current,ride)
#         if cost < min_cost:
#             min_path, min_cost = [(ride, path)], cost
#         elif cost == min_cost:
#             min_path.append((ride, path))
#     if len(min_path) == 1:
#         print("Path:", min_path[0][1])
#         return min_path[0][0]
#     else:
#         print("Multiple nearest rides found:")
#         rides = []
#         for ride in min_path:
#             rides.append(ride[0])
#             if ride == min_path[-1]:
#                 print(ride[0])
#             else:
#                 print(ride[0], end=", ")
#         while True:
#             chosen = input("Choose any one of the following nearest rides: ")
#             if chosen in rides:
#                 break
#             print("Invalid ride. Try again.")
#         for ride in min_path:
#             if ride[0] == chosen:
#                 print("Path:", ride[1])
#                 return ride[0]


# def main():
#     Graph={}
#     Graph = addnodes(Graph,nodes)
#     Graph= my_graph(Graph,rides_data)
#     # pp = pprint.PrettyPrinter(indent=1)
#     pp.pprint(Graph)
#     # print(Graph)

#     print("Welcome To Habib University Theme Park")
#     print("input 1 for Complete Tour")
#     print("input 2 to start from a random position")

#     starting = int(input("Select: "))
#     if starting == 1:
#         current = "Gate"
#     else:
#         visited = []
#         while True:
#             current = input("Current location: ")
#             if current not in nodes:
#                 print("Invalid ride. Try again.")
#                 continue
#             while len(visited) <= len(Graph):
#                 print("New location: ",current)
#                 visited.append(current)
#                 print("visited",visited)
#                 # Show Options
#                 print("1 to see all unvisited rides")
#                 print("2 to see nearest unvisited ride")
#                 print("3 to see nearest preferred unvisited ride")

#                 option = int(input("Choose: "))

#                 if option==1:
#                     outputlst=show_unvisited(visited,nodes)
#                     print(outputlst)
#                     while True:
#                         chosen = input("Choose Ride: ")
#                         if chosen in outputlst:
#                             path = dijkstra_for_desired(Graph,current,chosen)
#                             print(path)
#                             current = chosen
#                         else:
#                             print("Invalid Input")
#                 if option==2:
#                     check = option2(Graph, visited, current)
#                     if check != None:
#                         current = check  
#                     else:
#                         print("All rides visited.")

#                 if option==3:
#                     while True:
#                         print("Ride Types:")
#                         for type in rideTypes:
#                             if type == rideTypes[-1]:
#                                 print(type)
#                             else:
#                                 print(type, end=", ")
#                         prefer = input("Choose Preferred Ride Type: ")
#                         if prefer in rideTypes:
#                             check = option3(Graph, visited, prefer, current)
#                             if check != None:
#                                 current = check
#                             break
#                         print("Invalid ride type. Try again.")     
# main()
#---------------Implement DFS and BFS graph traversal algorithms-------------  

# DFS function :
def DFS(visited,graph,node):
    if node in graph:
        if node not in visited:
            print(node,end="")
            visited.add(node)
            for neighbor in graph[node]:
                DFS(visited,graph,neighbor)
    else:
        print("Error: Node "+node+" not found in the graph!")


# BFS function : 
def BFS(visited,graph,node):
    queue=[]
    
    if node in graph:
        visited.add(node)
        queue.append(node)
        while queue:
            m=queue.pop(0)
            print(m,end="")
            for neighbor in graph[m]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    else:
        print("ERROR: Node "+node+" not found in the graph!")


# Taking custom input from the user : 
def setGraph(graph):
    numEdges=int(input("Enter the number of edges: "))

    for i in range(numEdges):
        node=input("Enter node "+str(i+1)+": ")
        neighbors=input("Enter neighbors of "+node+" separated by space: ").split()
        graph[node]=neighbors

    return graph


# Main Menu function :  
def menu(graph):
    print("\n------------MENU--------------\n\n1.Enter a graph\n2.DFS\n3.BFS\n4.Exit")
    choice=int(input("\nEnter your choice: "))

    if choice==1:
        graph=setGraph(graph)
        print("\ngraph: "+str(graph))
    elif choice==2:
        print("DFS: ")
        startNode=input("Enter the starting node: ")
        DFS(set(),graph,startNode)
    elif choice==3:
        print("BFS: ")
        startNode=input("Enter the starting node: ")
        BFS(set(),graph,startNode)
    elif choice==4:
        print("\nProgram Ended")
        exit()
    else:
        print("\nInvalid input")



# Initializing empty graph :
graph={}

# Menu function will execute until exit choice isn't opted :
while True:
    menu(graph)



#Time complexity : DFS BFS :- O(V+E)
#Space complexity : DFS BFS :- O(V)



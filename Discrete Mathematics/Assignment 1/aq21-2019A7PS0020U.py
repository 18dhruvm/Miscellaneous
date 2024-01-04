vertices = int(input("Enter number of vertices: "))
  
def DFS(graph, marked, n, vert, start, count): 
  
    # mark the vertex as visited 
    marked[vert] = True
   
    # if there is path of (n-1) 
    if n == 0:  
  
        # mark vertex as unvisited
        marked[vert] = False
   
        # Check if vertex vert can end with vertex start 
        if graph[vert][start] == 1: 
            count = count + 1
            return count 
        else: 
            return count 
   
    # For searching every possible path of length (n-1) 
    for i in range(vertices): 
        if marked[i] == False and graph[vert][i] == 1: 
  
            count = DFS(graph, marked, n-1, i, start, count) 
   
    # marking vert as unvisited 
    marked[vert] = False
    return count 
   
# Counts cycles of length  
def countCycles( graph, n): 
  
    # all vertex are marked unvisited initially. 
    marked = [False] * vertices  
   
    # Searching for cycle by using v-n+1 vertices 
    count = 0
    for i in range(vertices-(n-1)): 
        count = DFS(graph, marked, n-1, i, i, count) 
   
        # ith vertex is marked as visited and 
        # will not be visited again. 
        marked[i] = True
      
    return int(count/2) 
   
# main : 
graph=[]

print("Enter adjacency matrix for the desired graph")
for i in range(vertices):

    elements=list(input("Enter %d row: "%(i+1)))
    
    for i in range(0,len(elements)):
       elements[i]=int(elements[i]) 
    graph.append(elements)
            
n = int(input("Enter +ve no n to determine whether the graph has a cycle of length n: "))

#conclusion
if (countCycles(graph, n)>0):
    print("Yes, the graph has cycle(s) of length",n)
    print("Total cycles of length",n,"are",countCycles(graph, n))
else:
    print("No, the graph doesnt have cycle of length",n)
    
    

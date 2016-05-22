neighbour_list = [[4], [2, 5], [1, 3, 8], [2, 14], [0, 9], [1], [10, 12], [13], 
                 [2, 14], [4, 10, 15], [6, 9], [17], [6], [7, 19, 20], [3, 8], 
                 [9, 21], [22], [11, 18], [17, 19], [13, 18, 26], [13, 26], 
                 [15, 27], [16, 23], [22, 24, 28], [23, 25, 29], [24], 
                 [19, 20, 30, 31], [21], [23, 29], [24, 28], [26, 31], [26, 30]]

def bfs(neighbour_list, root):
    queue = []
    seen = set()

    queue.append(root)
    seen.add(root)

    while queue:
        cn = queue.pop(0)
        print("Current node: %d" % cn)
        for nn in neighbour_list[cn]:
            if nn not in seen:
                queue.append(nn)
                seen.add(nn)
                print("  Found %d" % nn)

    return seen
def regiongrow(image,epsilon,start_point):
	Q = Queue()
    s = []    
    x = start_point[0]
    y = start_point[1]
    while not Q.isEmpty():

        t = Q.deque()
        x = t[0]
        y = t[1]
    
   
    Q.enque((x,y))
    while not Q.isEmpty():

        t = Q.deque()
        x = t[0]
        y = t[1]
        (a,b,c,d,e,f,g,h,i)=tuple(np.subtract(shape[x+1][y],tuple(means)))
        ssd=((a/(step))**2+(b/(step))**2+(c**2)/(step**2)/2+f**2+g**2+h**2+(i/step**2)**2)
        if x < image.shape[0]-1 and \
           ssd<= epsilon :

            if not Q.isInside( (x + 1 , y) ) and not (x + 1 , y) in s:
                Q.enque( (x + 1 , y) )
        (a,b,c,d,e,f,g,h,i)=tuple(np.subtract(shape[x-1][y],tuple(means)))
        ssd=((a/(step))**2+(b/(step))**2+(c**2)/(step**2)/2+f**2+g**2+h**2+(i/step**2)**2)
                
        if x > 0 and \
           ssd<= epsilon:

            if not Q.isInside( (x - 1 , y) ) and not (x - 1 , y) in s:
                Q.enque( (x - 1 , y) )
        (a,b,c,d,e,f,g,h,i)=tuple(np.subtract(shape[x][y+1],tuple(means)))
        ssd=((a/(step))**2+(b/(step))**2+(c**2)/(step**2)/2+f**2+g**2+h**2+(i/step**2)**2)
                     
        if y < (image.shape[1] - 1) and \
           ssd<= epsilon:

            if not Q.isInside( (x, y + 1) ) and not (x , y + 1) in s:
                Q.enque( (x , y + 1) )

        (a,b,c,d,e,f,g,h,i)=tuple(np.subtract(shape[x][y-1],tuple(means)))
        ssd=((a/(step))**2+(b/(step))**2+(c**2)/(step**2)/2+f**2+g**2+h**2+(i/step**2)**2)            
        if y > 0 and \
           ssd <= epsilon:

            if not Q.isInside( (x , y - 1) ) and not (x , y - 1) in s:
                Q.enque( (x , y - 1) )


        if t not in s:
            s.append( t )
print bfs(neighbour_list, 0)

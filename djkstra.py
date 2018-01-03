import heapq
import sys
#print "dsads"
class Vertex:
    def __init__(self, node,pur,idd):
        self.id=idd
        self.name = node
        self.distance=0
        self.pic="img.png"
        self.next={}
        self.purpose=pur
        self.distance_1=sys.maxint
        self.visited=False
        self.previous=None
        
    def show(self):
        #print self.name
        self.name
    def add_neighbour(self,neighbour,dist):
        self.next[neighbour]=dist
    def show_neighbour(self):
        for i in self.next.keys():
            i.name
            #print i.name
        return self.next.keys() 
    def show_name(self):
        return self.name
    def set_visited(self):
        self.visited=True
    def set_distance(self,dist):
        self.distance_1=dist
    def get_distance(self):
        return self.distance_1
    def get_weight(self,neighbour):
        #print "neighbour is "+neighbour.name
        #print self.next[neighbour]
        j=self.next[neighbour]
        return j
    def set_previous(self,current):
        self.previous=current
        
class Graph:
    def __init__(self):
          self.number_of_vertices=0
          self.vertical={}
          
    def add_vertex(self,node,pur,idd):
        self.number_of_vertices=self.number_of_vertices+1
        new_node=Vertex(node,pur,idd)
        self.vertical[node]=new_node
     
    def show_vertex(self):
        for i in self.vertical:
            #print self.vertical[i].name
            self.vertical[i].name
    def get_vertex(self,n):
        if n in self.vertical:
            return self.vertical[n]
        else:
            return None
        
    def add_edge(self,start,end,dist):
        self.vertical[start].add_neighbour(self.vertical[end],dist)
        self.vertical[end].add_neighbour(self.vertical[start],dist)
    
    def show_edge(self):
        for i in self.vertical:
             a=self.vertical[i]
            # print "for name == "
            # print a.show_name()
            # print "  "
             b=a.show_neighbour()
def shortest_path(b,path) :
    if b.previous:
        #print b.previous.show_name()
        path.append(b.previous.show_name())
        shortest_path(b.previous,path)
def dijkastra(gra,start,end):
    unvisited_queue=[]    
    #print "start is "+ start.name
    start.set_distance(0)
    for i in gra.vertical:
        b=gra.get_vertex(i)
        unvisited_queue.append((b.get_distance(),b))        
    #for i in unvisited_queue:
     #   print i
       
    #unvisited_queue=[(b.get_distance(),b) for b in gra]
    heapq.heapify(unvisited_queue)
    for i in unvisited_queue:
        i
        #print i
    while len(unvisited_queue):
        tmp=heapq.heappop(unvisited_queue)
        current=tmp[1]
        current.set_visited()
        
        #print "current is " + current.name + "it is "+ str(current.visited)

        for i in current.next:
            if i.visited:
                continue
            new_dist=current.get_distance()+current.get_weight(i)
            if new_dist<i.get_distance():
                i.set_distance(new_dist)
                i.set_previous(current)
         #       print "previous is "+current.name+ "of" +i.name
         #       print 'updated: current =%s next =%s new_dist=%s'%(current.show_name(),i.show_name(),i.get_distance())
        
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        #print "the unvisited queue is"
        #print unvisited_queue
        for i in gra.vertical:
            b=gra.get_vertex(i)
            if not b.visited:
                unvisited_queue.append((b.get_distance(),b))
       # unvisited_queue=[(b.get_distance(),b) for b in gra if not b.visited]
        heapq.heapify(unvisited_queue)
    

if __name__ == '__main__':

    g=Graph()
    g.add_vertex("library","library",1)
    g.add_vertex("garden","rest",2)
    g.add_vertex("lib_canteen","eat",3)
    g.add_vertex("back_gate","gate",4)
    g.add_vertex("lib_gate","gate",5)
    g.add_vertex("lib_to_f_block_gate","gate",6)
    g.add_vertex("f_block","acedemic",7)
    g.add_vertex("e_block","acedemic",8)
    g.add_vertex("workshop","acedemic",8)
    
    
    g.show_vertex()
    #for library
    g.add_edge("library","garden",1)
    g.add_edge("library","lib_to_f_block_gate",1)
    g.add_edge("library","lib_canteen",1)
    g.add_edge("library","back_gate",1)
    g.add_edge("garden","lib_to_f_block_gate",1)
    g.add_edge("garden","lib_gate",1)
    g.add_edge("lib_canteen","lib_gate",1)
    g.add_edge("lib_gate","workshop",1)
    g.add_edge("f_block","e_block",1)
    g.add_edge("library","lib_gate",1)
    g.add_edge("f_block","workshop",1)
   ## show a newa path here to the teacher
   # g.add_edge("f_block","lib_to_f_block_gate",1)
    #g.add_edge("")
    g.show_edge()
    dijkastra(g,g.get_vertex("library"),g.get_vertex("e_block"))
    path=[g.get_vertex("e_block").show_name()]
    shortest_path(g.get_vertex("e_block"),path)
    for i in path:
        i
        print i
        #print "dsadasdsadsasssssssssssssss"
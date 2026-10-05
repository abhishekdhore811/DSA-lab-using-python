class Queue:
    def __init__(self):
        self.F=-1
        self.R=-1
        self.QT=[0]*5
    
    def insert(self,x):
        if self.R==4:
            print("Queue is overflow...")
            return
        self.R=self.R+1
        
        self.QT[self.R]=x
        
        if self.F==-1:
            self.F=0
    
    def delete(self):
        if self.F==-1:
            print("Nothing to delete..")
            return
        else:
            y=self.QT[self.F]
        
        if self.F==self.R:
            self.F=self.R=-1
        else:
            self.F=self.F+1
        return y
    
    def display(self):
        if self.F==-1:
            print("Nothing to print")
            return
        for i in range (self.F,self.R+1):
            print(self.QT[i]) 
            

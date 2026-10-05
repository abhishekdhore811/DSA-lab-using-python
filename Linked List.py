class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def create(self):
        n=int(input("Enter no of nodes: "))

        if n<=0:
            print("Enter valid nodes")
            return
        
        for i in range(1,n+1):
            val=input(f"Enter data {i}: ")
            self.insert(val)

        print("Linked list created successfully...")

    def insert(self,val):
        new_node=Node(val)

        if self.head==None:
            self.head=new_node
            return
        
        temp=self.head
        while temp.next is not None:
            temp=temp.next

        temp.next=new_node

    def delete(self,val):

        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.data==val:
            self.head=self.head.next
            print(f"{val} node deleted.")
            return

        prev=self.head
        temp=self.head.next

        while temp is not None:
            if temp.data==val:
                prev.next=temp.next
                print(f"{val} node deleted.")
                return

            prev=temp
            temp=temp.next

        print(f"{val} not found for deletion.")

    def display(self):
        if self.head is None:
            print("Linked list is empty...")
            return

        temp=self.head
        while temp is not None:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")


# Main Program
obj = LL()

while True:
    print("\n------ MENU ------")
    print("1. Create Linked List")
    print("2. Insert Node")
    print("3. Delete Node")
    print("4. Display Linked List")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        obj.create()

    elif ch == 2:
        val = input("Enter data to insert: ")
        obj.insert(val)
        print("Node inserted successfully.")

    elif ch == 3:
        val = input("Enter data to delete: ")
        obj.delete(val)

    elif ch == 4:
        obj.display()

    elif ch == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")
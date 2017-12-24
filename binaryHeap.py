#-----------------------------------------------------------------------#
#This file contains operations related to the Max Binary Heap		#
#	Author: Utkarsh Dwivedi				   		#
#	Email: utkarshdwivedi394@gmail.com		   		#
#	Version: 2.1					   		#
#-----------------------------------------------------------------------#
import binaryHeapUtility as bHeap

class MaxHeap:
	def __init__(self):
		self.arr = []

	def insert(self,val):
		#insert the value at leaf node
		self.arr.append(val)
		i = len(self.arr)-1

		while self.arr[i] > parent(i,self.arr,1):
			swap(i,parent(i),self.arr)
			i = parent(i)
		return True

	def delete(self,node):
		#Swap the node to be deleted with the last node
		swap(node,-1,self.arr)
		#Delete the last Node
		self.arr.pop()

		#Heapify the entire tree again
		for i in range(len(self.arr)/2,-1,-1):
			self.maxHeapify(i)
		return
	
	def maxHeapify(self, node=0):
		left_node = left_child(node,self.arr)
		right_node = right_child(node,self.arr)
	
		#Below four conditions determine the greatest of parent, leftChild, rightChild
		if left_node and self.arr[left_node] > self.arr[node]:
			max_node = left_node
		else:
			max_node = node
	
		if right_node and self.arr[right_node] > self.arr[max_node]:
			max_node = right_node

		if max_node != node:
			swap(node,max_node,self.arr)
			#Heapify again for the max_node
			self.maxHeapify(max_node)
		return

	def getMaxHeap(self):
		return self.arr

#These function returns only index if value=0
#If value=1 and arr is given then returns value at the location

#Returns the parent of the given node in the array
def parent(i, arr=None, value=0):
	if i == 0:
		i = 1
	if value == 1:
		return arr[(i-1)/2]
	return (i-1)/2

#Returns the left child of the given node in the array
def left_child(i, arr, value=0):
	if 2*i+1 < len(arr):
		if value == 1:
			return arr[2*i+1]
		return 2*i+1
	return None

#Returns the right child of the given node in the array
def right_child(i, arr, value=0):
	if 2*i+2 < len(arr):
		if value == 1:
			return arr[2*i+2]
		return 2*i+2
	return None

#Swap elements at given indices in arr
def swap(x,y,arr):
	arr[x] += arr[y]
	arr[y] = arr[x]-arr[y]
	arr[x] = arr[x]-arr[y]


def showMainMenu():
	print "%20s"%("WELCOME")
	print "1. Create New Heap"
	print "2. Change to Heap"
	print "3. Insert Node"
	print "4. Delete Node"
	print "5. Print the given Heap in Tree Structure"
	print "6. Print the Heap in normal levelwise structure"
	print "0. Exit"
	print "Enter your Choice:",
	
	try:
		choice = int(raw_input())
		while int(choice) not in range(0,7):
			print "Wrong Choice!!"
			print "Enter correct choice:",
			choice = int(raw_input())
		return choice
	except ValueError:
		print "Naughty boy! Wrong key pressed, enter integer value",
		return 100
	except:
		print "Something fishy happened!",
		return 101

#To call different operations on the heap as per the choice provided by user
def callOperations(choice, heapArr, curHeap):
	funcDict = {
		1: [createHeap, heapArr],		#[function, arguments]
		2: [changeHeap, heapArr],
		3: [insert,curHeap],
		4: [delete,curHeap],
		5: [bHeap.printGivenHeap],
		6: [bHeap.printHeap],
		0: 0
		}

	if choice in range(0,5):
		return funcDict[choice][0](funcDict[choice][1])
	if choice in range(5,7):
		return funcDict[choice][0](curHeap.getMaxHeap())

#Function to create new maxHeap and append in list of Heaps
def createHeap(heapArr):
	temp = MaxHeap()
	heapArr.append(temp)
	return temp

#Function to switch between heaps
def changeHeap(heapArr):
	print "Following heaps are available:"
	i = 1
	for curHeap in heapArr:
		print "Heap No.:",i
		bHeap.printGivenHeap(curHeap.getMaxHeap())
		i += 1
	print "Enter the heap you want to choose(1-%d):"%(i-1),
	choice = int(raw_input())
	if choice in range(1,len(heapArr)+1):
		return heapArr[choice-1]
	print "ChangeHeap: Invalid Choice"
	return None

#Insert nodes into the maxHeap
def insert(curHeap):
	print "Insert Menu!!"
	print "1. Insert Nodes"
	print "2. Insert node with range of values"
	print "Your Choice:",
	ch = int(raw_input())

	if ch == 1:
		print "Enter the number of nodes to insert"
		n = raw_input()
		for i in range(int(n)):
			print "Give Value:",
			val = raw_input()
			curHeap.insert(int(val))
	if ch == 2:
		print "Enter the start range:",
		start = raw_input()
		print "Enter the end of range:",
		end = raw_input()
		
		for i in range(int(start), int(end)+1):
			curHeap.insert(i)
	return

def delete(curHeap):
	print "Current Heap:"
	bHeap.printGivenHeap(curHeap.getMaxHeap())
	print "Enter the node you want to delete(Value):",
	val = int(raw_input())
	node = curHeap.getMaxHeap().index(val)
	curHeap.delete(node)
	return

#Driver Menu
heapArr = []
curMainHeap = None
choice = showMainMenu()
while choice:
	try:
		if choice in range(0,7):
			curHeap = callOperations(int(choice), heapArr, curMainHeap)
			if curHeap:
				curMainHeap=curHeap
		else:
			print "Main:Invalid Choice!"
		print "Main Menu: Enter your choice (Press 10 to see Menu again):",
		choice = int(raw_input())
		if choice == 10:
			choice = showMainMenu()
	except ValueError:
		print "Naughty boy! Wrong key pressed, enter integer value",
		choice = 100
	except:
		print "Something fishy happened!",
		choice = 101	

#This function returns only index if value=0
#If value=1 and arr is given then returns value at the location
import sys
import math

INF = 798465416546
def parent(i, arr=None, value=0):
	if i == 0:
		i = 1
	if value == 1:
		return arr[(i-1)/2]
	return (i-1)/2

def left_child(i, arr, value=0):
	if 2*i+1 < len(arr):
		if value == 1:
			return arr[2*i+1]
		return 2*i+1
	return None

def right_child(i, arr, value=0):
	if 2*i+2 < len(arr):
		if value == 1:
			return arr[2*i+2]
		return 2*i+1
	return None

def swap(x,y,arr):
	arr[x] += arr[y]
	arr[y] = arr[x]-arr[y]
	arr[x] = arr[x]-arr[y]

def printHeap(arr):
	n = len(arr)
	cur_level = 0

	#print number while tree is exhausted
	while n > 0:
		i = 0
		#2**cur_level -> no of elements at current level
		while i < (2**cur_level) and n > 0:
			#-1 is added to compensate the 2*cur_level value which starts with 1
			print arr[2**cur_level+i-1],
			n -= 1
			i += 1
		print
		cur_level += 1

#Print Reverse Tree
#This function prints the reverse tree with value starting from 1 upto the n level
def printTreeReverse(n):
	cur_level = 0
	num = 1

	while cur_level < n:
		#Flag to print the relationship between children
		alter = False

		#Print the initial space
		sys.stdout.write("  "*(2**(cur_level)-1))
		for i in range(2**(n-cur_level-1)):
			#Print the number
			sys.stdout.write("%02d"%(num))
			num += 1
			
			#If the number is last of the current level, dont print between spaces
			if i == 2**(n-cur_level-1)-1:
				break

			if alter:
				#Print the space between two different childs
				sys.stdout.write("  "*(2**(cur_level+1)-1))
			else:
				#Print the start between two same children of the parent
				sys.stdout.write("**"*(2**(cur_level+1)-1))

			#Toggle the flag value
			alter ^= True
		cur_level += 1
		print

#This function prints the tree with values starting from 1 upto the n level
def printTree(n):
	cur_level = 0
	num = 1

	while cur_level < n:
		#Flag to print the relationship between children
		alter = False

		#Print the initial space
		sys.stdout.write("  "*(2**(n-cur_level-1)-1))
		for i in range(2**cur_level):
			#Print the number
			sys.stdout.write("%02d"%(num))
			num += 1
			
			#If the number is last of the current level, dont print between spaces
			if i == 2**(cur_level)-1:
				break

			if alter:
				#Print the space between two different childs
				sys.stdout.write("  "*(2**(n-cur_level)-1))
			else:
				#Print the start between two same children of the parent
				sys.stdout.write("**"*(2**(n-cur_level)-1))

			#Toggle the flag value
			alter ^= True
		cur_level += 1
		print

#This function prints the Heap in tree format
def printGivenHeap(arr):
	cur_level = 0
	n = int(math.ceil(math.log(len(arr)+1,2)))
	num = 0

	while cur_level < n:
		#Flag to print the relationship between children
		alter = False

		#Print the initial space
		sys.stdout.write("  "*(2**(n-cur_level-1)-1))
		for i in range(2**cur_level):
			#Print the number
			sys.stdout.write("%02d"%(arr[num]))
			num += 1
			
			#If the number is last of the current level, dont print between spaces
			if i == 2**(cur_level)-1 or num >= len(arr):
				break

			if alter:
				#Print the space between two different childs
				sys.stdout.write("  "*(2**(n-cur_level)-1))
			else:
				#Print the start between two same children of the parent
				sys.stdout.write("**"*(2**(n-cur_level)-1))

			#Toggle the flag value
			alter ^= True
		cur_level += 1
		print

def insert(arr, val):
	#insert the value at leaf node
	arr.append(val)
	i = len(arr)-1

	while arr[i] > parent(i,arr,1):
		swap(i,parent(i),arr)
		i = parent(i)
	return True

def delete(arr, node):
	#Swap the node to be deleted with the last node
	swap(node,-1,arr)
	#Delete the last Node
	arr.pop()
	maxHeapify(arr,node)

def maxHeapify(arr,node=0):
	left_node = left_child(node,arr)
	right_node = right_child(node,arr)

	max_node = left_node if left_child(node,arr,1) > right_child(node,arr,1) else right_node

	if arr[node] < arr[max_node]:
		swap(node,max_node,arr)
		maxHeapify(arr,max_node)
	return

arr = []
for i in range(1,10):
	insert(arr,i)
print "Before:"
printGivenHeap(arr)
delete(arr,0)
print "After:"
printGivenHeap(arr)

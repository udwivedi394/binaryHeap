#This function returns only index if value=0
#If value=1 and arr is given then returns value at the location
import binaryHeapUtility as bHeap

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
bHeap.printGivenHeap(arr)
delete(arr,0)
print "After:"
bHeap.printGivenHeap(arr)

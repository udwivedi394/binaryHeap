#-----------------------------------------------------------------------#
#This file contains operations related to the Max Binary Heap		#
#	Author: Utkarsh Dwivedi				   		#
#	Email: utkarshdwivedi394@gmail.com		   		#
#	Version: 2.1					   		#
#-----------------------------------------------------------------------#

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
	return

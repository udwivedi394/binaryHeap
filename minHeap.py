class MinHeap:
	def __init__(self):
		self.arr = []

	def insert(self,data):
		self.arr.append(data)
		
		i = len(self.arr)-1
		while self.arr[i] < parent(self.arr,i,1):
			swap(self.arr,i,parent(self.arr,i))
			i=parent(self.arr,i)
		return

	def delete(self,k):
		last = len(self.arr)-1
		swap(self.arr,k,last)
		self.arr.pop()
		self.minHeapify(k)

	def minHeapify(self,k):
		leftNode = leftChild(self.arr,k)
		rightNode = rightChild(self.arr,k)
	
		minNode = k
		if leftNode and self.arr[leftNode] < self.arr[k]:
			minNode = leftNode
		if rightNode and self.arr[rightNode] < self.arr[minNode]:
			minNode = rightNode

		while minNode != k:
			swap(self.arr,minNode,k)
			self.minHeapify(minNode)
		return
	
	def __str__(self):
		print self.arr
		return "True"

def swap(arr,x,y):
	arr[x] ^= arr[y]
	arr[y] ^= arr[x]
	arr[x] ^= arr[y]
	return

def parent(arr,i,value=0):
	if i==0:
		i = 1
	if value==1:
		return arr[(i-1)/2]
	return (i-1)/2

def leftChild(arr,i,value=0):
	if 2*(i+1)-1 < len(arr):
		if value==1:
			return arr[2*(i+1)-1]
		return 2*(i+1)-1
	return None

def rightChild(arr,i,value=0):
	if 2*(i+1) < len(arr):
		if value==1:
			return arr[2*(i+1)]
		return 2*(i+1)
	return None

heap = MinHeap()
heap.insert(40)
heap.insert(30)
heap.insert(20)
heap.insert(10)

print heap
heap.delete(0)
print heap

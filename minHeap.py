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
		if len(self.arr)==0:
			print "Heap empty!"
			return False
		last = len(self.arr)-1
		swap(self.arr,k,last)
		delVal = self.arr.pop()
		self.minHeapify()
		return delVal

	def minHeapify(self,k=0):
		leftNode = leftChild(self.arr,k)
		rightNode = rightChild(self.arr,k)
	
		minNode = k
		if leftNode and self.arr[leftNode] < self.arr[k]:
			minNode = leftNode
		if rightNode and self.arr[rightNode] < self.arr[minNode]:
			minNode = rightNode

		if minNode != k:
			swap(self.arr,minNode,k)
			self.minHeapify(minNode)
		return
	
	def __str__(self):
		print self.arr
		return "True"

def swap(arr,x,y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp
	return

#The XOR method works only when there are two separate memory location of x & y
def swap02(arr,x,y):
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
for i in range(100,0,-10):
	heap.insert(i)

for i in range(110,0,-10):
	print heap.delete(0)

#-----------------------------------------------------------------------#
#This file contains display utilities related to Binary Heap		#
#	Author: Utkarsh Dwivedi				   		#
#	Email: utkarshdwivedi394@gmail.com		   		#
#	Version: 1.0					   		#
#-----------------------------------------------------------------------#

import sys
import math
#This function print the pass array in levelwise tree form
def printHeap(arr):
	n = len(arr)
	cur_level = 0

	#print number while number of nodes in tree is exhausted
	while n > 0:
		#counter to count the number of nodes in current level
		i = 0
		#2**cur_level -> no of elements at current level
		while i < (2**cur_level) and n > 0:
			#-1 is added to compensate the 2*cur_level \
			#value which starts with 1	
			print arr[2**cur_level+i-1],
			n -= 1
			i += 1
		print
		cur_level += 1
	return

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
				#Print the * between two same children of the parent
				sys.stdout.write("**"*(2**(cur_level+1)-1))

			#Toggle the flag value
			alter ^= True
		cur_level += 1
		print
	return	

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
	return

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
	return 

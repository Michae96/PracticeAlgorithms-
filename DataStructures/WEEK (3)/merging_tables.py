import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
	global parent
	
	parents_to_update = []

	
	root = table
	while root != parent[root]:
		parents_to_update.append(parent[root])
		root = parent[root]

	
	for i in parents_to_update:
		parent[i] = root

	return root

def merge(destination, source):
	global ans
	realDestination, realSource = getParent(destination), getParent(source)

	if realDestination == realSource:
		return False
	if rank[realDestination] < rank[realSource]:
		parent[realDestination] = realSource
		lines[realSource] += lines[realDestination]
		ans = max(ans, lines[realSource])
	else:
		parent[realSource] = realDestination
		lines[realDestination] += lines[realSource]
		ans = max(ans, lines[realDestination])
		if rank[realDestination] == rank[realSource]:
			rank[realDestination] += 1
	
	return True

for i in range(m):
	destination, source = map(int, sys.stdin.readline().split())
	merge(destination - 1, source - 1)
	print(ans)
	
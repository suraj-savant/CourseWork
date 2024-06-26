import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        left = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth)
        right = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        print("Maximizing node at depth", curDepth, "with value", max(left, right))
        return max(left, right)
    else:
        left = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth)
        right = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        print("Minimizing node at depth", curDepth, "with value", min(left, right))
        return min(left, right)


scores = [5, 2, 1, 3, 6, 2, 0, 7]
treeDepth = math.floor(math.log(len(scores), 2))  

result = minimax(0, 0, True, scores, treeDepth)
print("Result is",result)
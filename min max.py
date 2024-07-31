import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # base case : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]
    
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )

def main():
    scores = list(map(int, input("Enter the scores (space-separated): ").split()))
    
    if not math.log(len(scores), 2).is_integer():
        print("The number of scores should be a power of 2.")
        return

    treeDepth = int(math.log(len(scores), 2))
    print("The optimal value is : ", end = "")
    print(minimax(0, 0, True, scores, treeDepth))

main()

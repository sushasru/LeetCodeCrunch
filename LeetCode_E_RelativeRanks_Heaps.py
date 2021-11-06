import heapq
def findRelativeRanks(score):
    print("\nScore:",score)
    len_sc = len(score)
    score_d = {}
    heap_score = []

    #T.C - O(n), S.C - O(n)
    for i,s in enumerate(score):
        if s not in score_d:
            score_d[s] = i

    print("\t Dictionary:",score_d)

    #T.C - O(logn), S.C - O(n)
    for i in range(len_sc//2-1,-1,-1):
        minHeap(score,i,len_sc)
        print("\t\tmaxheapscore:",score)

    #T.C - O(logn), S.C - O(n)
    for i in range(len_sc-1,-1,-1):
        score[i], score[0] = score[0], score[i]
        minHeap(score,0,i)
        print("\t\theapifyscore:",score)

    print("\t Min Heap:",score)

    
    result = []
    for i in score_d.keys():
        print(i)
        if score.index(i) == 0:
            result.append("Gold Medal")
        elif score.index(i) == 1:
            result.append("Silver Medal")
        elif score.index(i) == 2:
            result.append("Bronze Medal")
        else:
            result.append(score.index(i)+1)
        print("\t Cur Result:",result)
            


def minHeap(score,cur_idx,len_sc):
    smallest = cur_idx
    parent_idx = -(cur_idx//-2)-1
    lchild_idx = cur_idx*2 + 1
    rchild_idx = cur_idx*2 + 2
    if parent_idx <= 0:
        parent_idx = None
    if lchild_idx >= len_sc:
        lchild_idx = None
    if rchild_idx >= len_sc:
        rchild_idx = None

    if lchild_idx is not None and score[smallest] > score[lchild_idx]:
        smallest = lchild_idx

    if rchild_idx is not None and score[smallest] > score[rchild_idx]:
        smallest = rchild_idx

    if smallest != cur_idx:
        score[smallest], score[cur_idx] = score[cur_idx], score[smallest]
        minHeap(score,smallest,len_sc)
    return score

def Heapify(score,cur_idx,len_sc):
    pass
        


score = [5,4,3,2,1]
findRelativeRanks(score)
print("************************************************")
score = [10,3,8,9,4]
findRelativeRanks(score)
print("************************************************")

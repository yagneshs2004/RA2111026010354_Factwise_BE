cards= [1,2,3,4,5,6,1]
k=3
def points(cards,k):
    n=len(cards)
    sum_left = sum(cards[:k])
    sum_right = 0
    result = sum_left
    for i in range(k):
        sum_left -= cards[k-1-i]
        sum_right += cards[n-1-i]
        result=max(result,sum_left+sum_right)
    return result
result=points(cards,k)
print(result)
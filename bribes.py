# NOT WORKING


def minimumBribes(q):
    # Write your code here
    bribes = 0
    inc = 0
    size = len(q)
    for i in range(size):
        # if q[i] > i:
        #     inc += q[i] - i
        #     bribes += inc
        #     if inc > 2:
        #         print('Too chaotic')
        #         return
        # inc = 0
        for j in range(i, -1, -1):
            if q[i] < q[j]:
                bribes += 1
    print(bribes)


minimumBribes([1,2,5,3,7,8,6,4])
minimumBribes([2,5,1,3,4])

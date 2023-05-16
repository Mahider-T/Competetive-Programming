if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # top = arr[0]
    # runnerUp = arr[0]
    # for x in arr:
    #      if x > top :
    #         runnerUp = top
    #         top = x
    #      elif x > runnerUp and x != runnerUp:
    #          runnerUp = x
    maximum = max(arr)
    while(max(arr) == maximum):
        arr.remove(max(arr))
print(max(arr))
        
        
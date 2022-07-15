def solution(size):
    arr = []
    for i in range(size):
        arr.append([0]*size)
        arr[i][i] = 1
    return arr
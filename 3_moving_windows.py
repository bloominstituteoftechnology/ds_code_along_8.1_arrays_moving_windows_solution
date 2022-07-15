def solution(a, window_size):
    averages = []
    for i in range(len(a)-window_size+1):
        window_sum = 0
        for j in range(window_size):
            window_sum += a[i+j]
        window_avg = window_sum / window_size
        averages.append(window_avg)
    return averages
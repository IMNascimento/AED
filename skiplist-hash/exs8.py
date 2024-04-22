def find_pair_sorted(arr, x):
    #Encontra um par de números que somam x em um vetor ordenado.
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == x:
            return (arr[left], arr[right])
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    return None

def find_pair_unsorted(arr, x):
    #Encontra um par de números que somam x em um vetor não ordenado.
    seen = {}
    for num in arr:
        complement = x - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

#A):
# Vetor ordenado
sorted_arr = [1, 2, 3, 4, 5]
x_sorted = 9
print("Par encontrado no vetor ordenado:", find_pair_sorted(sorted_arr, x_sorted))

#B):
# Vetor não ordenado
unsorted_arr = [3, 3, 4, 2, 5]
x_unsorted = 6
print("Par encontrado no vetor não ordenado:", find_pair_unsorted(unsorted_arr, x_unsorted))
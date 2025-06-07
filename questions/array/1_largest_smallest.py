# Find the largest and smallest element in an array

def get_largest(arr) -> int:
    return max(arr)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(get_largest(arr))  # Output: 5
def generate_magic_square_odd(n):
    if n % 2 == 0:
        raise ValueError("This method only works for odd n")
    
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2  # Start from the middle of the first row

    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic_square

def print_magic_square(square):
    n = len(square)
    magic_sum = n * (n * n + 1) // 2
    print(f"Magic Square (n={n}) - Magic Sum = {magic_sum}")
    for row in square:
        print(" ".join(f"{num:2d}" for num in row))

# Example usage
if __name__ == "__main__":
    n = 3  # Must be odd
    square = generate_magic_square_odd(n)
    print_magic_square(square)

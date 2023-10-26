def longest_slide_down(pyramid):
    # Start from the second-to-last row of the pyramid and work upwards
    for row in range(len(pyramid) - 2, -1, -1):
        for i in range(len(pyramid[row])):
            # Calculate the maximum sum for each element in the current row
            pyramid[row][i] += max(pyramid[row + 1][i], pyramid[row + 1][i + 1])

    # The top element of the pyramid will contain the largest 'slide down' value
    return pyramid[0][0]

# Example usage:
pyramid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
result = longest_slide_down(pyramid)
print(result)  # Output: 23
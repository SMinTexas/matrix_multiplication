# Given two two-dimensional lists of numbers of the size 2x2 - 
# calculate the result of multiplying the two matrices. Print the resulting matrix.

# [-2 1],   [6,  5]
# [0  4]  * [-7, 1]
#
# a1 = -2 a2 = 1  a3 = 0 a4 = 4
# b1 = 6, b2 = 5, b3 = -7 b4= 1
#
# First iteration:
# a1 * b1 + a2 * b3  => -2 * 6 + 1 * -7 = -19
#
# Second iteration:
# a1 * b2 + a2 * b4  => -2 * 5 + 1 * 1 = -9
#
# Third iteration:
# a3 * b1 + a4 * b3  => 0 * 6 + 4 * -7 = -28
#
# Fourth iteration:
# a3 * b2 + a4 * b4  => 0 * 5 + 4 * 1 = 4

first_matrix = [[-2, 1],
                [0, 4]]

second_matrix = [[6, 5],
                 [-7, 1]]

result = [[0,0],
          [0,0]]

for f_row in range(len(first_matrix)):
    for s_col in range(len(second_matrix[0])):
        for s_row in range(len(second_matrix)):
            result[f_row][s_col] += first_matrix[f_row][s_row] * second_matrix[s_row][s_col]

for r in result:
    print(r)









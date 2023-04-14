
import numpy as np

infinite = True
while infinite:
    # Prompt user to enter the value for a matrix
    r = input("What value would you like to enter into the matrix: ")
    # Create matrix including the input of the user
    r = float(r)
    buffalo = np.array([[0, 0, r], [0.6, 0, 0], [0, 0.75, 0.95]])
    determinant = np.linalg.det(buffalo)
    if determinant == 0.0:
        print("Please enter a different number as the number you entered will cause the universe to end")

    else:
        # Print out the matrix
        infinite = False
        print(buffalo)


# Calculate Eigenvalues & Eigenvectors

eig_values, eig_vectors = np.linalg.eig(buffalo)
print("Eigenvalues:")
print(eig_values)
print("Eigenvectors:")
print(eig_vectors)

# Invert Eigenvalues & Eigenvectors
inverse = np.linalg.inv(eig_vectors)

# Choose x0
negative = True
while negative:
    juvenile = int(input("Please enter a positive integer to represent the starting population of juvenile water buffalo: "))
    adolescent = int(input("Please enter a positive integer to represent the starting population of adolescent water buffalo: "))
    adult = int(input("Please enter a positive integer to represent the starting population of adult water buffalo: "))
    if juvenile < 0 | adolescent < 0 | adult < 0:
        print("Please enter a POSITIVE integer!")
    else:
        negative = False

# Make x_0 vector
x_0 = np.array([[juvenile], [adolescent], [adult]])
print(x_0)

# Multiply inverse and x_0 vector
constant = np.multiply(inverse, x_0)

print(constant)

def round_matrix_3x3(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = '%.2f' % matrix[i][j]
    print(matrix)

list = np.array([[3, 4.242424, 3], [2,3,4], [5.88889, 4.233333333, 16]])

print(list)

round_matrix_3x3(list)
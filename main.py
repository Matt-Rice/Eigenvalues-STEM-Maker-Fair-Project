
# @Author Matt Rice & Fanni Kertesz
# @Version 3-11-23
# main.py
# Class


import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

# How to invert a matrix
# a = np.matrix([[2, 0],[0, 2]])
# print(np.linalg.inv(a))

# a = np.matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
#
# b = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], ])
#
# c = np.matrix([[0.4, .3], [1.6, 1.2]])
# print("c = ")
# print(c)

# w, v = np.linalg.eig(c)
# print("Eigenvalues:")
# print(w)
# print("Eigenvectors:")
# print(v)

# Assume that I loaded 'N' no of 2d points from a file and used
# np.cov() to find the below covariance matrix

# This is my covariance matrix obtained from 2 x N points
# cov_mat = [[0.4, 0.3], [1.6, 1.2]]
#
# eigen_values, eigen_vectors = la.eig(cov_mat)
#
# origin = [0, 0]
#
# eig_vec1 = eigen_vectors[:, 0]
# eig_vec2 = eigen_vectors[:, 1]
#
# print(eig_vec1)
# print(eig_vec2)


# This line below plots the 2d points

# c = eig_vec1
# d = eig_vec2
# plt.scatter(c, d)
#
# plt.show()

# Give background on what the program does, will be used in the window
background = None

infinite = True
while infinite:
    # Prompt user to enter the value for a matrix
    p = input("What value would you like to enter into the matrix: ")
    # Create matrix including the input of the user
    p = float(p)
    owl_mouse = np.array([[0.4, 0.3], [p, 1.2]])
    determinant = np.linalg.det(owl_mouse)
    if determinant == 0.0:
        print("Please enter a different number as the number you entered will cause the universe to end")

    else:
        # Print out the matrix
        infinite = False
        print(owl_mouse)


# Calculate Eigenvalues & Eigenvectors

eig_values, eig_vectors = np.linalg.eig(owl_mouse)
print("Eigenvalues:")
print(eig_values)
print("Eigenvectors:")
print(eig_vectors)

# Invert Eigenvalues & Eigenvectors
inverse = np.linalg.inv(eig_vectors)

# Choose x0
negative = True
while negative:
    owls = int(input("Please enter a positive integer to represent the starting population of the owls: "))
    mice = int(input("Please enter a positive integer to represent the starting population of the mice: "))
    if owls < 0 | mice < 0:
        print("Please enter a POSITIVE integer!")
    else:
        negative = False

# Make x_0 vector
x_0 = np.array([[owls], [mice]])
print(x_0)

# Multiply inverse and x_0 vector
constant = np.multiply(inverse, x_0)

print(constant)




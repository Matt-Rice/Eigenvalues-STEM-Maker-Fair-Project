import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd


# Rounding a two-dimensional matrix
def round_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = '%.2f' % matrix[i][j]
    print(matrix)


# Function to round the entries within a vector to two decimal places
def round_array(array):
    for i in range(len(array)):
        array[i] = '%.2f' % array[i]
    print(array)


# Function to round an imaginary number to two decimal places
def round_imaginary(num):
    return complex(round(num.real, 2), round(num.imag, 2))


# Function to round a matrix with imaginary entries
def round_imaginary_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = round_imaginary()
    print(matrix)


window = Tk()
window.geometry('1024x768')

# Prompt user to enter the value for a matrix
prompt = Label(window, text="What value would you like to enter into the matrix: ", font=('Times New Roman', 12))
prompt.pack()


def submit():
    infinite = True
    while infinite:

        # Create matrix including the  one input of the user
        p = float(entry.get())
        owl_mouse = np.array([[0.4, 0.3], [p, 1.2]])
        determinant = np.linalg.det(owl_mouse)
        if determinant == 0.0:
            non_invertible = Label(window,
                text="Please enter a different number as the number you entered will cause the universe to end")
            non_invertible.pack()

        else:
            # Print out the matrix
            infinite = False
            matrix_text = Label(window, text="owl-mouse population dynamics matrix:", font=('Times New Roman', 12))
            matrix_print = Label(window, text=owl_mouse, font=('Times New Roman', 12))
            matrix_text.pack()
            matrix_print.pack()

    # Calculate Eigenvalues & Eigenvectors
    eig_values, eig_vectors = np.linalg.eig(owl_mouse)

    # Round eigenvalues and eigenvectors
    round_array(eig_values)
    round_matrix(eig_vectors)

    eig_vectors = -1 * eig_vectors

    eigenprint1 = Label(window, text="Eigenvalues:", font=("Times New Roman", 12))
    eigenprint2 = Label(window, text=eig_values, font=("Times New Roman", 12))
    eigenprint3 = Label(window, text="Eigenvectors", font=("Times New Roman", 12))
    eigenprint4 = Label(window, text=eig_vectors, font=("Times New Roman", 12))

    eigenprint1.pack()
    eigenprint2.pack()
    eigenprint3.pack()
    eigenprint4.pack()

    # Invert Eigenvalues & Eigenvectors
    inverse = np.linalg.inv(eig_vectors)

    # Choose x0
    owl_prompt = Label(window,
                           text="Please enter a positive integer to represent the starting population of the owls: ",
                           font=("Times New Roman", 12))
    owl_enter = Entry(window, font=("Times New Roman", 12))
    owl_prompt.pack()
    owl_enter.pack()

    mice_prompt = Label(window,
                            text="Please enter a positive integer to represent the starting population of the mice: ",
                            font=("Times New Roman", 12))
    mice_enter = Entry(window, font=("Times New Roman", 12))
    mice_prompt.pack()
    mice_enter.pack()

    # Function to submit the x0 value
    def submit_x0():
        owls = int(owl_enter.get())
        mice = int(mice_enter.get())

    # Make x_0 vector

        x_0 = np.array([[owls], [mice]])
        print(x_0)

        # Multiply inverse and x_0 vector
        constant = inverse @ x_0
        round_matrix(constant)

        result_text = Label(window,
                            text="constants for the linear combination of eigenvectors that make up the initial population: ",
                            font=("Times New Roman", 12))
        result = Label(window, text=constant, font=("Times New Roman", 12))
        result_text.pack()
        result.pack()

        # Plots the 2d points

        x_0_1 = x_0[0, 0]
        x_0_2 = x_0[1, 0]

        x0_5 = x_0
        x0_10 = x_0
        x0_1 = owl_mouse @ x_0
        for x in range(5):
            x0_5 = owl_mouse @ x0_5
        for x in range(10):
            x0_10 = owl_mouse @ x0_10

        # Converting constants into points

        x0_1_1 = x0_1[0, 0]
        x0_1_2 = x0_1[1, 0]

        x0_5_1 = x0_5[0, 0]
        x0_5_2 = x0_5[1, 0]

        x0_10_1 = x0_10[0, 0]
        x0_10_2 = x0_10[1, 0]

        owlX = np.array([x_0_1,x0_1_1,x0_5_1,x0_10_1])
        mouseY = np.array([x_0_2, x0_1_2, x0_5_2, x0_10_2])
        plt.scatter(owlX, mouseY, color='purple')
        plt.xlabel("Owl Population")
        plt.ylabel("Mice Population")
        plt.show()

    submit2 = Button(window, text="submit", font=('Times New Roman', 12), fg='#0e16a1', command=submit_x0)
    submit2.pack()

# ------------------------------------------------------------------------------------------------


# Function that will submit the input for the 3x3 buffalo matrix and calculate eigenvalues and eigenvectors
def submit_buff():
    # Prompt user to enter the value for a matrix
    b = entry.get()
    # Create matrix including the input of the user
    b = float(b)
    buffalo = np.array([[0, 0, b], [0.6, 0, 0], [0, 0.75, 0.95]])


    # Print out the matrix
    matrix_textb = Label(window, text="buffalo population dynamics matrix:", font=('Times New Roman', 12))
    matrix_print = Label(window, text=buffalo, font=('Times New Roman', 12))
    matrix_textb.pack()
    matrix_print.pack()

    # Calculate Eigenvalues & Eigenvectors
    eig_valuesb, eig_vectorsb = np.linalg.eig(buffalo)

    # Scale the Eigenvectors by -1 to make it positive
    eig_vectorsb = -1 * eig_vectorsb

    eigenprint5 = Label(window, text="Eigenvalues:", font=("Times New Roman", 12))
    eigenprint6 = Label(window, text=eig_valuesb, font=("Times New Roman", 12))
    eigenprint7 = Label(window, text="Eigenvectors", font=("Times New Roman", 12))
    eigenprint8 = Label(window, text=eig_vectorsb, font=("Times New Roman", 12))

    eigenprint5.pack()
    eigenprint6.pack()
    eigenprint7.pack()
    eigenprint8.pack()

    # Invert Eigenvectors
    inverseb = np.linalg.inv(eig_vectorsb)

    # Choose x0 for the Buffalo

    juvenile_prompt = Label(window,
                       text="Please enter a positive integer to represent the starting population of the juvenile buffalo: ",
                       font=("Times New Roman", 12))
    juvenile_enter = Entry(window, font=("Times New Roman", 12))
    juvenile_prompt.pack()
    juvenile_enter.pack()

    adolescent_prompt = Label(window,
                       text="Please enter a positive integer to represent the starting population of the adolescent buffalo: ",
                       font=("Times New Roman", 12))
    adolescent_enter = Entry(window, font=("Times New Roman", 12))
    adolescent_prompt.pack()
    adolescent_enter.pack()

    adult_prompt = Label(window,
                       text="Please enter a positive integer to represent the starting population of the adult buffalo: ",
                       font=("Times New Roman", 12))
    adult_enter = Entry(window, font=("Times New Roman", 12))
    adult_prompt.pack()
    adult_enter.pack()

    def submit_x0b():
        juvenile = int(juvenile_enter.get())
        adolescent = int(adolescent_enter.get())
        adult = int(adult_enter.get())

        # Make x_0 vector
        x_0b = np.array([[juvenile], [adolescent], [adult]])
        print(x_0b)

        # Multiply inverse and x_0 vector
        constantb = inverseb @ x_0b

        result_text = Label(window,
                        text="constants for the linear combination of eigenvectors that make up the initial population: ",
                        font=("Times New Roman", 12))
        result = Label(window, text=constantb, font=("Times New Roman", 12))
        result_text.pack()
        result.pack()
        x_0b_1 = x_0b[0, 0]
        x_0b_2 = x_0b[1, 0]
        x_0b_3 = x_0b[2, 0]

        x0_5b = x_0b
        x0_10b = x_0b
        x0_1b = buffalo @ x_0b
        for x in range(5):
            x0_5b = buffalo @ x0_5b
        for x in range(10):
            x0_10b = buffalo @ x0_10b

        # Converting constants into points

        x0_1_1b = x0_1b[0, 0]
        x0_1_2b = x0_1b[1, 0]
        x0_1_3b = x0_1b[2, 0]

        x0_5_1b = x0_5b[0, 0]
        x0_5_2b = x0_5b[1, 0]
        x0_5_3b = x0_5b[2, 0]

        x0_10_1b = x0_10b[0, 0]
        x0_10_2b = x0_10b[1, 0]
        x0_10_3b = x0_10b[2, 0]
        xb = np.array([x_0b_1, x0_1_1b, x0_5_1b, x0_10_1b])
        yb = np.array([x_0b_2, x0_1_2b, x0_5_2b, x0_10_2b])
        zb = np.array([x_0b_3, x0_1_3b, x0_5_3b, x0_10_3b])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xb, yb, zb)
        ax.set_xlabel('juvenile')
        ax.set_ylabel('adolescent')
        ax.set_zlabel('adult')
        plt.show()

    submitb = Button(window, text="submit",
                     font=('Times New Roman', 12), fg='#0e16a1', command=submit_x0b)
    submitb.pack()


submit2x2 = Button(window, text="submit the predator parameter for Owls vs Mice populations",
                   font=('Times New Roman', 12), fg='#0e16a1', command=submit)
submit3x3 = Button(window, text="submit the birthrate parameter for Buffalo population demographics",
                   font=('Times New Roman', 12), fg='#0e16a1', command=submit_buff)

entry = Entry()

window.config(bg='#a3b3ff')
entry.config(font=('Times New Roman', 12), bg='#f7f7f7')

entry.pack()
submit2x2.pack()
submit3x3.pack()
window.mainloop()

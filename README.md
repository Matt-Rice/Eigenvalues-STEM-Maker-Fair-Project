Eigen Values Program


Overview

This application is an interactive demonstration of the properties of eigenspaces with two examples of population dynamics, written in Python.
The program allows the user to enter in a value for one of the two matrices which describe a certain population dynamic in a system. One option
is the predator parameter for an owl v mouse population, and the second option is the birthrate parameter for a buffalo population. Once a value
is entered, the matrix with the value is presented as well as the eigenvalues and their corresponding eigenvectors of the matrix. Then, the user
may enter a value for the starting population of each of parts of the population. The user is presented with the eigenspace-coordinates of the
entered initial population, a few of the projected vectors, and a graph showing how the population changes over time.


Dependencies

The program requires the following dependencies:
- numpy
- pandas
- matplotlib
- tkinter


Usage

1. Run the program.
2. Enter a value into the prompt to generate a matrix.
3. The program will then display the selected population dynamics matrix and the calculated eigenvalues and eigenvectors.
4. Enter some initial populations.
5. The program will display the eigenspace-coordinates of the initial population, a few projections, and a graph showing the population changes over time.

Note: Program assumes reasonable values will be entered at prompts such as non-negative birthrate, positive population, etc.


Credits

This program was developed by Matt Rice and Fanni Kertesz as a project for the STEM-maker fair at Bellarmine University.


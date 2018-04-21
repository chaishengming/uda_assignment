import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self.g[0][0]
        if self.h == 2:
            return (self.g[0][0]*self.g[1][1]) - (self.g[0][1]*self.g[1][0])

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        else:
            return sum([self.g[i][i] for i in range(self.h) for j in range(self.h) if i==j])

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        import matrix
        if self.h == 1:
            m = matrix.Matrix([[1/self.g[0][0]]])
            return m
        if self.h == 2:
            if self.determinant() == 0:
                raise ZeroDivisionError("Matrix does not have an inverse if determinant equal to zero")
            else:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
                temp = 1/self.determinant()
                inverse = [[temp*d, -temp*b],
                           [-temp*c, temp*a]
                          ]
                m = matrix.Matrix(inverse)
                return m

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        import matrix
        T = [[self.g[i][j] for i in range(self.h)] for j in range(self.w)]
        m = matrix.Matrix(T)
        return m
                

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        import matrix
        matrix_add = [[self.g[i][j]+other.g[i][j] for j in range(self.w)] for i in range(self.h)]
        m = matrix.Matrix(matrix_add)
        return m
        
        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        matrix_neg = [[-1*self.g[i][j] for j in range(self.w)] for i in range(self.h)]
        import matrix
        m = matrix.Matrix(matrix_neg)
        return m

        


        #return self

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        matrix_sub = [[self.g[i][j]-other.g[i][j] for j in range(self.w)] for i in range(self.h)]
        import matrix
        m = matrix.Matrix(matrix_sub)
        return m

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if self.w != other.h:
            raise(ValueError, "number of columns of the pre-matrix must equal the number of rows of the post-matrix")    
        result = []
        row = []
        ele_of_matrix = 0
        for i in range(self.h):
            for j in range(other.w):
                ele_of_matrix = sum([self[i][k]*other.T()[j][k] for k in range(self.w)])
                row.append(ele_of_matrix)
            result.append(row)
            row = []
            
        # the second method
        # result = [[sum([self[i][k]*other.T()[j][k] for k in range(self.w)]) for j in range(other.w)] for i in range(self.h)]
        import matrix
        m = matrix.Matrix(result)
        return m 
                                         

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            result = []
            row = []
            for i in range(self.h):
                for j in range(self.w):
                    row.append(other*self.g[i][j])
                result.append(row)
                row = []
            import matrix
            m = matrix.Matrix(result)
            return m
            #the second method
            #return [[other*self.g[i][j] for j in range(self.w)] for i in range(self.h)]
            
            
            
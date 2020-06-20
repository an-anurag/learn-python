class A: pass


class B(A): pass


class C(A): pass


class D(B, C):
    def m1(self):
        pass


c = D()
c.m1()
D.mro()


#################################################

class A: pass  # A, object


class B: pass  # B, object


class C: pass  # C, object


class X(A, B): pass  # X, A, B, object


class Y(B, C): pass  # Y, B, C, object


class P(X, Y, C): pass  # P, X, A, Y, B, C, object


A.mro()

#########################################################
# Running C3 algorithm on above

"""
    1. c3 algorithm
        1. mro(X) = X + merge(mro(P1), mro(P2), parent list ie. P1P2)
        1. If head element of first list not present in the tail part of any other list then consider that element in the 
           result and remove that element from all the lists. else leave the first list and consider the next list 
           XABO => X is the head, rest ABO is the tail

mro(P) = P + Merge(mro(X), mro(Y), mro(C), XYC)
       = P + Merge(XABO, YBCO, CO, XYC)
       = P + X + Merge(ABO, YBCO, CO, YC)
       = P + X + A + Merge(BO, YBCO, CO, YC)
       = P + X + A + Y + Merge(BO, BCO, CO, C)
       = P + X + A + Y + B + Merge(O, CO, CO, C)
       = P + X + A + Y + B + C + Merge(O, O, O)
       = P + X + A + Y + B + C + O
"""

############################################################

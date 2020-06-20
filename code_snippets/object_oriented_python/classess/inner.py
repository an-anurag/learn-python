class A:

    def __init__(self):
        self.b = None

    def amethod(self):
        pass

    class B:
        def __init__(self):
            self.a = A()

        def bmethod(self):
            pass
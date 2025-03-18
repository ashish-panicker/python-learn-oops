class A:
    def method(self):
        return "A's method"


class B(A):
    def method(self):
        return super().method() + " then B's method"


class C(A):
    def method(self):
        return super().method() + " then C's method"


class D(B, C):
    """
    class D is inherting from B, C
    """
    def method(self):
        return super().method() + " then D's method"


d = D()
print(D.__mro__)  # D -> B -> C -> A
print(d.method()) # Output of this statement?
"""
D.method() -> B.method() -> C.method() -> A.method()
A's method then C's method then B's method then D's method
"""
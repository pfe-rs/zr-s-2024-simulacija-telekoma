class Symbol:
    def __init__(self, I, Q):
        self.I = I
        self.Q = Q

    def __repr__(self):
        return f"I: {self.I}, Q: {self.Q}"
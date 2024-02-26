class bird:
    def fly(self):
        raise NotImplementedError
class eagle(bird):
    def fly(self):
        print("very fast")
    pass
Eagle=eagle()
Eagle.fly()
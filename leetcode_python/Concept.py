class Shark:

    animal_type = "fish"

    def __init__(self):
        animal_gender = "male"
        self.animal_name = "sShark"


    def dum(self):
        # Wrong, cannot see animal_type

        # if animal_type == "fish":
        #     print("fish")

        if self.animal_type == "fish":
            print("fish")

        # # Wrong
        # if animal_name == "sShark":
        #     print("sShark")

        # Correct
        if self.animal_name == "sShark":
            print("sShark")

        # Wrong, object has no attribute 'animal_gender'
        # if self.animal_gender == "male":
        #     print("male")

x = 5

class Example:

    def __init__(self):
        self.ex1 = "dum"

    def dum(self):
        ex1 = "bad"
        self.ex2 = "ex2"
        # print(ex1)

def foobar():
    x = 10
    print(x)

if __name__ == "__main__":
    # S = Shark()
    # S.dum()
    foobar()
    E = Example()
    # E.dum()
    print(E.ex1)
    print(E.ex2)
import random

subjects = ["EPS", "HG", "INF", "EI", "ANG", "AR", "FR", "MATH", "PH", "PC", "SVT"]
Mark2 = []
Coefficient = []
x = 0

def function(y):
    global x
    Mark1 = []

    def fun():
        rand = random.randint(1, 3)
        if rand == 1:
            print(a)
        elif rand == 2:
            print(b)
        elif rand == 3:
            print(c)

    try:
        num_ex: int = int(input(f"How many exams in {y}: "))
    except ValueError:
        print("Please enter a number next time and without comma.")
        quit()
    else:
        if num_ex != 0:
            for n in range(num_ex):
                mark: float = float(input("How much did you get? "))
                if 17 <= mark <= 20:
                    a: str = "EXCELLENT! Continue that way."
                    b: str = "Wow! You surprised me. Good job."
                    c: str = "Congratulations boy!"
                    fun()
                elif 15 <= mark < 17:
                    a: str = "You could do better, anyway you did well."
                    b: str = "Hmmm... Nice, concentrate and practice more."
                    c: str = "Good, but not excellent."
                    fun()
                elif 13 <= mark < 15:
                    a: str = "You MUST definitely improve!"
                    b: str = "Too low! Unexpected from you."
                    c: str = "No work, no better marks!"
                    fun()
                else:
                    print("Sorry for you but you went too bad this time, I am not satisfied... AT ALL! :(")
                Mark1.append(mark)
                Mark2.append(mark)
                Coefficient.append(coefficient)

            average: float = float(sum(Mark1) / len(Mark1))
            L4 = [w * j for w, j in zip(Coefficient, Mark2)]
            global_average: float = round(sum(L4) / sum(Coefficient), 2)
            x = global_average
            print(f"The average mark of {i} is: {average}/20.")
            return x
        else:
            return x

for i in subjects:
    if i == "MATH" or i == "PC" or i == "SVT":
        coefficient = 4
    elif i == "FR" or i == "ANG":
        coefficient = 3
    elif i == "AR" or i == "PH" or i == "HG" or i == "EI" or i == "EPS" or i == "INF":
        coefficient = 2
    glob_average = function(i)

print(f"Your global mark is {glob_average}/20")

# That's a project made by MYSELF,so proud of it, also because I had to work hard to solve some issues.
# Thanks for trying it...         SIGNATURE:
#                                    Haitam Laghmam

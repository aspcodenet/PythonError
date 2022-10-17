#Raise own Exceptions
# (usecase - def __init__ )
# usecase SetAge(self, int)
def CalculateSalary(hourlySalary:int, hoursWorked:int ) -> int:
    if hoursWorked < 0:
        raise ValueError("Hours worked cant be less than 0")
    salary = hourlySalary * hoursWorked
    if hoursWorked > 10:
        salary = salary * 1.2
    return salary

try:
    a = CalculateSalary(10,-5)
    print(a)
except ValueError:
    print("dsda")




while True:
    try:
        tal1Input = input("Ange tal 1:")
        tal1 = int(tal1Input)
        tal2Input = input("Ange tal 2:")
        tal2 = int(tal2Input)
        tal3 = tal1 / tal2
        print(tal3)
        break
    except ValueError:
        print("Verkar inte vara ett tal")
    except ZeroDivisionError:
        print("Tal2 får inte vara 0")
    except:
        print("Ngt jätteknas - mail skickat till utvecklaren så ska den få pisk!")

# while True:
#     try:
#         tal1Input = input("Ange tal 1:")
#         tal1 = int(tal1Input)
#         break
#     except:
#         print("Ange siffror tack")


# while True:
#     try:
#         tal2Input = input("Ange tal 2:")
#         tal2 = int(tal2Input)
#         break
#     except:
#         print("Ange siffror tack")

# try:
#     tal3 = tal1 / tal2
#     print(tal3)
# except:    
#     print("Ngt fick fel")

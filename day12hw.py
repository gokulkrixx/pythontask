import re
name = input("Enter Your Name ")
feedback = input("Enter Your feedback ")

try:
    if name == "":
        raise ValueError("ERROR...Name field is Empty")
    if feedback == "":
        raise ValueError("ERROR....Feedback field is Empty")
except ValueError as error:
    print(error)

else:
    print(f"""Name: {name}
feedback: {feedback}
Thank you for your valueable feedback""")

finally:
    print("OPus CuiSine")
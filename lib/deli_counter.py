def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently: " + " ".join([f"{i+1}. {person}" for i, person in enumerate(deli_line)])
        print(line_str)

def take_a_number(deli_line, person):
    deli_line.append(person)
    print(f"Welcome, {person}. You are number {len(deli_line)} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving_person = deli_line.pop(0)
        print(f"Currently serving {serving_person}.")

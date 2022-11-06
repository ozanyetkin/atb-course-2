def proper_answer(possible, answer):
    while answer not in possible:
        answer = input("Give me a proper answer: ")
    return answer

proper = proper_answer(["y", "n"], answer=input("Give me an answer: "))

if proper == "y":
    print("HELL YES")
if proper == "n":
    print("FUCK NO")

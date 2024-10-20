

# todo Phrase or Word Inverse

# ? Create a function that inverts words or the phrase depending on the value of parameter type. A "P" 
# ? means to invert the entire phrase, while a "W" means to invert every word in the phrase. See the following examples for clarity.
# ? Examples

# ? inverter("This is Valhalla", "P") ➞ "Valhalla is this"

# ? inverter("One fine day to start", "W") ➞ "Eno enif yad ot trats"

# ? inverter("Division by powers of two", "P") ➞ "Two of powers by division"

# ! Notes

#     * The first character of the returned string should be in uppercase and the rest are in lowercase.
#     * There will be no empty strings as inputs. Punctuation marks, though quite important for grammatical correctness, are discounted in the input phrases.

# , type


# def inverter(txt, type):
#    mylist = []

#    if type == "P":
#         lst= txt.split(" ")
#         return " ".join(list(reversed(lst))).capitalize()
#    elif  type == "W":
#         lst4= txt.split(" ")
#         for x in lst4:
#             lst3= x.split(" ")
#             " ".join.list(reversed(lst3))
#             mylist.append(" ".join.list(reversed(lst3)))
#         return " ".join(mylist)
# print(inverter("This is valhalla","P"))
# print(inverter("One fine day to start", "W"))

def inverter(txt, inversion_type):
    if inversion_type == "P":
        # Invert the entire phrase and capitalize
        return " ".join(list(reversed(txt.split(" ")))).capitalize()
    elif inversion_type == "W":
        # Invert each word in the phrase and join them
        return " ".join([word[::-1] for word in txt.split()]).capitalize()

# Test cases
print(inverter("This is valhalla", "P"))  # Expected: "Valhalla is this"
print(inverter("One fine day to start", "W"))  # Expected: "Eno enif yad ot trats"


# ! ///////////////////////////////////////////////////////////////////////////////////////

def inverter(txt, inversion_type):
    if inversion_type == "P":
        # Invert the entire phrase and capitalize
        return " ".join(list(reversed(txt.split(" ")))).capitalize()
    elif inversion_type == "W":
        # Invert each word in the phrase and join them
        return " ".join([word[::-1] for word in txt.split()]).capitalize()

# Test cases
print(inverter("This is valhalla", "P"))  # Expected: "Valhalla is this"
print(inverter("One fine day to start", "W"))  # Expected: "Eno enif yad ot trats"

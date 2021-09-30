

# filter_fn=lambda script_name: True if isinstance(script_name, str) else False 

# print(filter_fn("A"))
# print(filter_fn(False))

# filter_fn2=lambda script_name: True



filter_fn3=lambda x : True if x.split(".")[1] == "py" else False 

print(filter_fn3("ASDA.py"))
print(filter_fn3("ASDA.csv"))


def filter_py(script):
    if script.split(".")[1] == "py":
        return True 




print("Round 2")
filter_fn2=lambda x: filter_py(x)

print(filter_fn2("ASDA.py"))
print(filter_fn2("ADSA.csv"))

# dictionary stores unique key:value pair

monthconversion = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december"
}

print(monthconversion["oct"])
print(monthconversion.get("nov"))
print(monthconversion.items())
print(monthconversion.values())
print(monthconversion.copy())
print(monthconversion.pop("dec"))
print(monthconversion.values())
print(monthconversion.popitem())
print(monthconversion.values())
print(monthconversion.clear())
print(monthconversion.values())
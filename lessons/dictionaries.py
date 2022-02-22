"""Demonstrations of dictionary capabilities."""

# declar a dictionary variable
schools: dict[str, int]

# initialize empty dictionary
schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)
print(f"UNC has {schools['UNC']}")

# remove a key value pair from dictionary
schools.pop("Duke")

# test for a existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Is Duke present: {is_duke_present}")

# update key value pair
schools["UNC"] = 2000
schools["NCSU"] += 200

# demonstration of dictionary literal
schools = {}  # same as dict()

# alternatively, initialize key value pair
schools = {
    "UNC": 19400, 
    "Duke": 6717, 
    "NCSU": 26150
}
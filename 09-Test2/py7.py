#(p7.py) A valid username consists of 4 to 12 characters: lowercase letters, numbers and the underscore character. 
# Create a function f(arr) that, for a given array of usernames, returns the number of valid usernames in the array. Example:
#f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  

def f(arr):
    num=0

    for row in arr:
        if len(row)<=12 and len(row)>=4:
            if row.lower()==row:
                if any(char.isdigit() for char in row):
                    if "_" in row:
                        num+=1

    return num

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
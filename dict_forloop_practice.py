x = {"randy" : "active" , "nicole" : "active","jericho" : "inactive","jemuel" : "active"} 
#initiated a dictionary



for name , status  in x.items(): # in this im looping over x storing the key in the name var and the value to the status var and 
    if status == "inactive": # it checks  the  status  if it is inactive
        print("this user : " + name + " is " + status) # once inactive is found in the status of the dictionary  it executes this printing code
    elif name == "jemuel": # also it checks  if the name var is equal to "jemuel"
        print("bading ka talaga ", name) # also if found that name var is equal to "jemuel" it executes this code 


        #  Just a small logic note: If someone is both inactive and named jemuel, only the first if block will execute — the elif won’t run because if already matched. 
        # But in this code, "jemuel" is "active", so only the elif triggers.
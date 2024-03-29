import re
'''
1. Create a simple String calculator with a method signature:
———————————————
int Add(string numbers)
———————————————
The method can take up to two numbers, separated by commas, and will return their sum. 
for example “” or “1” or “1,2” as inputs.
(for an empty string it will return 0) 

2. Allow the Add method to handle an unknown amount of numbers

3. Allow the Add method to handle new lines between numbers (instead of commas).
the following input is ok: “1\n2,3” (will equal 6)
the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)
'''
def add(params: str)-> int:
    
    if params == "" or params is None:
        return 0
    elif len(str(params))==1:
        return int(params)
    else:
        delimiters= "[,|\n]"
        params_list = map(int,re.split(delimiters,str(params)))
        return sum(params_list)
    




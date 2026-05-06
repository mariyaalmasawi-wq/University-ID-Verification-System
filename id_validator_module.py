import re

def match(task) :
    pattern = r"(44|45|46)\d{7}$"
    x = re.search(pattern, task)
    if x:
       return "Yes"
    else :
       return "No"
    

def matching_parts(task) :
    pattern = r"(?:44|45|46)\d{7}$"
    x = re.findall(pattern, task)
    if x :
      return x 
    else :
       return "nothing"



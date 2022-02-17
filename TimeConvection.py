

def Time(s):
    """
    This funtion takes in a string time as a parameter and then converts it to 
    military time
    """
    if "PM" in s:
        s = s.rstrip("PM").split(":")
        if s[0] =="12":
            return ":".join(s)
        else:
            time = int(s[0])+12
            for i in s[1:]:
                time = str(time) + ":" +i
            return time


    elif "AM" in s:
        s = s.rstrip("AM").split(":")
        if s[0] =="12":
            time_h = "00"
            for i in s[1:]:
                time_h = time_h +":"+ i
            return time_h
        else:
            return ":".join(s)
        

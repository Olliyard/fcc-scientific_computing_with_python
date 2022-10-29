def add_time(start, duration, start_day=""):
    # ------- Setup -------
    #Split start time into hours, minutes and period (AM/PM)
    parts = start.split()
    hour, minutes = parts[0].split(":")
    period = parts[1]
    days_later = 0

    if(period == "PM"):
        hour = int(hour) + 12
    
    #Split duration into hours and minutes
    parts = duration.split()
    d_hour, d_minutes = parts[0].split(":")
    
    #Add hours and minutes (start hour expressed in 24-hour format)
    new_hour = int(hour) + int(d_hour)
    new_min = int(minutes) + int(d_minutes)


    # ------- Minutes calculations ------- #
    #If there are more minutes than intended (60) Convert minutes to hours and save overflow (64 min -> 1 hour, 4 min)
    if new_min >= 60:
        temp = new_min // 60
        new_min -= temp * 60
        new_hour += temp
        
    if (new_min < 10):
        new_min = f"0{new_min}" # adds zero as padding if minutes is below 10.


    # ------- Hours calculations ------- #
    #Hours in 24 hour format
    if new_hour > 24:
        days_later = new_hour // 24
        new_hour -= days_later * 24

    #Conversion from 24-hour format to 12-hour format (ERROR WHEN around 11.59pm -> am)
    if new_hour > 0 and new_hour < 12:
        period = "AM"
        
    elif new_hour == 12:
        period = "PM"
        
    elif new_hour > 12:
        period = "PM"
        new_hour -= 12

    else:
        period = "AM"
        new_hour += 12
    
    
    # ------- Days from start time ------- #
    #Calculate days later from start time
    if days_later > 0:
        if days_later == 1:
            days_string = "(next day)"
        else:
            days_string = f"({days_later} days later)"
    else:
        days_string = ""
    
    
    # ------- Setting new_time return values ------- #
    #Set the values for new_time when date is excluded
    if not start_day:
        if days_later:
            new_time = f"{new_hour}:{new_min} {period} {days_string}"
        else:
            new_time = f"{new_hour}:{new_min} {period}"
    
    
    # ------- With days included ------- #
    if start_day:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        #Convert string to lowercase, uppercase first letter so it fits the weekdays list elements.
        start_day = start_day.lower().capitalize()
        
        #Get the remainder from the sum of index element for day given and days later
        final_day = (weekdays.index(start_day) + days_later) % 7
        final_day = weekdays[final_day]
        
        if not days_string:
            new_time = f"{new_hour}:{new_min} {period}, {final_day}"
        
        else:
            new_time = f"{new_hour}:{new_min} {period}, {final_day} {days_string}"

    return new_time

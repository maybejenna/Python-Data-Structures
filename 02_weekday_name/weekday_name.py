def weekday_name(day_of_week):
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if 0 < day_of_week < 8:
        return days_of_week[day_of_week-1]
    else:
        return "None"
    # """Return name of weekday.
    #
    #     >>> weekday_name(1)
    #     'Sunday'
    #
    #     >>> weekday_name(7)
    #     'Saturday'
    #
    # For days not between 1 and 7, return None
    #
    #     >>> weekday_name(9)
    #     >>> weekday_name(0)
    # """

print (weekday_name(1))
print (weekday_name(0))
print (weekday_name(7))
print (weekday_name(8))


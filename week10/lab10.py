# 1. Name:
#      Margaret Binns
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      Take two dates and calculate the number of days between them.
# 4. What was the hardest part? Be as specific as possible.
#      It was all fine and dandy until the math wasn't skadoodling the way I wanted it to and the math wasn't working.
# 5. How long did it take for you to complete the assignment?
#      6 hours cause math


    

def IsLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def GetYear(startOrEnd):
    year = 0

    while year < 1753:
        try:
            year = int(input(f"What is the {startOrEnd} year? "))
        except:
            print ("The year must be an int. Try again.")
            continue

        if year < 1753:
            print ("Must be a year above 1753. Try again.")

    assert isinstance(year,int), "year must be an int."
    assert year >= 1753, "year must be larger than 1753."

    return year

def GetMonth(startOrEnd):
    month = 0

    while month > 12 or month < 1:
        try:
            month = int(input(f"What is the {startOrEnd} month? "))
        except:
            print ("The month must be an int. Try again.")
            continue
            
        if month > 12 or month < 1:
            print ("Must be a valid month (1-12).")

    assert isinstance(month,int), "month must be an int."
    assert month >= 1 and month <= 12, "month must be in range 1-12."

    return month

def GetDay(startOrEnd, month, isLeapYear):
    day = 0
    lowerLimit = 1
    upperLimit = MonthDayTotal(month, isLeapYear)

    while day < lowerLimit or day > upperLimit:
        try:
            day = int(input (f"What is the {startOrEnd} day? "))
        except:
            print ("The day must be an int. Try again.")
            continue
            
        if day < lowerLimit or day > upperLimit:
            print (f"Day must be in range {lowerLimit}-{upperLimit}.")

    assert isinstance(day,int), "day must be an int."
    assert day >= lowerLimit and day <= upperLimit, "day must be valid range depending on month and/or leap year."

    return day

def MonthDayTotal(month, isLeapYear):
    assert 1 <= month <= 12, "month is not in valid range" 

    monthThirty = [4,6,9,11]
    monthThirtyOne = [1,3,5,7,8,10,12]
    
    if month in monthThirty:
        monthTotal = 30

    elif month in monthThirtyOne:
        monthTotal = 31

    elif month == 0 or month == 13:
        monthTotal = 0

    elif month == 2 and isLeapYear == False:
        monthTotal = 28

    elif month == 2 and isLeapYear == True:
        monthTotal = 29

    return monthTotal

def YearDayTotal(isLeapYear):
    if isLeapYear == False:
        yearDayCount = 365

    elif isLeapYear == True:
        yearDayCount = 366

    return yearDayCount

def PartialMonthStart(month, day, isLeapYear):
    monthTotal = MonthDayTotal(month, isLeapYear)
    partialMonthCount = monthTotal - day

    return partialMonthCount

def PartialMonthEnd(day):
    #this is redundant but it makes things make sense (syntactic sugar)
    return day


def PartialYearStart(month, day, isLeapYear):
    dayCountPerMonth = 0

    if (month + 1) < 13:
        for i in range((month+1),13):
            monthTotal = MonthDayTotal(i, isLeapYear)
            dayCountPerMonth = dayCountPerMonth + monthTotal
    elif (month + 1) == 13:
        monthTotal = MonthDayTotal(12, isLeapYear)
        dayCountPerMonth = dayCountPerMonth + monthTotal

    partialYearTotal = dayCountPerMonth + PartialMonthStart(month, day, isLeapYear)

    return partialYearTotal

def PartialYearEnd(month, day, isLeapYear):
    dayCountPerMonth = 0
    if (month) > 1:
        for i in range(1, (month)):
            monthTotal = MonthDayTotal(i, isLeapYear)
            dayCountPerMonth = dayCountPerMonth + monthTotal
    elif (month) == 1:
        monthTotal = MonthDayTotal(1, isLeapYear)
        dayCountPerMonth = dayCountPerMonth + monthTotal

    dayCountPerMonth = dayCountPerMonth + PartialMonthEnd(day)

    return dayCountPerMonth

def FullYearCount(startYear, endYear):
    return endYear - startYear

def SameYearCount(startMonth, endMonth, startDay, endDay, isLeapYear):
    startMonthCount = PartialMonthStart(startMonth, startDay, isLeapYear)
    endMonthCount = PartialMonthEnd(endDay)
    betweenMonthCount = 0

    if (startMonth + 1) < (endMonth - 1):
        for i in range(startMonth + 1, endMonth - 1):
            betweenMonthCount = betweenMonthCount + MonthDayTotal(i, isLeapYear)
    elif (startMonth + 1) == (endMonth - 1):
        betweenMonthCount = betweenMonthCount + MonthDayTotal(startMonth + 1, isLeapYear)

    return startMonthCount + endMonthCount + betweenMonthCount

def SameMonthCount(startDay, endDay):
    return endDay - startDay

def DifferentYearCount(startYear, startMonth, startDay, endYear, endMonth, endDay, startIsLeapYear, endIsLeapYear):
    partialStartYear = PartialYearStart(startMonth, startDay, startIsLeapYear)
    partialEndYear = PartialYearEnd(endMonth, endDay, endIsLeapYear)
    betweenYearCount = 0

    if (startYear + 1) < (endYear - 1):
        for i in range(startYear + 1, endYear):
            isBetweenYearLeapYear = IsLeapYear(i)
            yearDayCount = YearDayTotal(isBetweenYearLeapYear)
            betweenYearCount = betweenYearCount + yearDayCount
    elif (startYear + 1) == (endYear - 1):
        yearDayCount = YearDayTotal(startIsLeapYear)
        betweenYearCount = betweenYearCount + yearDayCount

    return partialStartYear + betweenYearCount + partialEndYear

def Main():
    isValid = False

    while isValid == False:
        startYear = GetYear("start")
        isStartLeapYear = IsLeapYear(startYear)
        startMonth = GetMonth("start")
        startDay = GetDay("start", startMonth, isStartLeapYear)

        endYear = GetYear("end")
        if endYear < startYear:
            print("Start year should be larger than end year.")
            continue
        isEndLeapYear = IsLeapYear(endYear)
        endMonth = GetMonth("end")
        if endYear == startYear and endMonth < startMonth:
            print("Start month should be larger than end month.")
            continue
        endDay = GetDay("end",endMonth, isEndLeapYear)
        if endMonth == startMonth and endDay < startDay:
            print ("Start day should be larger than end day.")
            continue
        isValid = True
        
    if startYear == endYear:
        if startMonth == endMonth:
            totalDays = SameMonthCount(startDay, endDay)
        else:
            totalDays = SameYearCount(startMonth, endMonth, startDay, endDay, isStartLeapYear)

    else:
        totalDays = DifferentYearCount(startYear, startMonth, startDay, endYear, endMonth, endDay, isStartLeapYear, isEndLeapYear)

    print (f"the total number of days between the start date of {startMonth}/{startDay}/{startYear} and the end date of {endMonth}/{endDay}/{endYear} is {totalDays}.")


            
if __name__ == "__main__":
    Main()
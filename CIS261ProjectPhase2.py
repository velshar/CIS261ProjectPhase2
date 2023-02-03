#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter the from date (mm/dd/yyyy): ")
    todate = input("Enter the to date (mm/dd/yyyy): ")
    return fromdate, todate

#write the GetHoursWorked function
def GetHoursWorked():
    hrsWrkd = (input("Enter hours worked: "))
    return float(hrsWrkd)

#write the GetHourlyRate function
def GetHourlyRate():
    hrlyRate = (input("Enter hourly rate: "))
    return float(hrlyRate)
    

# write the GetTaxRate function

def GetTaxRate():
    taxRate = (input("Enter tax Rate : "))

    taxRate = taxRate

    return float(taxRate)


def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

    
def PrintInfo(empname, toDate, fromDate, hours, hourlyrate, taxrate, calcGrossPay, calcIncomeTax, calcNetPay):   
    
    print()
    print("Name:  ", empname) 
    print("From Date:   ",fromDate)
    print("To Date:  ",toDate)
    print("Hours Worked:  ", f"{hours:.2f}")   
    print("Hourly Rate:  ",hourlyrate)
    print("Gross Pay:  ",calcGrossPay)
    print("Tax Rate:  ", taxrate)
    print("Income Tax: ",calcIncomeTax)
    print("Net Pay: ",calcNetPay)
        

def PrintTotals(allTotals):    

    print()
    print("Total Number Of Employees: ", allTotals[0])
    print(f"Total Hours Worked: {allTotals[1]:.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"Totalgross Pay {allTotals[2]:.2f}")
    print(f"Total Tax: {allTotals[3]:.2f}")
    print(f"Total Net Pay: {allTotals[4]:.2f}")

if __name__ == "__main__":

    #These are the totals for the employees.
    TotHours = 0.00
    TotHourRate = 0.00 #Added this to capture hourly rate.
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    TotIncomeTax = 0.00

    empNameList = []
    totHoursList = []
    totHoursRate = []
    toDatesList = []
    fromDateList = []
    totTaxRateList = []

    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break

        fromdate, todate = GetDatesWorked()
        TotHours = GetHoursWorked()
        TotHourRate = GetHourlyRate()
        TotTax = GetTaxRate()        

        empNameList.append(empname)
        toDatesList.append(todate)
        fromDateList.append(fromdate)
        totHoursList.append(TotHours)
        totHoursRate.append(TotHourRate)
        totTaxRateList.append(TotTax)

        #print(empNameList +  totHoursList  + totHoursRate )

        #This will pring out the details of the employee.
        #PrintInfo(empname,TotHours,TotHourRate,TotGrossPay,TotTax,TotIncomeTax,TotNetPay)
               
    
    i = 0
    allTotals = [0, 0, 0, 0, 0]
    while i < len(empNameList):
        #print(empNameList[i])
        calcGrossPay, calcIncomeTax, calcNetPay = CalcTaxAndNetPay(totHoursList[i],totHoursRate[i],totTaxRateList[i])

        PrintInfo(empNameList[i],toDatesList[i],fromDateList[i],totHoursList[i],totHoursRate[i],totTaxRateList[i],calcGrossPay, calcIncomeTax, calcNetPay)       


        ##This is counting for the entire company.
        #Employee count
        allTotals[0] = (i+1)
        #Employee Hours worked
        allTotals[1] += totHoursList[i]   
        #Employee gross pay
        allTotals[2] += calcGrossPay
        #Employee income tax
        allTotals[3] += calcIncomeTax
        #Employee ney pay
        allTotals[4] += calcNetPay

        i +=1
        

    #print(allTotals)
    #Information about all employees and company.    
    PrintTotals(allTotals)




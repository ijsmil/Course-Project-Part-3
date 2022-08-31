# Ifetayo Sands
# CIS 261
# Course Project Part 3
from datetime import datetime
def GetName():
    name = input("Enter employee name: ")
    return name
def GetDatesWorked():
    startdate = input("Enter Start Date (mm/dd/yyyy: ") 
    enddate = input("Enter End Date (mm/dd/yyyy: ")
    return startdate, enddate
def GetTotalHours():
    hours = float(input("Enter total hours: "))
    return hours
def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
def printinfo(DetailsPrinted):
    TotalEmployees = 0
    TotalHours = 0.00
    TotalGrossPay = 0.00
    TotalTax = 0.00
    TotalNetPay = 0.00
    EmpFile = open("Employees.txt", "r")
    while True:
        rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue # skip next if statement and re-start loop
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "") #remove carriage return from end of line
        EmpList = EmpDetail.split("|")
        startdate = EmpList[0]

        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(startdate, "%m/%d/%Y")
            if (checkdate < rundate):

             continue
        enddate = EmpList[1]
        name = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay, incometax, netpay, = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(startdate, enddate, name, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        TotalEmployees += 1
        TotalHours += hours
        TotalGrossPay += grosspay
        TotalTax += incometax
        TotalNetPay += netpay
        EmpTotals["TotalEmployees"] = TotalEmployees
        EmpTotals["TotalHours"] = TotalHours
        EmpTotals["TotalGrossPay"] = TotalGrossPay
        EmpTotals["TotalTax"] = TotalTax
        EmpTotals["TotalNetPay"] = TotalNetPay
        DetailsPrinted = True
    if (DetailsPrinted): # skip of no detail lines printed
        PrintTotals (EmpTotals)
    else:
        print("No detail information to print")
def PrintTotals(EmpTotals):
    print()
    print(f'Total Number of Employees: {EmpTotals["TotalEmployees"]}')
    print(f'Total Hours: {EmpTotals["TotalHours"]:,.2f}')
   
    print(f'Total Gross Pay: {EmpTotals["TotalGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotalTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotalNetPay"]:,.2f}')
if __name__ == "__main__":
    EmpFile = open("Employees.txt", "a+")
    EmpTotals = {}
    DetailsPrinted = False
    while True:
        name = GetName()
        if(name.upper() == "END"):
            break
        startdate, enddate = GetDatesWorked()
        hours = GetTotalHours()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        EmpDetail = startdate + "|" + enddate + "|" + name + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
        EmpFile.write(EmpDetail)
    # close file to save data
    EmpFile.close()
    printinfo(DetailsPrinted)
        
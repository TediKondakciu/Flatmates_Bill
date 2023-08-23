from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_flatmate1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of your flatmate? ")
days_flatmate2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

the_bill = Bill(amount=amount, period=period)
f1 = Flatmate(name=name1, days_in_house=days_flatmate1)
f2 = Flatmate(name=name2, days_in_house=days_flatmate2)

print(f"{f1.name} pays: ", f1.pays(bill=the_bill, flatmate2=f2))
print(f"{f2.name} pays: ", f2.pays(bill=the_bill, flatmate2=f1))


pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=f1, flatmate2=f2, bill=the_bill)

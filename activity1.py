def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")
tip=int(input("Enter tip amount-(percentage) "))
bill=int(input("enter bill amount "))
total_calc(bill,tip)
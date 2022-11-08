cost = 50
amount_due = cost
while(amount_due>=0):
    print(f'Amount Due: {amount_due}')
    amount = int(input('Insert coin '))
    amount_due -= amount

print(f'change owed: {abs(amount_due)}')
    

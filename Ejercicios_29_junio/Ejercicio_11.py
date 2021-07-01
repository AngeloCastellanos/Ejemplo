def invoice(amount, iva = 16):
    
    return amount + amount*iva/100

print(invoice(1000,10))
print(invoice(1000))
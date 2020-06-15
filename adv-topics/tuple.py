#!/usr/bin/env python3

months_of_the_year = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
(jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) = months_of_the_year

print(feb)


productInfo = ('Keyboard','23')
(prodName, price) = productInfo

print(prodName)























contact_info = ['555-0123', 'david@gmail.com']
(phone, email) = contact_info
print(phone)
print(email)


contacts = [('David', '555-0123'), ('Tom', '555-5678')]
for (name, phone) in contacts:
    print("{}'s phone number is {}.".format(name, phone))

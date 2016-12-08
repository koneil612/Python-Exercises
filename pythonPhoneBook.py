contacts = {
    "JOHN": {
        'first_name': 'John',
        'phone': {
            'work': '492-253-3592'
            # 'cell': '503-435-9729'
            # 'home': '552-572-4928'
        }
    },
    "SALLY": {
            'first_name': 'Sally',
            'phone': {
                'work': '539-764-8642'
                # 'cell': '452-642-7532'
                # 'home': '763-358-2362'
            }
        }
}
print type(contacts)
# print "Electronic Phone Book:"
menu = {}
menu['1']='Look up an entry'
menu['2']='Set an entry'
menu['3']='Delete an entry'
menu['4']='List all entries'
menu['5']='Quit'
while True:
    options=menu.keys()
    options.sort()
    for entry in options:
        print entry, menu[entry]

    selection=raw_input("What do you want to do? (1-5)? ")
    if selection == '1':
        grab = raw_input('Name: ')
        grab = grab.upper()
        print "Found entry for %s: %s" % (contacts[grab]['first_name'], contacts[grab]['phone']['work'])
    if grab !== contacts[i]:
            print grab + " is not in your contacts."
        # break

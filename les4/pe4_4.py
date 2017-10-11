def new_password(oldpassword, newpassword):
    oldpassword = input('Voer je oude wachtoord in')
    newpassword = input('Voer je nieuwe wachtoord in')
    if oldpassword == newpassword and newpassword > str(6):
        print('False')
    else:
        print('True')

new_password(1,1)

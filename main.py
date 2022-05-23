from advanced_tk import advanced

choice = input("Do you want the 'normal' or the 'advanced' code: ").lower()

if choice == 'normal':
    import normal
elif choice == 'advanced' or choice == 'adv':
    print("Erm.. A Tkinter window is opened.. yeah, here!")
    advanced()

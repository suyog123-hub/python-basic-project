while(True):
    password = input("Enter your password: ")
    special_characters = "@#&!_"

    has_upper = any(ch.isupper() for ch in password) 
    has_digit = any(ch.isdigit() for ch in password) 
    has_special = any(ch in special_characters for ch in password) 

    criteria_met = sum([has_upper, has_digit, has_special])

    if len(password) < 8:
        print("Very weak password — too short.")
    elif criteria_met == 3:
        print("Your password strength is HIGH — great job!")
        exit()
    elif criteria_met == 2:
        print("Your password strength is MODERATE — add more variety (uppercase, digits, or special characters).")
    else:   
        print("Weak password — missing uppercase, digits, and/or special characters.")

  # THAT IS STRING MAIN PROJECT IN THIS PROJECT WE WILL COVER ALL ABOUT STRING FUNCTION,METHODS,KEYWORDS.

  # A PROJECT IS MENU DRIVEN PROJECT IN THIS PROJECT WE WILL COVER "A USER CAN ENTER STRING ONCE,THAN CHOOSE WHAT KIND OF OPERATION TO PERFORM FROM BIG LIST STRING TOOLS.

def main():
    print("🧠 Welcome to String Utility Suite 🧠")
    user_string = input("Enter Your String :-")

    while True:
        print("\n 🔧 Select an option :")
        print("1. String Length")
        print("2. String Slicing")
        print("3. Convert to Upper , Lower , Title , Swapcase")
        print("4. Convert Substring")
        print("5. Find/ Replace Substring")
        print("6.StartWith / EndWith")
        print("7. Check isalpha / isdigit / isalnum / isspace")
        print("8. strip / Lstrip / Rstrip")
        print("9. Split / Join")
        print("10. Center / Ljust / Rjust / Zfill")
        print("11. Palindrome Checker")
        print("12. Anagram Checker")
        print("13. ASCII (ord/chr)")
        print("14. Encode / Decode")
        print("15. EXIT")

        choice = input("Enter Choice Which Task You Perform :-")                # ENTER CHOICE

        if choice == "1":
            print("Length Of String :-" , len(user_string))

        elif choice == "2":
            start = int(input("Start Index :-"))
            end = int(input("End Index :-"))
            print("Sliced :-" , user_string[start:end])

        elif choice == "3":
            print("Upper Case :-" , user_string.upper())
            print("Lower Case :-" , user_string.lower())
            print("Title Case :-" , user_string.title())
            print("Swap Case :-" , user_string.swapcase())

        elif choice == "4":
            sub = input("Enter SubString to count :-")
            print("Occurrences:-" , user_string.count(sub))

        elif choice == "5":
            sub = input("Find :")
            new = input("Replace With :-")
            print("First Found At index;-" , user_string.find(sub))
            print("Replace New String:-" , user_string.replace(sub , new))

        elif choice == "6":
            print("Start With :-" , user_string.startswith("A"))
            print("End With :-" , user_string.endswith("."))

        elif choice == "7":
            print("ISALPHA() :-" , user_string.isalpha())
            print("ISDIGIT() :-" , user_string.isdigit())
            print("ISALNUM() :-" , user_string.isalnum())
            print("ISSPACE() :-" , user_string.isspace())

        elif choice == "8":
            print("Strip() :-" , user_string.strip())
            print("Lstrip() :-" , user_string.lstrip())
            print("Rstrip() :-" , user_string.rstrip())

        elif choice == "9":
            parts = user_string.split()
            print("Split String :-" , parts)
            print("Join With '-':" , '-'.join(parts))

        elif choice == "10":
            width = int(input("Width :-"))
            print("Center() :-" , user_string.center(width , '*'))
            print("Ljust() :-" , user_string.ljust(width , '*'))
            print("Rjust() :-" , user_string.rjust(width , '*'))
            print("Zfill() :-" , user_string.zfill(width))

        elif choice == "11":
            cleaned = ''.join(c.lower() for c in user_string if c.isalnum())
            print("Palindrome?:" , cleaned == cleaned[::-1])

        elif choice == "12":
            other = input("Enter Another String :-")
            def is_anagram(s1,s2):
                return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" " , "").lower())
            print("Are Anagrams?:" , is_anagram(user_string , other))

        elif choice == "13":
            for char in user_string:
                print(f"'{char}' -> ASCII: {ord(char)}")
            code = int(input("Enter ASCII code (e.g . 65):"))
            print("Character :-",chr(code))

        elif choice == "14":
            encode = user_string.encode("utf-8")
            print("Encode:-" , encode)
            print("Decode :-" ,encode.decode("utf-8"))

        elif choice == "15":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid Choice ! Try again..")
main()

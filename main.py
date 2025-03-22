def is_Palindrome(value):
    original_value=str(value)
    reversed_value=original_value[::-1]
    return original_value==reversed_value

def main():
    print("WELCOME TO THE PALINDROME CHECKER!✋")
    palindrome_count=0

    while True:
        print("\n Menu: ")
        print("1. Check if a number is a palindrome")
        print("2. Exit")
        choice=input("choose an option: ")

        if choice=="1":
            value=input("Enter a number or a word: ").strip()

            if is_Palindrome(value):
                print(f"😄{value} is a palindrome😁")
                palindrome_count+=1

                if value.lower()=="racecar":
                    print("🏎️ 🏎️ 🏎️ you won a free racecar ⁉")
            else:
                print(f"too sad 😔{value} is not a palindrome 😭")
        elif choice=="2":
             print(f"Thanks for playing! you checked {palindrome_count} palindromes!")
             break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__=="__main__":
     main()
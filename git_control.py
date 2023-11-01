#Benjamin Stickle
#Version control testing

def menuDisplay():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(passcode):
    encoded_passcode = ""

    for n in passcode:
        n = int(n)
        if n < 7:
            n += 3
            encoded_passcode += str(n)
        else:
            n = (n+3) % 10 
            encoded_passcode += str(n) 

    return encoded_passcode 


def main():
    while True:
        menuDisplay()
        userInput = input("Please enter an option:")
        if userInput == "1":
            password = input("Please enter your password to encode:")
            encodedPassword = encode(password)
            print("Your password has been encoded and stored!")
        if userInput == "2":
            pass
        if userInput == "3":
            exit()
    

if __name__ == "__main__":
    main()


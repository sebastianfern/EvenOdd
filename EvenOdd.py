class EvenOdd:
    
    def main():

        print("This program determines if a number is even or odd.")

        UserEnteredNum = input("What number would you like to try?")

        UserEnteredNum.strip
        try: 
            enteredNum = int(UserEnteredNum) 
            if enteredNum % 2 == 0:
                EvenOdd.is_even()
            else:
                EvenOdd.is_odd()
        except ValueError as e:
            print("Number not entered, Invalid input")

    def is_even():
        print("Even")

    def is_odd():
        print("Odd")


if __name__ == '__main__':
    EvenOdd.main()
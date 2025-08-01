#A program that check for "hello" in a greeting or at least an "h"
def main():
    greeting = input("Greeting: ")
    return greetings(greeting)

# A function that takes in a greeting and tharoughly check for "hello" or an "h" and print out the corresponding outcome amount.
def greetings(greeting):
    greeting = greeting.strip(" ").lower()

    if "hello" in greeting[:6]:
        print("$0")
    elif "h" in greeting[:1]:
        print("$20")
    else:
        print("$100")

main()

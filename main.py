from functions import encode_message, decode_message
from art import logo4

do_some_morse_code = True
while do_some_morse_code:
    print(logo4)
    # print("Mores Code encoder and decoder")
    user_input = input("What would you like to do to a message? Type encode or decode: ").lower()
    if user_input == "encode":
        encode_message(input("Type your message: ").upper())
    elif user_input == "decode":
        decode_message(input("Message to decode: "))
    elif user_input == "end" or user_input == "bye" or user_input == "quit":
        do_some_morse_code = False
    else:
        print("invalid input try again")

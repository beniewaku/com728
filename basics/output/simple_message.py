# Display message to the standard output
from basics.input import user_input, string_operators, review, data_types, ascii_robot
from basics.output import escape_characters


import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message

def run_block_a(ascii_art=None):
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "escape_characters":
        escape_characters.run()
    elif response =="ascii_art":
        ascii_art.run()
    elif response == "user_input":
        user_input.run()
    elif response == "string_operators":
        string_operators.run()
    elif response == "review":
         review.run()
    elif response =="data_types":
         data_types.run()
    elif response == "ascii_robot":
         ascii_robot.run()

def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()
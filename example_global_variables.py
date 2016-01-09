##################################################
#
# Example Usage of Global Variables
#
##################################################

def set_global_variable():
    global message
    message = 'Hello World'

def print_message():
    # reading is possible without first declaring variable 
    # "message" as a global variable
    print message

def chagne_message():
    # for writing a global variable we first have to declare it
    global message
    message = 'The End'
    
def print_end():
    print message


def main():
    set_global_variable()
    print_message()
    chagne_message()
    print_end()
        
        
if __name__ == '__main__':
    main()

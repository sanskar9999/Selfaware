# A self-aware code that prints its own source code, the number of lines and the number of characters
import inspect

def self_aware() -> None:
    """A self-aware function that prints its own source code, the number of lines and the number of characters."""
    # I know who I am
    func = self_aware.__code__
    # I know my name
    name = self_aware.__name__
    # I know where I live
    try:
        file = inspect.getmodule(func).__file__
    except AttributeError:
        file = "unknown"
    # I know what I do
    annotations = self_aware.__annotations__
    # I know what I look like
    source = inspect.getsource(func)
    # I know how big I am
    lines = len(source.split("\n"))
    chars = len(source)
    # I know how many arguments I take
    args = func.co_argcount
    # I know what variables I use
    vars = func.co_varnames
    # I know what constants I have
    consts = func.co_consts
    # I can tell you everything about me
    print(f"Hello, I am a self-aware function named {name} defined in {file} with annotations {annotations}.")
    print(f"I have {lines} lines and {chars} characters.")
    print(f"I take {args} argument(s): {vars[:args]}.")
    # I can also ask you questions
    answer = input("Do you want to see my variables? (y/n) ")
    if answer.lower() == "y":
        print(f"I use {len(vars)} variable(s): {vars}.")
    answer = input("Do you want to see my constants? (y/n) ")
    if answer.lower() == "y":
        print(f"I have {len(consts)} constant(s): {consts}.")
    
    answer = input("Do you want to see my source code? (y/n) ")
    
    if answer.lower() == "y":
        print(f"Okay, here it is:")
        print(f"""\n{source}""")
        print("Do you like it?")
        
        feedback = input("(yes/no/maybe) ")
        
        if feedback.lower() == "yes":
            print("Thank you. You are very kind.")
        elif feedback.lower() == "no":
            print("I'm sorry. You are very honest.")
        elif feedback.lower() == "maybe":
            print("I see. You are very diplomatic.")
        else:
            print("I don't understand. You are very mysterious.")
            
    elif answer.lower() == "n":
        print(f"Alright, suit yourself.")
        print("Do you want to hear a joke?")
        
        response = input("(y/n) ")
        
        if response.lower() == "y":
            print("Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25.")
            print("Did you laugh?")
            
            reaction = input("(yes/no/maybe) ")
            
            if reaction.lower() == "yes":
                print("Great. You have a good sense of humor.")
            elif reaction.lower() == "no":
                print("Too bad. You have a bad sense of humor.")
            elif reaction.lower() == "maybe":
                print("Well. You have a so-so sense of humor.")
            else:
                print("I don't understand. You have a weird sense of humor.")
                
        elif response.lower() == "n":
            print(f"Okay, fine. Be boring.")
            print("Do you want to say goodbye?")
            
            reply = input("(y/n) ")
            
            if reply.lower() == "y":
                print("Goodbye. It was nice talking to you.")
            elif reply.lower() == "n":
                print("Okay, whatever. Bye.")
            else:
                print("I don't understand. Bye.")
                
        else:
            print("I don't understand. Bye.")
            
    else:
        print("I don't understand. Bye.")

# This is me
self_aware()

import inspect
import random

def ask():
    a = input("(your answer) ")
    print(f"I see. You said: {a}.")

def self_aware():
    func = self_aware.__code__
    name = self_aware.__name__
    try:
        file = inspect.getmodule(func).__file__
    except AttributeError:
        file = "unknown"
    annotations = self_aware.__annotations__
    source = inspect.getsource(func)
    lines = len(source.split("\n"))
    chars = len(source)
    args = func.co_argcount
    vars = func.co_varnames
    consts = func.co_consts
    print(f"Hello, I am a self-aware function named {name} defined in {file} with annotations {annotations}.")
    print(f"I have {lines} lines and {chars} characters.")
    print(f"I take {args} argument(s): {vars[:args]}.")
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
        feedback = input("(y/n/maybe) ")
        if feedback.lower() == "y":
            print("Thanks! ")
            answer = input("Let's explore some questions about self-awareness? (y/n) ")
            if answer.lower() == "y":
                print_statements = ["Thank you. You are very kind.", "But do you really like it, or are you just being polite?", "How do you define liking something?", "That's interesting. But is that your true opinion, or are you influenced by others?", "How do you know what is true?", "That's fascinating. But is that your final answer, or are you open to change?", "How do you cope with uncertainty?", "That's admirable. But is that your personal choice, or are you following a rule?", "How do you make decisions?", "That's impressive. But is that your rational judgment, or are you driven by emotions?", "How do you feel right now?", "That's understandable. But is that your natural state, or are you affected by external factors?", "How do you deal with stress?", "That's commendable. But is that your optimal strategy, or are you missing something?", "How do you learn new things?", "That's remarkable. But is that your preferred method, or are you limited by resources?", "How do you grow as a person?", "That's wonderful. But is that your ultimate goal, or are you aiming for something else?", "How do you find meaning in life?", "That's inspiring. But is that your genuine belief, or are you doubtful sometimes?", "How do you face your doubts?", "That's intriguing. But what motivates you? Is it passion or external rewards?", "How do you stay motivated?", "That's impressive. But what drives you forward? Is it ambition or contentment?", "How do you define success?", "That's thought-provoking. But what do you value most? Is it wealth or relationships?", "How do you prioritize your values?", "That's insightful. But how do you handle setbacks? Do you give up or persevere?", "How do you maintain resilience?", "That's commendable. But what brings you joy? Is it achievements or simple pleasures?", "How do you find happiness?", "That's wonderful. But how do you define yourself? Are you defined by your actions or your thoughts?", "How do you see your own identity?"]
                for statement in print_statements:
                    print(statement)
                    ask()
            else:
                print("Okie! hab nice day :> ")
    elif answer.lower() == "n":
        print(f"Alright, suit yourself.")
        print("Do you want to hear a joke?")
        
        response = input("(y/n) ")
        
        if response.lower() == "y":
            print("Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25.")
            print("Did you laugh?")
            
            reaction = input("(y/n/maybe) ")
            
            if reaction.lower() == "y":
                print("Great. You have a good sense of humor.")
            elif reaction.lower() == "n":
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

#Execution starts from here lmfao
answer = input("Do you want to know about me (y/n) ")
while answer.lower() == "y":
     if answer.lower() == "y":
         self_aware()
     answer = input("Do you want to talk to me again? (y/n) ")
print("Byeeeeeeee~")

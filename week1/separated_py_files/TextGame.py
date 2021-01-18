def play_game():
    """
    my small stupid text game :D
    """

    def unimmaginable(user_answer):
        print('You feel tired. Straining yourself again trying to choose somthing that is, right now, unimaginable.')
        print("Who knew the number", user_answer, "would be your down fall?")
        print("You died of exhaustion.")
        print("BAD END ∎" )
        exit()

    def bad_player(tried_text=None):
        print('You lay in confusion trying to decide what to do. "Am I going mad?" you think. "I\'m unable to tell the differences between numbers and letters anymore."' )
        if tried_text is not None:
            print("You try your best to recall the symbol '1', but all you can think of are the weirdly shaped figures '", tried_text, "'")
        print("")
        print("You died")
        print("BAD END ∎" )
    
    def food():
        print("What else is there to do during isolation? You eat your mother's cooking that she made for the whole family the day before. It warms you up.")
        print("Looking in as the narrator, I could only specuate that you are feeling content despite the ongoing chaos in the world. Got a place to stay and access to food. To another day player!")
        print("GOOD END ∎" )

    def sleep():
        print("What else is there to do during isolation? You crawl back into bed and stare up at the ceiling.")
        print("To another day player!")
        print("GOOD END ∎" )
    user_answer = -1

    print("Today marks a whole year you have been in quarantine")
    print("What is the first thing you will do today?")
    
    try:
        user_answer = input("""
I am going...
    1. to the fridge
    2. back to sleep
    3. PARTY and try to over throw the government.
        """)
        user_answer = int(user_answer)
    except:
        bad_player(user_answer)
        
    if user_answer == 1:
        food()
    elif user_answer == 2:
        sleep()
    elif user_answer == 3:
        print("...")
        print("You're in jail now with Covid")
        print("BAD END ∎" )
    else:
        unimmaginable(user_answer)

play_game()
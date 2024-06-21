print("Are you in a hurry?")
answer = input()

if answer.lower() == 'yes':
    print("Keep walking.")
else:
    print("Do you remember their name?")
    answer = input()

    if answer.lower() == 'no':
        print("Don't say hi.")
    else:
        print("Is the person an ex?")
        answer = input()

        if answer.lower() == 'yes':
            print("Keep walking.")
        else:
            print("Are you in an unusual situation?")
            answer = input()

            if answer.lower() == 'yes':
                print("Don't say hi.")
            else:
                print("Say hi.")
By following the series of questions and providing Yes o

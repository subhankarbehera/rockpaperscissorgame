while (true):
    one_user=input("sherlock\t:").casefold()
    two_user=input("mycroft\t:").casefold()
    if(one_user == 'r') and (two_user == 'r'):
        print("match draw")
        
    elif(one_user == 'r') and (two_user == 'p'):
        print("mycroft won")
    elif(one_user == 'r') and (two_user == 's'):
        print("sherlock won")
    elif(one_user == 'p') and (two_user == 'r'):
        print("sherlock won")
    elif(one_user == 'p') and (two_user == 'p'):
        print("match draw")
    elif(one_user == 'p') and (two_user == 's'):
        print("mycroft won")
    elif(one_user == 's') and (two_user == 'r'):
        print("mycroft won")
    elif(one_user == 's') and (two_user == 'p'):
        print("sherlock won")
    elif(one_user == 's') and (two_user == 's'):
        print("match draw")
    
    else:
        print("inputs do not match")
    print("\n")
    continue_input = input("want to play again? (y/n):").casefold()
    print("\n")
    if(continue_input == 'y') or (continue_input == 'yes'):
        continue
    else:
         print("see you again.bye")
         break

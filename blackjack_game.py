# import functions to handle the cards the user calculate score and compare scores
from blackjack import play_game
restart = True
while restart:         
    restart = input("\nDo you want to play the black jack game. Yes/No: ").lower()
    if restart == "yes":
        print("\n" * 50)
        play_game()
        restart = True
    else:
         restart = False
                    
                    
            
        
        
        
    

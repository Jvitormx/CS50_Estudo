import random
import sys

while True:

    n=input("Level: ")
    verify=n.isnumeric()
    if verify==True:
        n_int=int(n)
        if n_int>0:
            n_int=random.randint(1,n_int)

            while True:

                guess=input("Guess: ")
                verify_guess=guess.isnumeric()
                if verify_guess==True:
                    guess_int=int(guess)
                    if guess_int>0:
                        if guess_int<n_int:
                            print("Too small!")
                            continue
                        elif guess_int>n_int:
                            print("Too large!")
                            continue
                        else:
                            print("Just right!")
                            sys.exit()
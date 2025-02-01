# 1. Name:
#      Margaret Binns

# 2. Assignment Name:
#      Lab 04: Monopoly

# 3. Assignment Description:
#      This program purpose is to decide whether or not a user is able to purchase and place a hotel on their property in the game monopoly. It goes over various variables such as available funds, current houses, and overall ownership of properties to figure out the answer.

# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out how to know whether the user has enough money or not becuase I'm not familiar with monopoly rules.

# 5. How long did it take for you to complete the assignment?
#      3 hours

prompt_color_group = input ('Do you own all the green properties? (y/n)')

if prompt_color_group == 'y':

    prompt_PA = int(input ('What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel)'))

    if prompt_PA == range(3):

        prompt_NC = int(input('What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel)'))

        if prompt_NC == range(3):

            prompt_PC = int(input('What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel)'))

            if prompt_PC == range(3):

                prompt_hotels = int(input('How many hotels are there to purchase?'))

                if prompt_hotels > 0:

                    total_money_needed = 0
                    #figure out this part of the flow chart in chart 2

                    prompt_cash = int(input('How much cash do you have to spend?'))

                    if prompt_cash >= total_money_needed:
                       
                        prompt_houses = int(input('How many houses are there to purchase? '))

                        if prompt_houses == 4:

                            pass
                            #pick up at point b

                        else:

                            #out: no houses
                            print ('There are not enough houses available for purchase at this time.')





                    else:
                       
                       #out: cash
                       print ('You do not have sufficient funds to purchase a hotel at this time.')

                else:

                    #out: no hotels
                    print ('There are not enough hotels available for purchase at this time.') 

            elif prompt_PC == 5:

                #out:swap pc
                print ('Swap Pacific\'s hotel with Pennsylvania\'s 4 houses.')

            else:
                pass

        elif prompt_NC == 5:

            #out:swap nc
            print ('Swap North Carolina\'s hotel with Pennsylvania\'s 4 houses.')

        else:
            pass

    elif prompt_PA == 5:

        #out:one hotel
        print ('You cannot purchase a hotel if the property already has one.')

    else:
        pass
        

else:
    #out:no properties
    print ('You cannot purchase a hotel until you own all the properties of a given color group.')
     
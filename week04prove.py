# 1. Name:
#      Margaret Binns test
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python?
#      Was it an aspect of the problem you are to solve?
#      Was it the instructions or any part of the problem definition?
#      Was it the submission process?
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

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

                   pass

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
     
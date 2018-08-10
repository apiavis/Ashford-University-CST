colors = ['red', 'blue', 'yellow']
color_1 = (input('Enter one color that you would like to mix (all lowercase): '))
if color_1 in colors:
    color_2 = (input('Enter the second color that you would like to mix (all lowercase): '))
    if color_2 in colors:
        if ((color_1 == 'red') and (color_2 == 'blue')) or ((color_1 == 'blue') and (color_2 == 'red')):
            print(color_1, 'and', color_2, 'will make purple')
        elif ((color_1 == 'red') and (color_2 == 'yellow')) or ((color_1 == 'yellow') and (color_2 == 'red')):
            print(color_1, 'and', color_2, 'will make orange')
        elif ((color_1 == 'blue') and (color_2 == 'yellow')) or ((color_1 == 'yellow') and (color_2 == 'blue')):
            print(color_1, 'and', color_2, 'will make green')
    else:
        print('The color you have entered is not a primary color.  Please start over.')
else:
    print('The color you have entered is not a primary color.  Please start over.')

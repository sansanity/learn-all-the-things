# from sense_hat import SenseHat
# sense=SenseHat()


inp = input("What text do you want?")
# text_colour = input("Please enter your preferred R G B colour scheme for your text, separated by commas: ")
# bg_colour = input("Please enter your preferred R G B colour scheme for your background, separated by commas: ")
# speed = float(input("Please enter a scroll speed: "))

sentinel = False

while not sentinel:
    text_colour = input("Please enter your preferred R G B colour scheme for your text, separated by commas: ")
    bg_colour = input("Please enter your preferred R G B colour scheme for your background, separated by commas: ")
    speed = input("Please enter a scroll speed: ")

    try:
        text_list = text_colour.split(",")
    except:
        print("You have not separated your values by commas")
        continue
    
    try:
        text_list = [int(x) for x in text_list]
    except:
        print("You have not entered an integer value!")
        continue

    try:
        bg_colour_list = bg_colour.split(",")
    except:
        print("You have not separated your values by commas")
    
    try:
        bg_colour_list = [int(x) for x in bg_colour_list]
    except:
        print("You have not entered an integer value!")

    for x in text_colour:
        if type(x) != int:
            break
        elif x >= 355:
            break
        else:
            continue

    for x in bg_colour:
        if type(x) != int:
            break
        elif x >= 355:
            break
        else:
            continue
    
    if type(speed) != int or type(speed) != float:
        continue

    sentinel = True
    







                      

# while True: 
#     sense.show_message(inp,text_colour= text_list, back_colour= bg_colour_list, scroll_speed = speed)
#     sense.clear()

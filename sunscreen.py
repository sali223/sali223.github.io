weather = "sunny"
temperature = 75  #temp 
time_of_day = "afternoon"   or "evening"
has_sunscreen = True

def recommend_sunscreen(weather, temperature, time_of_day, has_sunscreen):
    if weather == "sunny" and temperature > 70:
        if time_of_day == "afternoon":
            if has_sunscreen:
                print("Great! You already have sunscreen. Don't forget to reapply every 2 hours.")
            else:
                print("It's sunny and warm! Don't forget to wear sunscreen, especially in the afternoon.")
        elif time_of_day == "morning":
            print("It's sunny in the morning, but the sun isn't as intense yet. Still, sunscreen is a good idea.")
        else:
            print("It's sunny, but it's evening. Sunscreen might not be necessary unless you're outside for a while.")
    else:
        print("The weather isn't ideal for sunscreen right now.")

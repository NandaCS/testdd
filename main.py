story = """
Okay, we understand you... You are not alone! If you are feeling %s REMEMBER that you can count with %s in sad and happy moments. When your stress level is %s, REMEMBER that there are some things that you can do to feel better, such as meditate, listen to music, make art, or hangout with a friend.
The school environment can be hard and affect our lives drastically. If you are having difficult %s, don't hesitate to ask for help! REMEMBER that you are not alone and everyone goes through hardships. Besides that, if you feel %s in some circunstances, REMEMBER that you can %s.
We understand that sometimes students have too much pressure and need to deal with personal and academic life simultaneously. If you feel tired %s REMEMBER to review your schedule and organize it in a way that you can sleep at least 8 hours to preserve your physical and mental health.
Sometimes people don't ask for help because they feel %s. REMEMBER that many people around you also need help and you can be the one to bring happiness to them. %s would be excellent ways to put it in practice.
REMEMBER: you should not be ashamed to ask for help!"""

print ("REMEMO")
print ("Hey! How are you? Is everything going well? I know school can be overwhelming sometimes and that's why I am here to talk with you. By the way, at the end of our talk I will give you a gift! our secret.")
a = input("Based on this spacetime dimension you inhabit right now, define your feelings in one word. I know it's hard: ")
b = input("If you need to tell a secret to a human. Who would you look for? (Type their name): ")
c = input("How do you define your level of stress? (1-10)- 10 being the most stressful: ")
d = input("This one gets tricky. Ready? Tell me the two hardest things you experienced in college so far (eg.: to make friends or to deal with midterms): ")
e = input("That's tough... But now I will have to be a little bit invasive, I guess you don't mind because we're intimate friends already! Think about your most recent personal struggle. Which one of these four words would better define your feelings in that moment? (anxious, discouraged, fearful, or stressed) Type one or more: ")
f = input("Thanks for trusting me. Now, tell me two things that you really enjoy doing in your free time (I like to talk to humans!): ")
g = input("Let's be honest. How often do you feel tired? (always, often, sometimes): ")
h = input("Why do you think some people don't like to ask for help? (eg.: ashamed, uncomfortable) Maybe the feel... ")
i = input("Before you go, tell me two ways we can help other people around us (eg.: volunteering and donating): ")

print (story % (a, b, c, d, e, f, g, h, i))

bye = input("Thank you for chatting with me! I hope it was helpful and you understood what you can do to take care of your mental heath! Feel free to visit me more often or look for professional assistance. Love u! <3") 

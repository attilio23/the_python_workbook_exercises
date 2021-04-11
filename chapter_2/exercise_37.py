##
#Determine whether the entered letter is a vowel or a resonant
#Read the letter from the user
letter=str(input("Enter the letter:\n"))
if letter=='a'or letter=='e' or letter=='i' or letter=='o' or letter=='u' or letter=='A'or letter=='E' or letter=='I' or letter=='O' or letter=='U':
    print("You entered a vowel")
elif letter=='y' or letter=='Y':
    print("Sometimes it's a vowel, sometimes it's a consonant")
else:
     print("You entered a consonant")

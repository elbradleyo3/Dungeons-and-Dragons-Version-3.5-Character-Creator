# import the random module so the program can simulate dice rolling
import random

#The Basic Information for your character

print()

name = input("what is your name?")
race = input("what is your race?")
size = input("what size is your character?")
Class = input("what class is your character?")
age = input("how old is your character?")
gender = input("what gender is your character?")
height = int(input("how tall is your character (in inches)?"))
weight  = input("how much does your character weigh (in pounds)?")
alignment = input("what is your character's alignment?")


#All of your character's ability 

print()
strength_score = int(input("what is your strength score?"))
constitution_score = int(input("what is your constitution score?"))
dexterity_score = int(input("what is your dexterity score?"))
intelligence_score = int(input("what is your intelligence score?"))
wisdom_score = int(input("what is your wisdom score?"))
charisma_score = int(input("what is your charisma score?"))

strength_modifier = (strength_score-10)/2 
constitution_modifier = (constitution_score-10)/2 
dexterity_modifier = (dexterity_score-10)/2 
intelligence_modifier = (intelligence_score-10)/2 
wisdom_modifier = (wisdom_score-10)/2 
charisma_modifier = (charisma_score-10)/2 



# Armor Calculation
armor_bonus = 0
max_dex = 0

wearing_armor = input("are you wearing armor? (type yes or no)")

if wearing_armor == "yes" or "Yes":

    armor = input("what armor are you wearing (choose from the following) \n" \
                  "Light Armor: Padded, Leather, Studded Leather, Chain Shirt \n" \
                  "Medium Armor: Hide, Scale Mail, Chainmail, Breastplate \n" \
                  "Heavy Armor: Splint_Mail, Banded Mail, Half-Plate, Full-Plate \n" \
                  "(if your armor is not listed type \"other\" ")

    if armor == "Padded" or "padded":
        armor_bonus = 1
        max_dex = 8

    elif armor == "Leather" or "leather":
        armor_bonus = 2
        max_dex = 6

    elif armor == "Studded Leather" or "Studded leather" or "studded leather" or "studded Leather":
        armor_bonus = 3
        max_dex = 5

    elif armor == "Chain Shirt" or "Chain shirt" or "chain shirt" or "chain Shirt":
        armor_bonus = 4
        max_dex = 4

    elif armor == "Hide" or "hide":
        armor_bonus = 3
        max_dex = 4

    elif armor == "Scale Mail" or "Scale mail" or "scale mail" or "scale Mail":
        armor_bonus = 4
        max_dex = 3
    
    elif armor == "Chainmail" or "ChainMail" or "chainmail":
        armor_bonus = 5
        max_dex = 2

    elif armor == "Breastplate" or "BreastPlate" or "breastplate":
        armor_bonus = 5
        max_dex = 3

    elif armor == "Splint Mail" or "Splint Mail" or "splint mail" or "splint Mail" :
        armor_bonus = 6
        max_dex = 0

    elif armor == "Banded Mail" or "Banded mail" or "banded mail" or "banded Mail":
        armor_bonus = 6
        max_dex = 1

    elif armor == "Half-Plate" or "Half-plate" or "half-plate":
        armor_bonus = 7
        max_dex = 0

    elif armor == "Full-Plate" or "Full-plate" or "full-plate":
        armor_bonus = 8
        max_dex = 1

    elif armor == "Other" or "other":
        armor_bonus = int(input("what is the armor bonus: "))
        max_dex = int(input("what is the maximum dexterity bonus"))

else: wearing_armor == "no"
armor_bouns = 0
max_dex = 99


using_shield = input("are you using a shield? (type yes or no)")

shield_bonus = 0

if using_shield == "yes" or "Yes":

    shield = input ("what shield are you using? (choose from the following) \n" \
                    "Buckler, Light Wood, Light Steel, Heavy Wood, Heavy Steel, Tower")

    if shield == "Buckler" or "buckler":
        shield_bonus = 1

    elif shield == "Light Wood" or "Light wood" or "light wood" or " light Wood":
        shield_bonus = 1

    elif shield == "Light Steel" or "Light steel" or "light steel" or "light Steel":
        shield_bonus = 1

    elif shield == "Heavy Wood" or "Heavy wood" or "heavy wood" or "heavy Wood":
        shield_bonus = 2

    elif shield == "Heavy Steel" or "Heavy steel" or "heavy steel" or "heavy Steel":
        shield_bonus = 2

    elif shield == "Tower" or "tower":
        shield_bonus = 4
        
    
    
    
    

                   
                      
    
print("Name: ", name)    
print("Race: ", race)
print("Size: ", size)
print("Class: ", Class)
print("Age: ", age)
print("Gender: ", gender)
print("Height: ", height)
print("Weight: ", weight)
print("Alignment: ", alignment)
    
print()
print("Armor Class Breakdown:")
print()
print("Armor Bonus: ", armor_bonus)
print("Shield Bonus: ", shield_bonus )
print("Dexterity Bonus: ", )
print("Total: ", armor_bonus + shield_bonus + dexterity_modifier)


print()

print("Ability Scores:")
print("strength score: ", strength_score, "\t", "strength modifier: ", strength_modifier)
print("constitution score: ", constitution_score, "\t", "constitution modifier: ", constitution_modifier)
print("dexterity score: ", dexterity_score, "\t", "dexterity modifier: ", dexterity_modifier)
print("intelligence score: ", intelligence_score, "\t", "intelligence modifier: ", intelligence_modifier)
print("wisdom score: ", wisdom_score, "\t", "wisdom modifier: ", wisdom_modifier)
print("charisma score: ", charisma_score, "\t", "charisma modifier: ", charisma_modifier)

# have in program dice roller
# have the option to save character sheet to a document

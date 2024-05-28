from random import choice


Action = [
        "Attack on Titan",
        "One Punch Man",
        "My Hero Academia",
        "Naruto: Shippuden",
        "Demon Slayer: Kimetsu no Yaiba",
        "Tokyo Ghoul",
        "Fate/Stay Night: Unlimited Blade Works",
        "Hunter x Hunter (2011)",
        "Fullmetal Alchemist: Brotherhood",
        "Dragon Ball Z",
    ]

Comedy = [
        "Gintama",
        "One Punch Man",
        "Konosuba: God's Blessing on This Wonderful World!",
        "The Disastrous Life of Saiki K.",
        "Nichijou (My Ordinary Life)",
        "Daily Lives of High School Boys",
        "Haven't You Heard? I'm Sakamoto",
        "Grand Blue Dreaming",
        "Mob Psycho 100",
        "Great Teacher Onizuka",
]

Adventure = [
        "One Piece",
        "Hunter x Hunter (2011)",
        "Made in Abyss",
        "Fullmetal Alchemist: Brotherhood",
        "Attack on Titan",
        "Magi: The Labyrinth of Magic",
        "Naruto: Shippuden",
        "Sword Art Online",
        "Vinland Saga",
        "The Rising of the Shield Hero",
]



class Anime_list:
        while True:
                User_Question = input("Pick a anime genre:\nAction\nComedy\nAdventure\nAnswer:")
                if User_Question.lower() == "action":
                        print(choice(Action))
                        break
                if User_Question.lower() == "comedy":
                        print(choice(Comedy))
                        break
                if User_Question.lower() == "avdenture":
                        print(choice(Adventure))
                        break
                else:
                        print("not a genre, try again")


Anime_list()
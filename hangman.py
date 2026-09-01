import random

list_of_words = [
    "adventure", "backpack", "boundary", "capital", "compass", "continent", "country", 
    "desert", "distance", "equator", "glacier", "horizon", "island", "latitude", 
    "longitude", "mountain", "ocean", "peninsula", "plateau", "railroad", "safari", 
    "scenery", "topography", "tourism", "valley", "volcano", "waterfall", "wilderness",
    "atmosphere", "biodiversity", "cell", "chemical", "climate", "comet", "eclipse", 
    "ecology", "element", "evolution", "experiment", "galaxy", "gravity", "hurricane", 
    "laboratory", "mammal", "molecule", "organism", "oxygen", "photosynthesis", 
    "planet", "radiation", "satellite", "skeleton", "telescope", "temperature", 
    "universe", "vaccine", "velocity", "weather",
    "algorithm", "application", "artificial", "backup", "bandwidth", "binary", 
    "browser", "compiler", "computer", "database", "developer", "encryption", 
    "firewall", "hardware", "interface", "internet", "keyboard", "monitor", 
    "network", "password", "processor", "program", "protocol", "security", 
    "software", "terminal", "variable", "website",
    "appetizer", "barbecue", "beverage", "breakfast", "chocolate", "cinnamon", 
    "delicious", "dessert", "dinner", "flavor", "hungry", "ingredient", "kitchen", 
    "luncheon", "mushroom", "nutrition", "pineapple", "pancake", "restaurant", 
    "sandwich", "seafood", "spaghetti", "strawberry", "tasty", "vegetable", 
    "vinegar", "waffle", "yoghurt",
    "architecture", "broadcast", "camera", "canvas", "celebrity", "cinema", 
    "concert", "costume", "creative", "exhibition", "festival", "gallery", 
    "illustration", "instrument", "journalism", "literature", "magazine", 
    "melody", "museum", "musician", "orchestra", "painting", "photography", 
    "sculpture", "symphony", "theater", "tragedy", "vintage",
    "abruptly", "absurd", "abyss", "askew", "avenue", "awkward", "axiom", "azure", 
    "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "blitz", "blizzard", 
    "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", 
    "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", 
    "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", 
    "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", 
    "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", 
    "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "futurism", 
    "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", 
    "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", 
    "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", 
    "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", 
    "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", 
    "junkie", "juxtaposition", "kaleidoscope", "kamikaze", "kayak", "kazoo", 
    "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", 
    "larynx", "luxury", "marquis", "matrix", "megahertz", "microwave", "mnemonic", 
    "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", 
    "ovary", "oxidize", "oxygen", "pajamas", "peekaboo", "phlegm", "pixel", "pizazz", 
    "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", 
    "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", 
    "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", 
    "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", 
    "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", 
    "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", 
    "unknown", "unworthy", "unzip", "updraft", "upstream", "urban", "exodus", 
    "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", 
    "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", 
    "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", 
    "xylophone", "yacht", "yearbook", "yippee", "yoked", "youthful", "yummy", 
    "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"
]

y = True

while y == True:
    print("\n........................WELCOME TO THE HANGMAN GAME........................")
    print("Guess the word......")
    guess_word = random.choice(list_of_words)
    print(f"Word length is: {len(guess_word)}")
    print(f"You get {len(guess_word)-2} tries.")
    print("START.......... \n")
    out_of_guesses = False
    st = ['_'] * len(guess_word)
    print(" ".join(st),"\n")
    win = False
    
    for i in range(len(guess_word)-2):
        guessed = input(f"Guess {i+1}: ").strip().lower()
        st = ['_'] * len(guess_word)
        if len(guessed) != len(guess_word):
            if (len(guess_word)-2)-(i+1) == 0:
                out_of_guesses = True
                print(f"You have {(len(guess_word)-2)-(i+1)} guesses remaining\n")
            else:
                print(f"Please enter a {len(guess_word)}-letter word\n")
        elif guessed == guess_word:
            print("You guessed it correctly....\n")
            win = True
            break
        else:
            for j in range(len(guess_word)):
                if guessed[j] == guess_word[j]:
                    st[j] = guessed[j]
            print("Guessed: \n", " ".join(st))
            st = []
            print("Incorrect Guess. Try Again.")
            print(f"You have {(len(guess_word)-2)-(i+1)} guesses remaining\n")
            
        if ((len(guess_word)-2)-(i+1) == 0) or (out_of_guesses == True):
            print("\nGAME OVER!!!")
            print(f"The correct word was \"{guess_word}\".\n")

    while True:
        y_n = input("Do you want to continue with a new game? (y/n): ")
        if y_n.strip().lower() == 'y':
            y = True
            break
        elif y_n.strip().lower() == 'n':
            print("Thank You for playing the game!!!\n")
            y = False
            break
        else:
            print("Please enter a valid command.")

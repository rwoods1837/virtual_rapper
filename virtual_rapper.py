class Rapper:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.health = 5

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Dis boi ded.")

    def sleep(self):
        if self.is_alive:
            print(self.name + " goes 'zzzzzzzzzzzzzz...'")
        else:
            print("You kind of already killed dis dude")

    def play(self):
        if self.is_alive:
            print(self.name + " goes 'AYE!'")
        else:
            print("Its wrong to play with a dead person")

    def rap(self):
        if self.name == "Logic":
            print("sayin that you can't solidifys you never will")
        elif self.name == "J. Cole":
            print("ok the neighbors think I'm selling dope")
        elif self.name == "Kendrick Lamar":
            print("We gon be alright")
        elif self.name == "Drake":
            print("she say do you love me, I tell her only partly, I only love my bed and my mama I'm sorry.")
        elif self.name == "Kanye West":
            print("Now, I ain't sayin she a gold digga")
        elif self.name == "Eminem":
            print("Will the real slim shady please stand up")
        elif self.name == "Machine Gun Kelly":
            print("")
        elif self.name == "Tech N9ne":
            print("")

    def kill(self, other):
        print(self.name + " kills " + other.name + "!")
        other.is_alive = False

    def pay_respects(self, other):
        if other.is_alive:
            print("He's still alive bro")
        else:
            print(self.name + " pays respect to " + other.name)

    def rap_battle(self, other):
        print(self.name + " out-raps " + other.name + "!")

    def hug(self, other):
        print(self.name + " hugs " + other.name +"!")
        other.health += 1

        if other.health < 10:
            print(other.name + " says, 'I'm like " + str(other.health) + " healthy now.")
        else:
            print(other.name + " says, 'Um, this is awkward.'")

    def attack(self, other):
        print(self.name + " attacks " + other.name + "!")
        other.health -=1
        print(other.name + " says Ow!!" + "Hey! Now my health is only " + str(other.health))
  
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
logic = Rapper("Logic")
j_cole = Rapper("J. Cole")
kendrick_lamar = Rapper("Kendrick Lamar")
drake = Rapper("Drake")
kanye_west = Rapper("Kanye West")
eminem = Rapper("Eminem")
mgk = Rapper("Machine Gun Kelly")
tech_n9ne = Rapper("Tech N9ne")

#see video for explanation of code: https://www.youtube.com/watch?v=POQIIKb1BZA&ab_channel=thenewboston
class Enemy:
    #class variable
    life = 3

    def attack(self):
        print("ouch!")
        self.life -=1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()
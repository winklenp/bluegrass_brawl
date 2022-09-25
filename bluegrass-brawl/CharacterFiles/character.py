import pygame
import fighter
import attack
import vector
import projectile
class MetalMan(fighter.Fighter):
    def __init__(self, screen, x, y):
        self.imageRect=pygame.rect.Rect(0,0,160,124)
        fighter.Fighter.__init__(self, screen, x, y, 1200, "CharacterFiles/CharacterModels/MetalMan/")
        self.WALKSPEED = 1.5
        self.GRAVITYSTRENGTH = 1.3
        self.JUMPSPEED = 10
        self.rect = pygame.rect.Rect(x, y, 95, 120)
        self.punch = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0, 0), 3),
                                    attack.AttackFrame(1, [attack.Hitbox((60, -70, 20, 20), vector.Vector(5, -5), 70)]),
                                    attack.AttackFrame(1, [], vector.Vector(0, 0), 5)])
        self.airPunch = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0.1, 0), 3), attack.AttackFrame(1, [
            attack.Hitbox((60, -70, 20, 20), vector.Vector(5, -10), 55)], vector.Vector(10, 0), 10),
                                       attack.AttackFrame(0, [], vector.Vector(0, 0), 15)])
        self.smashPunch=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),15),attack.AttackFrame(1,[attack.Hitbox((60,-70,20,20),vector.Vector(0,-10),5)]),attack.AttackFrame(1,[],vector.Vector(0,0),3),attack.AttackFrame(2,[attack.Hitbox((60,-90,20,20),vector.Vector(8,-20),50)]),attack.AttackFrame(2,[],vector.Vector(0,0),20)])
        self.helmetShot=attack.Attack([attack.AttackFrame(0),attack.AttackFrame(0,[],vector.Vector(0,0),1,"HelmetShot"),attack.AttackFrame(0,[],vector.Vector(0,0),40)])
        self.upPunch=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),6),attack.AttackFrame(2,[attack.Hitbox((60,-90,20,20),vector.Vector(2,-12),3)],vector.Vector(1,-15),20)],True)

    def update(self, left, right, up, down, attack1, attack2, platforms):
        fighter.Fighter.update(self, left, right, up, down,platforms)
        if not self.dead and self.attack == None:
            if attack1:
                if self.grounded:
                    self.attack=self.punch
                else:
                    self.attack=self.airPunch
            elif attack2:
                if up:
                    self.attack=self.upPunch
                elif left or right:
                    self.attack=self.helmetShot
                elif self.grounded:
                    self.attack=self.smashPunch
                else:
                    self.attack=self.airPunch
            self.checkAirAttack()
            if self.attack!=None:
                self.attack.start()


class BlueGrassBilly(fighter.Fighter):
    def __init__(self, screen, x, y):
        self.imageRect=pygame.rect.Rect(0,0,75,150)
        fighter.Fighter.__init__(self, screen, x, y, 1000, "CharacterFiles/CharacterModels/BlueGrassBilly/")
        self.WALKSPEED = 7
        self.GRAVITYSTRENGTH = 1.3
        self.JUMPSPEED = 20
        self.stepLength=7
        self.rect = pygame.rect.Rect(x, y, 70, 150)

        self.punch=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),3),attack.AttackFrame(1,[attack.Hitbox((20,-80,20,20),vector.Vector(3,-5),5)]),attack.AttackFrame(1,[],vector.Vector(0,0),5)])
        self.kick=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),4),attack.AttackFrame(2,[attack.Hitbox((15,-40,20,25),vector.Vector(2,-15),15)]),attack.AttackFrame(2,[],vector.Vector(0,0),15)])
        self.kickHeadCombo=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),10),attack.AttackFrame(2,[attack.Hitbox((15,-40,20,25),vector.Vector(0,-30),10)]),attack.AttackFrame(2,[],vector.Vector(0,0),10),attack.AttackFrame(0,[],vector.Vector(0,0),20),attack.AttackFrame(0,[],vector.Vector(2,-25)),attack.AttackFrame(0,[attack.Hitbox((-30,-150,60,10),vector.Vector(5,-10),5)],vector.Vector(0,0),25)])
        self.pitchfork=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),20),attack.AttackFrame(1,[],vector.Vector(0,0),1,"Pitchfork"),attack.AttackFrame(1,[],vector.Vector(0,0),20)])
        self.upKick=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,-30),1),attack.AttackFrame(2,[attack.Hitbox((15,-40,20,25),vector.Vector(0,-31),1)],vector.Vector(0,-30),3),attack.AttackFrame(2,[],vector.Vector(0,-30),5),attack.AttackFrame(2,[],vector.Vector(0,-8)),attack.AttackFrame(2,[],vector.Vector(0,0),16),attack.AttackFrame(1,[attack.Hitbox((20,-80,20,20),vector.Vector(8,-6),15)],vector.Vector(10,-5)),attack.AttackFrame(1,[attack.Hitbox((20,-80,20,20),vector.Vector(8,-6),2)],vector.Vector(0,0),15)],True)

    def update(self, left, right, up, down, attack1, attack2,platforms):
        fighter.Fighter.update(self, left, right, up, down,platforms)
        if self.attack==None and not self.dead:
            if attack1:
                if self.grounded:
                    if left or right:
                        self.attack=self.punch
                    else:
                        self.attack=self.kick
            elif attack2:
                if up:
                    self.attack=self.upKick
                elif left or right:
                    self.attack=self.pitchfork
                elif self.grounded:
                    self.attack=self.kickHeadCombo
            self.checkAirAttack()
            if self.attack!=None:
                self.attack.start()


class CountryCarl(fighter.Fighter):
    def __init__(self, screen, x, y):
        self.imageRect=pygame.rect.Rect(0,0,200,140)
        fighter.Fighter.__init__(self, screen, x, y, 1000, "CharacterFiles/CharacterModels/CountryCarl/")
        self.WALKSPEED = 3
        self.GRAVITYSTRENGTH = 1.3
        self.JUMPSPEED = 11
        self.rect = pygame.rect.Rect(x, y, 50, 140)
        self.punch = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0, 0), 3),
                                    attack.AttackFrame(1, [attack.Hitbox((10, -90, 20, 20), vector.Vector(5, -5), 10)]),
                                    attack.AttackFrame(1, [], vector.Vector(0, 0), 5)])
        self.pigThrow=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),15),attack.AttackFrame(0,[],vector.Vector(0,0),1,"Pig"),attack.AttackFrame(0,[],vector.Vector(0,0),20)])
        self.pigJump=attack.Attack([attack.AttackFrame(2,[],vector.Vector(8,-25)),attack.AttackFrame(2,[],vector.Vector(0,0),20),attack.AttackFrame(0,[],vector.Vector(8,-15))],True)
        self.pigCharge=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),5),attack.AttackFrame(2,[attack.Hitbox((10,-120,20,120),vector.Vector(20,-7),47)],vector.Vector(15,0),20),attack.AttackFrame(2,[],vector.Vector(0,0),20)])
        self.pigSlam=attack.Attack([attack.AttackFrame(2,[],vector.Vector(0,-20)),attack.AttackFrame(2,[],vector.Vector(0,0),15),attack.AttackFrame(2,[attack.Hitbox((-20,-20,50,20),vector.Vector(15,3),20),attack.Hitbox((-80,-20,60,20),vector.Vector(-15,3),6)],vector.Vector(0,15),8),attack.AttackFrame(2,[],vector.Vector(0,0),20)])

    def update(self, left, right, up, down, attack1, attack2,platforms):
        fighter.Fighter.update(self, left, right, up, down,platforms)
        if not self.dead and self.attack == None:
            if attack1:
                if up or down:
                    self.attack=self.pigSlam
                else:
                    self.attack = self.punch
            elif attack2:
                if up:
                    self.attack=self.pigJump
                elif left or right:
                    self.attack=self.pigCharge
                else:
                    self.attack=self.pigThrow
            self.checkAirAttack()
            if self.attack!=None:
                self.attack.start()

class SinginSusan(fighter.Fighter):
    def __init__(self, screen, x, y):
        self.imageRect=pygame.rect.Rect(0,0,150,120)
        fighter.Fighter.__init__(self, screen, x, y, 1000, "CharacterFiles/CharacterModels/SinginSusan/")
        self.WALKSPEED = 4
        self.GRAVITYSTRENGTH = 1.3
        self.JUMPSPEED = 14
        self.rect = pygame.rect.Rect(x, y, 60, 100)
        self.punch = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0, 0), 3),
                                    attack.AttackFrame(1, [attack.Hitbox((35, -100, 20, 20), vector.Vector(5, -5), 10)]),
                                    attack.AttackFrame(1, [], vector.Vector(0, 0), 5)])
        self.thrust=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),3),attack.AttackFrame(2,[attack.Hitbox((40,-60,20,20),vector.Vector(8,-3),10)],vector.Vector(0,0),2),attack.AttackFrame(2,[],vector.Vector(0,0),4)])
        self.micThrow=attack.Attack([attack.AttackFrame(1,[],vector.Vector(0,0),15),attack.AttackFrame(0,[],vector.Vector(0,0),1,"Microphone"),attack.AttackFrame(0,[],vector.Vector(0,0),20)])
        self.upAttack=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),4),attack.AttackFrame(1,[attack.Hitbox((35,-100,20,20),vector.Vector(3,-18),2)],vector.Vector(2,-15),20),attack.AttackFrame(2,[attack.Hitbox((40,-60,20,20),vector.Vector(0,15),15)],vector.Vector(0.1,0)),attack.AttackFrame(2,[],vector.Vector(0.1,0),10)],True)
        self.hammerCharge=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),5),attack.AttackFrame(1,[attack.Hitbox((35,-100,20,20),vector.Vector(5,-10),9)],vector.Vector(3,0),15),attack.AttackFrame(2,[attack.Hitbox((40,-60,20,20),vector.Vector(8,-8),9)],vector.Vector(3,0),15),
        attack.AttackFrame(1,[attack.Hitbox((35,-100,20,20),vector.Vector(5,-10),9)],vector.Vector(3,0),15),attack.AttackFrame(2,[attack.Hitbox((40,-60,20,20),vector.Vector(8,-8),9)],vector.Vector(3,0),15)],True)

    def update(self, left, right, up, down, attack1, attack2,platforms):
        fighter.Fighter.update(self, left, right, up, down,platforms)
        if not self.dead and self.attack == None:
            if attack1:
                if left or right:
                    self.attack=self.thrust
                else:
                    self.attack=self.punch
            elif attack2:
                if up:
                    self.attack=self.upAttack
                elif left or right:
                    self.attack=self.hammerCharge
                else:
                    self.attack=self.micThrow
            self.checkAirAttack()
            if self.attack!=None:
                self.attack.start()

class SinisterStan(fighter.Fighter):
    def __init__(self, screen, x, y):
        self.imageRect=pygame.rect.Rect(0,0,130,130)
        fighter.Fighter.__init__(self, screen, x, y, 250, "CharacterFiles/CharacterModels/SinisterStan/")
        self.WALKSPEED = 5
        self.GRAVITYSTRENGTH = 1.3
        self.JUMPSPEED = 9
        self.rect = pygame.rect.Rect(x, y, 50, 100)
        self.punch = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0, 0), 3),
                                    attack.AttackFrame(1, [attack.Hitbox((40, -50, 20, 20), vector.Vector(5, -5), 250)]),
                                    attack.AttackFrame(1, [], vector.Vector(0, 0), 5)])
        self.airPunch = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0.1, 0), 3), attack.AttackFrame(1, [
            attack.Hitbox((40, -50, 20, 20), vector.Vector(0, 10), 40)], vector.Vector(10, 0), 10),
                                       attack.AttackFrame(0, [], vector.Vector(0, 0), 15)])
        self.knifeThrow=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),10),attack.AttackFrame(0,[],vector.Vector(0,0),1,"Knife"),attack.AttackFrame(0,[],vector.Vector(0,0),20)])

    def update(self, left, right, up, down, attack1, attack2,platforms):
        fighter.Fighter.update(self, left, right, up, down,platforms)
        if not self.dead and self.attack == None:
            if attack1:
                if self.grounded:
                    self.attack = self.punch
                else:
                    self.attack = self.airPunch
            elif attack2:
                self.attack=self.knifeThrow
            self.checkAirAttack()
            if self.attack!=None:
                self.attack.start()

class MonstrousMike(fighter.Fighter):
    def __init__(self, screen, x, y):
        self.imageRect=pygame.rect.Rect(0,0,300,200)
        fighter.Fighter.__init__(self, screen, x, y, 1000, "CharacterFiles/CharacterModels/MonstrousMike/")
        self.WALKSPEED = 3
        self.GRAVITYSTRENGTH = 1
        self.JUMPSPEED = 9
        self.rect = pygame.rect.Rect(x, y, 110, 160)
        self.punch = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0, 0), 6),
                                    attack.AttackFrame(1, [attack.Hitbox((80, -120, 40, 40), vector.Vector(5, -5), 15)]),
                                    attack.AttackFrame(1, [], vector.Vector(0, 0), 7)])
        self.smashPunch=attack.Attack([attack.AttackFrame(2,[],vector.Vector(0,0),15),attack.AttackFrame(1,[attack.Hitbox((80,-120,40,40),vector.Vector(6,12),50)]),attack.AttackFrame(1,[],vector.Vector(0,0),20)])
        self.fireball=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),10),attack.AttackFrame(3,[],vector.Vector(0,0),1,"Fireball"),attack.AttackFrame(3,[],vector.Vector(0,0),20)])
        self.punchFlurry=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),3),attack.AttackFrame(1,[attack.Hitbox((80,-120,40,40),vector.Vector(0,-20),2)],vector.Vector(0,0),2),
        attack.AttackFrame(0,[],vector.Vector(0,0),2),attack.AttackFrame(2,[attack.Hitbox((60,-180,40,40),vector.Vector(0,-0.1),2)],vector.Vector(0,0),2),
        attack.AttackFrame(0,[],vector.Vector(0,0),2),attack.AttackFrame(1,[attack.Hitbox((80,-120,40,40),vector.Vector(0,-0.1),2)],vector.Vector(0,0),2),
        attack.AttackFrame(0,[],vector.Vector(0,0),2),attack.AttackFrame(2,[attack.Hitbox((60,-180,40,40),vector.Vector(0,-0.1),2)],vector.Vector(0,0),2),
        attack.AttackFrame(0,[],vector.Vector(0,0),2),attack.AttackFrame(1,[attack.Hitbox((80,-120,40,40),vector.Vector(0,-0.1),2)],vector.Vector(0,0),2),
        attack.AttackFrame(0,[],vector.Vector(0,0),2),attack.AttackFrame(1,[attack.Hitbox((80,-120,40,40),vector.Vector(12,-7),20)],vector.Vector(0,0),1),attack.AttackFrame(1,[],vector.Vector(0,0),15)])
        self.leap=attack.Attack([attack.AttackFrame(0,[],vector.Vector(8,-25)),attack.AttackFrame(0,[],vector.Vector(0,0),15)],True)

    def update(self, left, right, up, down, attack1, attack2,platforms):
        fighter.Fighter.update(self, left, right, up, down,platforms)
        if not self.dead and self.attack == None:
            if attack1:
                if down:
                    self.attack=self.smashPunch
                else:
                    self.attack=self.punch
            elif attack2:
                if up:
                    self.attack=self.leap
                elif left or right:
                    self.attack=self.fireball
                else:
                    self.attack=self.punchFlurry
            self.checkAirAttack()
            if self.attack!=None:
                self.attack.start()


class EvilEmily(fighter.Fighter):
    def __init__(self, screen, x, y):
        self.imageRect=pygame.rect.Rect(0,0,140,120)
        fighter.Fighter.__init__(self, screen, x, y, 1000, "CharacterFiles/CharacterModels/EvilEmily/")
        self.WALKSPEED = 4
        self.GRAVITYSTRENGTH = 1.3
        self.JUMPSPEED = 13
        self.rect = pygame.rect.Rect(x, y, 50, 120)
        self.punch = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0, 0), 3),
                                    attack.AttackFrame(1, [attack.Hitbox((30, -70, 20, 20), vector.Vector(5, -5), 10)]),
                                    attack.AttackFrame(1, [], vector.Vector(0, 0), 5)])
        self.sideShoot=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),5),attack.AttackFrame(0,[attack.Hitbox((20,-120,20,120),vector.Vector(15,-3),3)],vector.Vector(18,0),15),attack.AttackFrame(1,[attack.Hitbox((30,-70,20,20),vector.Vector(2,-10),4)],vector.Vector(1,-8),15),
        attack.AttackFrame(1,[attack.Hitbox((30,-70,20,20),vector.Vector(5,-12),15)],vector.Vector(2,-16)),attack.AttackFrame(1,[],vector.Vector(0,0),15)],True)
        self.upPunch=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),7),attack.AttackFrame(1,[attack.Hitbox((30,-70,20,20),vector.Vector(4,-10),4)],vector.Vector(3,-12),20),attack.AttackFrame(1,[],vector.Vector(0,0),10)],True)

    def update(self, left, right, up, down, attack1, attack2,platforms):
        fighter.Fighter.update(self, left, right, up, down,platforms)
        if not self.dead and self.attack == None:
            if attack1:
                self.attack = self.punch
            elif attack2:
                if up:
                    self.attack=self.upPunch
                elif left or right:
                    self.attack=self.sideShoot
            self.checkAirAttack()
            if self.attack!=None:
                self.attack.start()



class BackwoodsBob(fighter.Fighter):
    def __init__(self, screen, x, y):
        self.imageRect=pygame.rect.Rect(0,0,150,120)
        fighter.Fighter.__init__(self, screen, x, y, 1000, "CharacterFiles/CharacterModels/BackwoodsBob/")
        self.WALKSPEED = 2.5
        self.GRAVITYSTRENGTH = 1.3
        self.JUMPSPEED = 12
        self.rect = pygame.rect.Rect(x, y, 60, 120)
        self.swing = attack.Attack([attack.AttackFrame(0, [], vector.Vector(0, 0), 8),
                                    attack.AttackFrame(1, [attack.Hitbox((40, -90, 40, 50), vector.Vector(5, -5), 20)]),
                                    attack.AttackFrame(1, [], vector.Vector(0, 0), 10)])
        self.jumpSwing=attack.Attack([attack.AttackFrame(0,[],vector.Vector(4,-28)),attack.AttackFrame(0,[],vector.Vector(0,0),25),attack.AttackFrame(1,[attack.Hitbox((40,-90,40,50),vector.Vector(5,15),20)],vector.Vector(0,0),10),attack.AttackFrame(1,[],vector.Vector(0,0),10)],True)
        self.axeThrow=attack.Attack([attack.AttackFrame(0,[],vector.Vector(0,0),10),attack.AttackFrame(0,[],vector.Vector(0,0),1,"Axe"),attack.AttackFrame(0,[],vector.Vector(0,0),20)])
        self.axeJump=attack.Attack([attack.AttackFrame(1,[],vector.Vector(5,-12)),attack.AttackFrame(1,[],vector.Vector(0,0),20),attack.AttackFrame(1,[attack.Hitbox((40,-90,40,50),vector.Vector(8,-7),15)],vector.Vector(5,-12)),attack.AttackFrame(1,[],vector.Vector(0,0),20),attack.AttackFrame(1,[attack.Hitbox((40,-90,40,50),vector.Vector(10,-7),20)]),attack.AttackFrame(1,[],vector.Vector(0,0),20)])

    def update(self, left, right, up, down, attack1, attack2,platforms):
        fighter.Fighter.update(self, left, right, up, down,platforms)
        if not self.dead and self.attack == None:
            if attack1:
                if left or right:
                    self.attack=self.axeJump
                else:
                    self.attack = self.swing
            elif attack2:
                if up:
                    self.attack=self.jumpSwing
                elif left or right:
                    self.attack=self.axeThrow
            self.checkAirAttack()
            if self.attack!=None:
                self.attack.start()
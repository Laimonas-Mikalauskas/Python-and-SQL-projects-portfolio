# Game Character: Space Player

import pygame
pygame.init()

surface = pygame.display.set_mode((2560, 1600))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


class SpacePlayer:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 5
        self.health = 100

    def move(self, keys):
        if keys[pygame.K_w]:  # Move up
            self.rect.y -= self.speed
        if keys[pygame.K_s]:  # Move down
            self.rect.y += self.speed
        if keys[pygame.K_a]:  # Move left
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # Move right
            self.rect.x += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def update(self, keys):
        keys = pygame.key.get_pressed()
        self.move(keys)

        if keys[pygame.K_SPACE]:
            print("Shooting!") 

class Primary_Weapon:
    def __init__(self, name, damage, range):
        self.name = "Laser Turret"
        self.damage = damage
        self.range = range
        self.ammo = 300
        self.magazine_size = 60

class Secondary_Weapon:
    def __init__(self, name, damage, range):
        self.name = "Plasma Rifle"
        self.damage = damage
        self.range = range
        self.ammo = 50 
        self.magazine_size = 10


    def shoot(self):
        print(f"Shooting {self.name} for {self.damage} damage over {self.range} range.") 
    def upgrade(self, amount):
        self.damage += amount
        print(f"Weapon upgraded by {amount}. New damage: {self.damage}")    
    def reload(self):
        print(f"{self.name} reloaded.")    
    def status(self):
        print(f"Weapon: {self.name}, Damage: {self.damage}, Range: {self.range}")    
    def switch(self, new_weapon):
        self.name = new_weapon
        print(f"Switched to weapon: {self.name}")    
    def is_functional(self):
        return self.damage > 0    
    def repair(self, amount):
        self.damage += amount
        print(f"Weapon repaired by {amount}. New damage: {self.damage}")    
    def deactivate(self):
        print(f"{self.name} deactivated.")    
    def activate(self):
        print(f"{self.name} activated.")    
    def drop(self, position):
        print(f"{self.name} dropped at position {position}.")
    def pickup(self, player):
        print(f"{self.name} picked up by player.")
    def is_loaded(self):
        return True    
    def upgrade_range(self, amount):
        self.range += amount
        print(f"Weapon range upgraded by {amount}. New range: {self.range}")
    def recharge(self):
        print(f"{self.name} recharged.")

class AmmoPack:
    def __init__(self, ammo_amount):
        self.ammo_amount = ammo_amount

    def use(self, weapon):
        weapon.damage += self.ammo_amount
        print(f"Ammo pack used. Weapon damage: {weapon.damage}")
    def upgrade(self, amount):
        self.ammo_amount += amount
        print(f"Ammo pack upgraded by {amount}. New ammo amount: {self.ammo_amount}")    
    def is_empty(self):
        return self.ammo_amount <= 0
    def refill(self, amount):
        self.ammo_amount += amount
        print(f"Ammo pack refilled by {amount}. New ammo amount: {self.ammo_amount}")    
    def status(self):
        print(f"Ammo pack ammo amount: {self.ammo_amount}")    
    def deactivate(self):
        print("Ammo pack deactivated.")    
    def activate(self):
        print("Ammo pack activated.")
    def drop(self, position):
        print(f"Ammo pack dropped at position {position}.")
    def pickup(self, player):
        print("Ammo pack picked up by player.")    
    def is_used(self):
        return self.ammo_amount <= 0
    def upgrade_ammo(self, amount):
        self.ammo_amount += amount
        print(f"Ammo pack ammo amount upgraded by {amount}. New ammo amount: {self.ammo_amount}")    
    def repair(self, amount):
        self.ammo_amount += amount
        print(f"Ammo pack repaired by {amount}. New ammo amount: {self.ammo_amount}") 
    def is_active(self):
        return self.ammo_amount > 0 
    def recharge(self, amount):
        self.ammo_amount += amount
        print(f"Ammo pack recharged by {amount}. New ammo amount: {self.ammo_amount}")


class Shield:
    def __init__(self, strength):
        self.strength = 8000

    def activate(self):
        print(f"Shield activated with strength {self.strength}.")
    def deactivate(self):
        print("Shield deactivated.")
    def absorb_damage(self, amount):
        absorbed = min(self.strength, amount)
        self.strength -= absorbed
        return amount - absorbed
    def recharge(self, amount):
        self.strength += amount
        if self.strength > 100:
            self.strength = 100
        return self.strength > 0
    def status(self):
        print(f"Shield strength: {self.strength}")
    def upgrade(self, amount):
        self.strength += amount
        print(f"Shield upgraded by {amount}. New strength: {self.strength}")    
    def repair(self, amount):
        self.strength += amount
        if self.strength > 100:
            self.strength = 100     
    def is_active(self):
        return self.strength > 0
    
class HealthPack:
    def __init__(self, heal_amount):
        self.heal_amount = heal_amount

    def use(self, player):
        player.health += self.heal_amount
        if player.health > 100:
            player.health = 100
        print(f"Health pack used. Player health: {player.health}")

    def upgrade(self, amount):
        self.heal_amount += amount
        print(f"Health pack upgraded by {amount}. New heal amount: {self.heal_amount}")    
    def is_empty(self):
        return self.heal_amount <= 0
    def refill(self, amount):
        self.heal_amount += amount
        print(f"Health pack refilled by {amount}. New heal amount: {self.heal_amount}")    
    def status(self):
        print(f"Health pack heal amount: {self.heal_amount}")    
    def deactivate(self):
        print("Health pack deactivated.")    
    def activate(self):
        print("Health pack activated.")
    def drop(self, position):
        print(f"Health pack dropped at position {position}.")
    def pickup(self, player):
        print("Health pack picked up by player.")    
    def is_used(self):
        return self.heal_amount <= 0
    def upgrade_heal(self, amount):
        self.heal_amount += amount
        print(f"Health pack heal amount upgraded by {amount}. New heal amount: {self.heal_amount}")
    def repair(self, amount):
        self.heal_amount += amount
        print(f"Health pack repaired by {amount}. New heal amount: {self.heal_amount}") 
    def is_active(self):
        return self.heal_amount > 0 
    def recharge(self, amount):
        self.heal_amount += amount
        print(f"Health pack recharged by {amount}. New heal amount: {self.heal_amount}") 


class Jetpack:
    def __init__(self, fuel):
        self.fuel = fuel

    def fly(self):
        if self.fuel > 0:
            self.fuel -= 1
            print("Flying with jetpack.")
        else:
            print("Out of fuel!")

    def recharge(self, amount):
        self.fuel += amount
        print(f"Jetpack recharged by {amount}. New fuel: {self.fuel}")    
    def status(self):
        print(f"Jetpack fuel: {self.fuel}")    
    def upgrade(self, amount):
        self.fuel += amount
        print(f"Jetpack upgraded by {amount}. New fuel: {self.fuel}")    
    def repair(self, amount):
        self.fuel += amount
        print(f"Jetpack repaired by {amount}. New fuel: {self.fuel}") 
    def is_active(self):
        return self.fuel > 0 
    def deactivate(self):
        print("Jetpack deactivated.")    
    def activate(self):
        print("Jetpack activated.")
    def drop(self, position):
        print(f"Jetpack dropped at position {position}.")
    def pickup(self, player):
        print("Jetpack picked up by player.")    
    def is_flying(self):
        return self.fuel > 0    
    def upgrade_fuel(self, amount):
        self.fuel += amount
        print(f"Jetpack fuel upgraded by {amount}. New fuel: {self.fuel}")
    def repair_fuel(self, amount):
        self.fuel += amount
        print(f"Jetpack fuel repaired by {amount}. New fuel: {self.fuel}")  
    def is_depleted(self):
        return self.fuel <= 0   
    def recharge_fuel(self, amount):
        self.fuel += amount
        print(f"Jetpack fuel recharged by {amount}. New fuel: {self.fuel}") 


class Explosive_Grenade:
    def __init__(self, name, damage, range):
        self.name = "Explosive_Grenade"
        self.damage = 100
        self.radius = 1500

class Magnetic_Mine:
    def __init__(self, name, damage, range):
        self.name = "Magnetic_Mine"
        self.damage = 150
        self.radius = 1000


    def throw(self, position):
        print(f"Explosive throwed to position {position}, dealing {self.damage} damage in radius {self.radius}.")    
    def upgrade(self, amount):
        self.damage += amount
        print(f"Explosive upgraded by {amount}. New damage: {self.damage}")    
    def is_active(self):
        return self.damage > 0    
    def deactivate(self):
        print("Explosive deactivated.")    
    def activate(self):
        print("Explosive activated.")
    def drop(self, position):
        print(f"Explosive dropped at position {position}.")
    def pickup(self, player):
        print("Explosive picked up by player.")    
    def is_thrown(self):
        return self.damage <= 0    
    def upgrade_radius(self, amount):
        self.radius += amount
        print(f"Explosive radius upgraded by {amount}. New radius: {self.radius}")    
    def repair(self, amount):
        self.damage += amount
        print(f"Explosive repaired by {amount}. New damage: {self.damage}") 
    def is_detonated(self):
        return self.damage <= 0    
    def recharge(self): 
        print("Explosive recharged.") 

class JetpackFuel:
    def __init__(self, fuel_amount):
        self.fuel_amount = fuel_amount

    def use(self, jetpack):
        jetpack.fuel += self.fuel_amount
        print(f"Jetpack fuel used. Jetpack fuel: {jetpack.fuel}")
    def upgrade(self, amount):
        self.fuel_amount += amount
        print(f"Jetpack fuel upgraded by {amount}. New fuel amount: {self.fuel_amount}")    
    def is_empty(self):
        return self.fuel_amount <= 0
    def refill(self, amount):
        self.fuel_amount += amount
        print(f"Jetpack fuel refilled by {amount}. New fuel amount: {self.fuel_amount}")    
    def status(self):
        print(f"Jetpack fuel amount: {self.fuel_amount}")    
    def deactivate(self):
        print("Jetpack fuel deactivated.")    
    def activate(self):
        print("Jetpack fuel activated.")
    def drop(self, position):
        print(f"Jetpack fuel dropped at position {position}.")
    def pickup(self, player):
        print("Jetpack fuel picked up by player.")    
    def is_used(self):
        return self.fuel_amount <= 0    

class SpacePlayerAI(SpacePlayer):
    def __init__(self, x, y, width, height, color, difficulty):
        super().__init__(x, y, width, height, color)
        self.difficulty = difficulty

    def make_decision(self):
        if self.difficulty == "easy":
            print("AI makes a simple decision.")
        elif self.difficulty == "medium":
            print("AI makes a moderate decision.")
        elif self.difficulty == "hard":
            print("AI makes a complex decision.")

    def patrol(self, path):
        print(f"AI patrolling along path: {path}") 


class SpacePlayerStealth(SpacePlayer):
    def __init__(self, x, y, width, height, color, stealth_level):
        super().__init__(x, y, width, height, color)
        self.stealth_level = stealth_level
        self.is_hidden = False

    def enter_stealth_mode(self):
        self.is_hidden = True
        print(f"Player entered stealth mode with level {self.stealth_level}.")    
    def exit_stealth_mode(self):
        self.is_hidden = False
        print("Player exited stealth mode.")    
    def increase_stealth(self):
        self.stealth_level += 1
        print(f"Increased stealth level to {self.stealth_level}.")    
    def decrease_stealth(self):
        if self.stealth_level > 0:
            self.stealth_level -= 1
            print(f"Decreased stealth level to {self.stealth_level}.")    
    def is_detected(self, enemy):
        detection_chance = enemy.detection_ability - self.stealth_level
        detected = detection_chance > 0
        print(f"Player detected by enemy: {detected}.")
        return detected    
    def sneak_attack(self, enemy):
        if self.is_hidden:
            damage = 50 + (10 * self.stealth_level)
            enemy.health -= damage
            print(f"Performed sneak attack on enemy for {damage} damage.")
        else:
            print("Cannot perform sneak attack while not in stealth mode.")    
    def hide(self):
        if not self.is_hidden:
            self.enter_stealth_mode()
        else:
            print("Player is already hidden.")    
    def reveal(self):
        if self.is_hidden:
            self.exit_stealth_mode()
        else:
            print("Player is already revealed.")    
    def update_stealth(self, keys):
        self.update(keys)
        if self.is_hidden:
            print("Player is moving stealthily.")
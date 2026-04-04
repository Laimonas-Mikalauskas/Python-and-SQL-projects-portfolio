# Sci-fi FPS Defense Of Trappist 1-d game environment setup

import pygame
pygame.init()

if __name__ == "__Defense Of Trappist 1-d__":
    pygame.init()

    # Set up the game window
    surface = pygame.display.set_mode((2560, 1600))
    pygame.display.is_fullscreen()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # Quit Pygame
    pygame.quit()

# CHARACTER DECORATORS

class Character:
    def __init__(self, character, health, armor, power_ups, special_ability, weapon, ammo, type):
        self.character = "Starfighter_X"
        self.health = 1200
        self.armor = 800
        self.power_ups = "Shield_Boost"
        self.special_ability = "Cloaking"
        self.weapon = "Plasma_Cannon"
        self.ammo = 500
        self.type = "Player" 

    @classmethod    
    def create_character(cls, character, health, armor, power_ups, special_ability, weapon, ammo, type):              
        return cls(character, health, armor, power_ups, special_ability, weapon, ammo, type) 
       
# MISSION DECORATORS

class Mission:
    def __init__(self, mission, environment, difficulty):
        self.mission = "Destroy_Alien_Mothership"
        self.environment = "Asteroid_Field"
        self.difficulty = "Hard"

    @classmethod
    def create_mission(cls, mission, environment, difficulty):
        return cls(mission, environment, difficulty) 

# LEVEL DECORATORS

class Level:
    def __init__(self, level, enemies, time_limit, power_level, obstacles, checkpoints):
        self.level = 7
        self.enemies = "Alien_Fighters"
        self.time_limit = 400
        self.power_level = 9500
        self.obstacles = "Meteor_Showers"
        self.checkpoints = 4

    @classmethod
    def create_level(cls, level, enemies, time_limit, power_level, obstacles, checkpoints):
        return cls(level, enemies, time_limit, power_level, obstacles, checkpoints) 

# ENVIRONMENT DECORATORS

class Environment:
    def __init__(self, environment, weather_conditions, gravity, terrain_type):
        self.environment = "Nebula_Zone"
        self.weather_conditions = "Cosmic_Radiation"
        self.gravity = "Low_Gravity"
        self.terrain_type = "Asteroid_Belts"
       
    @classmethod
    def create_environment(cls, environment, weather_conditions, gravity, terrain_type):
        return cls(environment, weather_conditions, gravity, terrain_type)
    
# HEADQUARTERS DECORATORS

class Headquarters:
    def __init__(self, hq_name, location, defense_level):
        self.hq_name = "Earth_Command_Center"
        self.location = "Lunar_Base"
        self.defense_level = "Maximum"

    @classmethod
    def create_headquarters(cls, hq_name, location, defense_level):
        return cls(hq_name, location, defense_level)
    
# HEADQUARTERS LOCATIONS DECORATORS 

class HeadquartersLocation:
    def __init__(self, location_name, coordinates, security_level):
        self.location_name = "Sector_7G"
        self.coordinates = "X:300 Y:450 Z:600"
        self.security_level = "High"

    @classmethod
    def create_headquarters_location(cls, location_name, coordinates, security_level):
        return cls(location_name, coordinates, security_level)
  
# ALLIES DECORATORS

class Allies:
    def __init__(self, ally_name, ally_type, support_ability):
        self.ally_name = "Galactic_Federation"
        self.ally_type = "Space_Fleet"
        self.support_ability = "Reinforcements"

    @classmethod
    def create_allies(cls, ally_name, ally_type, support_ability):
        return cls(ally_name, ally_type, support_ability)
    
# ALLY TYPES DECORATORS

class AllyType:
    def __init__(self, type_name, strength, weakness):
        self.type_name = "Battlecruiser"
        self.strength = "Heavy_Armor"
        self.weakness = "Slow_Speed"

    @classmethod
    def create_ally_type(cls, type_name, strength, weakness):
        return cls(type_name, strength, weakness)
    
# ALLY POWERS DECORATORS

class AllyPower:
    def __init__(self, power_name, effect, duration):
        self.power_name = "Shield_Overload"
        self.effect = "Temporary_Invincibility"
        self.duration = 20

    @classmethod
    def create_ally_power(cls, power_name, effect, duration):
        return cls(power_name, effect, duration) 
    
# ALLY WEAKNESSES DECORATORS

class AllyWeakness:
    def __init__(self, weakness_name, exploit_method, duration):
        self.weakness_name = "EMP_Missiles"
        self.exploit_method = "Disable_Systems"
        self.duration = 10

    @classmethod
    def create_ally_weakness(cls, weakness_name, exploit_method, duration):
        return cls(weakness_name, exploit_method, duration)

    
# ALLY WEAPONS DECORATORS

class AllyWeapon:
    def __init__(self, weapon_name, damage, range):
        self.weapon_name = "Laser_Turrets"
        self.damage = 300
        self.range = 1000

    @classmethod
    def create_ally_weapon(cls, weapon_name, damage, range):
        return cls(weapon_name, damage, range)

# ENEMY HEADQUARTERS DECORATORS

class EnemyHeadquarters:
    def __init__(self, hq_name, location, defense_level):
        self.hq_name = "Alien_Mothership"
        self.location = "Deep_Space"
        self.defense_level = "Maximum"

    @classmethod
    def create_enemy_headquarters(cls, hq_name, location, defense_level):
        return cls(hq_name, location, defense_level)

# ENEMY HEADQUARTERS LOCATIONS DECORATORS

class EnemyHeadquartersLocation:
    def __init__(self, location_name, coordinates, security_level):
        self.location_name = "Zeta_Reticuli_Sector"
        self.coordinates = "X:450 Y:320 Z:780"
        self.security_level = "High"

    @classmethod
    def create_enemy_headquarters_location(cls, location_name, coordinates, security_level):
        return cls(location_name, coordinates, security_level)     


# ENEMY DECORATORS

class Enemy:
    def __init__(self, enemy_name, enemy_type, attack_power):
        self.enemy_name = "Alien_Scout"
        self.enemy_type = "Alien_Fighter"
        self.attack_power = 100

    @classmethod
    def create_enemy(cls, enemy_name, enemy_type, attack_power):
        return cls(enemy_name, enemy_type, attack_power)
    
# ENEMY TYPES DECORATORS

class EnemyType:
    def __init__(self, type_name, strength, weakness):
        self.type_name = "Stealth_Ship"
        self.strength = "Invisibility"
        self.weakness = "Low_Shields"

    @classmethod
    def create_enemy_type(cls, type_name, strength, weakness):
        return cls(type_name, strength, weakness)

# ENEMY POWERS DECORATORS

class EnemyPower:
    def __init__(self, power_name, effect, duration):
        self.power_name = "Cloaking_Device"
        self.effect = "Temporary_Invisibility"
        self.duration = 15

    @classmethod
    def create_enemy_power(cls, power_name, effect, duration):
        return cls(power_name, effect, duration)
    
# ENEMY WEAKNESSES DECORATORS

class EnemyWeakness:
    def __init__(self, weakness_name, exploit_method, duration):
        self.weakness_name = "EMP_Blaster"
        self.exploit_method = "Disable_Systems"
        self.duration = 10

    @classmethod
    def create_enemy_weakness(cls, weakness_name, exploit_method, duration):
        return cls(weakness_name, exploit_method, duration) 
 
# ENEMY WEAPONS DECORATORS

class EnemyWeapon:
    def __init__(self, weapon_name, damage, range):
        self.weapon_name = "Ion_Blaster"
        self.damage = 250
        self.range = 800

    @classmethod
    def create_enemy_weapon(cls, weapon_name, damage, range):
        return cls(weapon_name, damage, range)     

# SCORE DECORATORS

class Score:
    def __init__(self, score, bonus_points, retry_attempts):
        self.score = 2000
        self.bonus_points = 800
        self.retry_attempts = 3

    @classmethod
    def create_score(cls, score, bonus_points, retry_attempts):
        return cls(score, bonus_points, retry_attempts)
    
# GAME DECORATORS

class Game:
    def __init__(self, game_name, difficulty, time_limit):
        self.game_name = "In Orbit Of The Trappist 1-d"
        self.difficulty = "Easy, Medium, Hard"
        self.time_limit = 400
        
    @classmethod
    def create_game(cls, game_name, difficulty, time_limit):
        return cls(game_name, difficulty, time_limit)

# SOUNDTRACK DECORATORS

class Soundtrack:
    def __init__(self, soundtrack_name, composer, duration):
        self.soundtrack_name = "Epic_Space_Battle"
        self.composer = "Synth_Master"
        self.duration = 600

    @classmethod
    def create_soundtrack(cls, soundtrack_name, composer, duration):
        return cls(soundtrack_name, composer, duration)
    
# GAME GENRE DECORATORS

class GameGenre:
    def __init__(self, genre_name, description, popularity_rank):
        self.genre_name = "Sci-Fi_Shooter"
        self.description = "Fast-paced_space_combat_with_futuristic_weapons"
        self.popularity_rank = 1


# GAME VERSION DECORATORS

class GameVersion:
    def __init__(self, version_number, release_date, platform):
        self.version_number = "1.0.0"
        self.release_date = "2025-12-01"
        self.platform = "PC, Console"

    @classmethod
    def create_game_version(cls, version_number, release_date, platform):
        return cls(version_number, release_date, platform)

# GAME RELEASE YEAR DECORATORS

class GameReleaseYear:
    def __init__(self, release_year, updates, patches):
        self.release_year = 2025
        self.updates = 5
        self.patches = 3

    @classmethod
    def create_game_release_year(cls, release_year, updates, patches):
        return cls(release_year, updates, patches)
    
# GAME DEVELOPER DECORATORS
class GameDeveloper:
    def __init__(self, developer_name, location, founded_year):
        self.developer_name = "Galactic_Games_Studio"
        self.location = "Silicon_Valley"
        self.founded_year = 2010

    @classmethod
    def create_game_developer(cls, developer_name, location, founded_year):
        return cls(developer_name, location, founded_year)  

# GAME PUBLISHER DECORATORS

class GamePublisher:
    def __init__(self, publisher_name, location, founded_year):
        self.publisher_name = "Universal_Entertainment"
        self.location = "New_York_City"
        self.founded_year = 2005

    @classmethod
    def create_game_publisher(cls, publisher_name, location, founded_year):
        return cls(publisher_name, location, founded_year)

# Creating instances of each class    
Game = Game.create_game("In Orbit Of The Trappist 1-d", "Easy, Medium, Hard", 400)
Character = Character.create_character("Starfighter_X", 1200, 800, "Shield_Boost", "Cloaking", "Plasma_Cannon", 500, "Player")
Mission = Mission.create_mission("Destroy_Alien_Mothership", "Asteroid_Field", "Hard")
Level = Level.create_level(7, "Alien_Fighters", 400, 9500, "Meteor_Showers", 4)
Environment = Environment.create_environment("Nebula_Zone", "Cosmic_Radiation", "Low_Gravity", "Asteroid_Belts")
Headquarters = Headquarters.create_headquarters("Earth_Command_Center", "Lunar_Base", "Maximum")
HeadquartersLocation = HeadquartersLocation.create_headquarters_location("Sector_7G", "X:300 Y:450 Z:600", "High")


# ALLIES DECORATORS
Allies = Allies.create_allies("Galactic_Federation", "Space_Fleet", "Reinforcements")
AllyType = AllyType.create_ally_type("Battlecruiser", "Heavy_Armor", "Slow_Speed")
AllyPower = AllyPower.create_ally_power("Shield_Overload", "Temporary_Invincibility", 20)
AllyWeakness = AllyWeakness.create_ally_weakness("EMP_Missiles", "Disable_Systems", 10)
AllyWeapon = AllyWeapon.create_ally_weapon("Laser_Turrets", 300, 1000) 

# ENEMY DECORATORS
EnemyHeadquarters = EnemyHeadquarters.create_enemy_headquarters("Alien_Mothership", "Deep_Space", "Maximum")
EnemyHeadquartersLocation = EnemyHeadquartersLocation.create_enemy_headquarters_location("Zeta_Reticuli_Sector", "X:450 Y:320 Z:780", "High")
Enemy = Enemy.create_enemy("Alien_Scout", "Alien_Fighter", 100)
EnemyType = EnemyType.create_enemy_type("Stealth_Ship", "Invisibility", "Low_Shields")
EnemyPower = EnemyPower.create_enemy_power("Cloaking_Device", "Temporary_Invisibility", 15)
EnemyWeakness = EnemyWeakness.create_enemy_weakness("EMP_Blaster", "Disable_Systems", 10)
EnemyWeapon = EnemyWeapon.create_enemy_weapon("Ion_Blaster", 250, 800)

Score = Score.create_score(2000, 800, 3)

Soundtrack = Soundtrack.create_soundtrack("Epic_Space_Battle", "Synth_Master", 300)

GameGenre = GameGenre("Sci-Fi_Shooter", "Fast-paced_space_combat_with_futuristic_weapons", 1)


GameReleaseYear = GameReleaseYear.create_game_release_year(2025, 5, 3)


GameVersion = GameVersion.create_game_version("1.0.0", "2025-12-01", "PC, Console")
GameDeveloper = GameDeveloper.create_game_developer("Silicon_Valley", "Galactic_Games_Studio", 2010)
GamePublisher = GamePublisher.create_game_publisher("Universal_Entertainment", "New_York_City", 2005)

print("Game:", Game.game_name)
print("Character:", Character.character)
print("Mission:", Mission.mission)
print("Level:", Level.level)
print("Environment:", Environment.environment)
print("Headquarters:", Headquarters.hq_name)
print("Allies:", Allies.ally_name)
print("Enemy Headquarters:", EnemyHeadquarters.hq_name)
print("Enemy:", Enemy.enemy_name)
print("Score:", Score.score)
print("Soundtrack:", Soundtrack.soundtrack_name)
print("Game Genre:", GameGenre.genre_name)
print("Game Version:", GameVersion.version_number)
print("Game Developer:", GameDeveloper.developer_name)
print("Game Publisher:", GamePublisher.publisher_name)  

















    
# Defense Of Trappist 1-d Game Modes

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
        self.health = 100
    
    def update(self, keys):
        pass


class Space_Player_Campaign (SpacePlayer):
    def __init__(self, mission_objectives, level, difficulty):
        self.mission_objectives = mission_objectives
        self.difficulty = difficulty

    def start_mission(self, mission):
        print(f"Starting mission: {mission} in level {self.level}.")    
    def complete_objective(self, objective):
        if objective in self.mission_objectives:
            self.mission_objectives.remove(objective)
            print(f"Completed objective: {objective}.")
        else:
            print(f"Objective: {objective} not found.")    
    def fail_mission(self):
        print(f"Mission failed in level {self.level}.")    
    def advance_level(self):
        self.level += 1
        print(f"Advanced to level {self.level}.")    
    def add_objective(self, objective):
        self.mission_objectives.append(objective)
        print(f"Added objective: {objective}.")    
    def get_objectives(self):
        return self.mission_objectives    
    def is_mission_complete(self):
        return len(self.mission_objectives) == 0    
    def restart_mission(self):
        print(f"Restarting mission in level {self.level}.")    
    
    def save_progress(self):
        print(f"Progress saved at level {self.level}.")    
    def load_progress(self, level, objectives):
        self.level = level
        self.mission_objectives = objectives
        print(f"Progress loaded at level {self.level} with objectives: {self.mission_objectives}.")    
    def update_campaign(self, keys):
        self.update(keys)
        if self.is_mission_complete():
            self.advance_level()                    


class SpacePlayerMultiplayer(SpacePlayer):
    def __init__(self, mission_objectives, level, difficulty):
        self.mission_objectives = mission_objectives
        self.difficulty = difficulty
        self.player_id = id(self)


    def send_position(self):
        print(f"Sending position of player {self.player_id}: {self.rect.topleft}")
    def receive_position(self, position):
        self.rect.topleft = position
        print(f"Received position for player {self.player_id}: {self.rect.topleft}")    
    
    def sync_health(self, health):
        self.health = health
        print(f"Synced health for player {self.player_id}: {self.health}")
    def sync_weapon(self, weapon):
        print(f"Synced weapon for player {self.player_id}: {weapon.name}")    
    def sync_shield(self, shield):
        print(f"Synced shield for player {self.player_id}: {shield.strength}")    
   
    def send_action(self, action):
        print(f"Player {self.player_id} performed action: {action}")    
    def receive_action(self, action):
        print(f"Player {self.player_id} received action: {action}")    
    def is_connected(self):
        return True    
    def disconnect(self):
        print(f"Player {self.player_id} disconnected.")    
    def reconnect(self):
        print(f"Player {self.player_id} reconnected.")    
   
    def get_latency(self):
        return 50  # Dummy latency value in ms    
    def handle_lag(self):
        print(f"Handling lag for player {self.player_id}.")    
    def update_multiplayer(self, keys):
        self.update(keys)
        self.send_position()    
    def chat(self, message):
        print(f"Player {self.player_id} says: {message}")    
    def receive_chat(self, message):
        print(f"Player {self.player_id} received message: {message}")    
    def is_host(self):
        return self.player_id == 1    
    def promote_to_host(self):
        print(f"Player {self.player_id} promoted to host.")    
    def demote_from_host(self):
        print(f"Player {self.player_id} demoted from host.")    
    
    def sync_score(self, score):
        print(f"Synced score for player {self.player_id}: {score}")    
    def get_score(self):
        return 0  # Dummy score value   
    def update_score(self, points):
        print(f"Updated score for player {self.player_id} by {points} points.") 
    
    def is_alive(self):
        return self.health > 0    
    def respawn(self, position):
        self.rect.topleft = position
        self.health = 100
        print(f"Player {self.player_id} respawned at position {position}.")
    def send_stats(self):
        print(f"Sending stats for player {self.player_id}: Health={self.health}, Score={self.get_score()}")
    def receive_stats(self, health, score):
        self.health = health
        print(f"Received stats for player {self.player_id}: Health={self.health}, Score={score}")    
    def is_spectator(self):
        return False    
    def toggle_spectator_mode(self):
        print(f"Toggling spectator mode for player {self.player_id}.")  

class SpacePlayerCoop(SpacePlayer):
    def __init__(self, x, y, width, height, color, team_id):
        super().__init__(x, y, width, height, color)
        self.team_id = team_id

    def assist_teammate(self, teammate):
        print(f"Assisting teammate in team {self.team_id}.")    
    def share_resources(self, teammate, resource_type, amount):
        print(f"Sharing {amount} of {resource_type} with teammate in team {self.team_id}.")    
    def revive_teammate(self, teammate):
        print(f"Reviving teammate in team {self.team_id}.")    
    def communicate(self, message):
        print(f"Team {self.team_id} communication: {message}")    
    def receive_communication(self, message):
        print(f"Team {self.team_id} received message: {message}")    
    
    def is_team_alive(self, team):
        return all(member.health > 0 for member in team)    
    def team_respawn(self, team, position):
        for member in team:
            member.rect.topleft = position
            member.health = 100
        print(f"Team {self.team_id} respawned at position {position}.")    
    def sync_team_stats(self, team):
        for member in team:
            print(f"Syncing stats for team {self.team_id} member: Health={member.health}")    
    def get_team_score(self, team):
        return sum(member.get_score() for member in team)    
    def update_team_score(self, team, points):
        for member in team:
            member.update_score(points)
        print(f"Updated team {self.team_id} score by {points} points.")    
    def is_team_spectator(self, team):
        return all(member.is_spectator() for member in team)    
    def toggle_team_spectator_mode(self, team):     
        for member in team:
            member.toggle_spectator_mode()
        print(f"Toggling spectator mode for team {self.team_id}.")    
    def send_team_stats(self, team):
        for member in team:
            member.send_stats()    
    def receive_team_stats(self, team, stats):
        for member, stat in zip(team, stats):
            member.receive_stats(stat['health'], stat['score'])    
    def is_team_host(self, team):
        return any(member.is_host() for member in team)    
    def promote_team_host(self, team, member):
        member.promote_to_host()
        print(f"Member promoted to host in team {self.team_id}.")    
    def demote_team_host(self, team, member):   
        member.demote_from_host()
        print(f"Member demoted from host in team {self.team_id}.")      
    def update_coop(self, keys):
        self.update(keys)
        self.send_team_stats([self])

    def chat_team(self, message):
        print(f"Team {self.team_id} says: {message}")    
    def receive_team_chat(self, message):
        print(f"Team {self.team_id} received message: {message}")
    def is_team_leader(self, team):
        return self.team_id == 1    
    def assign_team_leader(self, member):
        print(f"Member assigned as leader in team {self.team_id}.")    
    def remove_team_leader(self, member):
        print(f"Member removed as leader in team {self.team_id}.")
    def get_team_members(self, team):
        return team
    def add_team_member(self, team, member):
        team.append(member)
        print(f"Member added to team {self.team_id}.")    
    def remove_team_member(self, team, member):
        team.remove(member)
        print(f"Member removed from team {self.team_id}.")    
    def get_team_objectives(self, team):
        return []    
    def add_team_objective(self, team, objective):
        print(f"Added objective to team {self.team_id}: {objective}.")    
    def complete_team_objective(self, team, objective):
        print(f"Completed objective for team {self.team_id}: {objective}.")    
    def fail_team_mission(self, team):
        print(f"Team {self.team_id} mission failed.")    
    def restart_team_mission(self, team):
        print(f"Restarting mission for team {self.team_id}.")    
    def save_team_progress(self, team):
        print(f"Team {self.team_id} progress saved.")    
    def load_team_progress(self, team, level, objectives):
        print(f"Team {self.team_id} progress loaded at level {level} with objectives: {objectives}.")            


    

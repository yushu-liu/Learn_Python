import sys
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from alien import Alien
from game_stats import GameStats

import pygame

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set the background Color
    bg_color = (230,230,230)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings,screen,ship,bullets)

        if stats.game_active:
            ship.update()

            # Make the most recently drawn screen visible
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,ship,screen,aliens,bullets)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#Screen Dimensions
#Fix Constants Pep-8; Caps
screen_width = 700
screen_height = 400

class Game(object):
    """Contains the game logic, events, and display."""

    def __init__(self):
        """Constructs block lists, blocks, and game conditions."""
        self.score = 0
        self.game_over = False
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        #Good Block List Creation
        for i in range(35):
            # Block Image
            block = Block("snowman_sprite.png")
            # Block Locations
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)
            # Add Blocks to Lists
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)

        #Bad Block List Creation
        for i in range(25):
            block = Block("robot_sprite.png")
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        self.player = Player(100, 100)
        self.all_sprites_list.add(self.player)

    def display_screen(self,screen):
        screen.fill(WHITE)
        background_position = [0, 0]
        background_image = pygame.image.load("snowy_village.png").convert()

        screen.blit(background_image, [0, 0])


        if self.game_over:
            screen.fill(BLACK)
            font = pygame.font.SysFont("Courier",30)
            text = font.render("Game Over. \nHit Space to Play Again", True, WHITE)
            center_text_x = (screen_width // 2) - (text.get_width() // 2)
            center_text_y = (screen_height // 2) - (text.get_height() // 2)
            screen.blit(text, [center_text_x, center_text_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


    def game_events(self):
        """Contains Game Processes & Events (Controls)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.K_SPACE:
                if self.game_over:
                    self.__init__()

            #User Presses Key Down
            elif event.type == pygame.KEYDOWN:
                #which key and adjust speed
                if event.key == pygame.K_a:
                    self.player.changespeed(-3,0)
                elif event.key == pygame.K_d:
                    self.player.changespeed(3,0)
                elif event.key == pygame.K_w:
                    self.player.changespeed(0,-3)
                elif event.key == pygame.K_s:
                    self.player.changespeed(0,3)

            #User Stops Pressing Key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.changespeed(3,0)
                elif event.key == pygame.K_d:
                    self.player.changespeed(-3,0)
                elif event.key == pygame.K_w:
                    self.player.changespeed(0,3)
                elif event.key == pygame.K_s:
                    self.player.changespeed(0,-3)

        return False

    def game_logic(self):
        """Updates block positions and checks for block collisions."""
        if not self.game_over:
            self.all_sprites_list.update()

            # Block Collision Sounds
            good_block_sound = pygame.mixer.Sound("good_block.wav")
            bad_block_sound = pygame.mixer.Sound("bad_block.wav")

            #Check for Collisions between player and Other Blocks
            good_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.good_block_list, True)
            bad_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.bad_block_list, True)

            #Good Collisions
            for block in good_blocks_hit_list:
                self.score += 1
                good_block_sound.play()
                print(self.score)

            #Bad Collisions
            for block in bad_blocks_hit_list:
                self.score -= 1
                bad_block_sound.play()
                print(self.score)

            #Game Over Condition
            if len(good_blocks_hit_list) == 35:
                self.game_over = True


class Block(pygame.sprite.Sprite):
   """Creates the attributes for all blocks."""

    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(WHITE)
        #Position Update, Setting rect.x and rect.y
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    """ Create's player controlled block."""

    def __init__(self, x, y):
        super().__init__()
        #Height,Width,Color
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)
        #Pass-in Location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #Starting Speed
        self.change_x = 0
        self.change_y = 0


    def changespeed(self, x, y):
        """ Changes Player Speed."""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ New position for player block."""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        #Screen Edge Check
        #Left Screen Check
        if self.rect.x < 0:
            self.rect.x = 0

        #Right Screen Check
        if self.rect.x > (700 - 15):
            self.rect.x = (700 - 15)

        #Top Screen Check
        if self.rect.y < 0:
            self.rect.y = 0

        #Bottom Screen Check
        if self.rect.y > (400 - 15):
            self.rect.y = (400 - 15)


def main():

    pygame.init()

    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Save Snowy Village!")

    done = False

    clock = pygame.time.Clock()

    game = Game()

    while not done:

        done = game.game_events()


        game.game_logic()


        game.display_screen(screen)


        #frame_count = 0
        #frame_rate = 60
        #start_time = 90


        #Main Game Loop

        #Score
        """font = pygame.font.SysFont('Courier', 25)
        scoretext = font.render("Score:" + str(score), True, BLACK)
        screen.blit(scoretext, [10, 10])

        # Countdown Timer
        seconds_total = start_time - (frame_count // frame_rate)
        if seconds_total < 0:
            seconds_total = 0
        # Modulus Remainder Calcs Seconds
        minutes = seconds_total // 60
        seconds = seconds_total % 60

        displayed_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
        text = font.render(displayed_string, True, BLACK)
        screen.blit(text, [450, 10])"""

        #frame_count += 1

        #pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
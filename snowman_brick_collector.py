import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

class Game(object):
    """Contains the game logic, events, and display."""

    def __init__(self):
        """Constructs block lists, blocks, and game conditions."""
        self.score = 0
        self.game_over = False
        self.game_over_hit_count = 0

        # Timer Count
        self.frame_count = 0
        self.frame_rate = 60
        self.start_time = 60
        self.minutes = 0
        self.seconds = 0
        self.seconds_total = 1

        #Block Lists
        self.good_block_list = pygame.sprite.Group()
        self.bad_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        #Player Block
        self.player = Player(100, 100)
        self.all_sprites_list.add(self.player)

        self.snowflake_list = []
        self.snowflake_item = [1]

        #Good Block List Creation
        for i in range(30):
            # Block Image
            block = Block("snowman_sprite.png")
            # Block Locations
            block.rect.x = random.randrange(10,650)
            block.rect.y = random.randrange(50,360)
            # Add Blocks to Lists
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)

        #Bad Block List Creation
        for i in range(20):
            block = Block("robot_sprite.png")
            block.rect.x = random.randrange(10,650)
            block.rect.y = random.randrange(50,360)
            self.bad_block_list.add(block)
            self.all_sprites_list.add(block)

        #Snowflake List Creation (Non-Sprite)
        for i in range(50):
            snow_x = random.randrange(0,700)
            snow_y = random.randrange(0,400)
            self.snowflake_list.append([snow_x,snow_y])



    def display_screen(self,screen):
        """Draws sprites and text to screen."""
        screen.fill(WHITE)
        background_image = pygame.image.load("snowy_village.png").convert()

        screen.blit(background_image, [0, 0])

        #Score Display
        font = pygame.font.SysFont('Courier', 25)
        score_text = font.render("Score:" + str(self.score), True, BLACK)

        #Timer Display
        displayed_string = "Time left: {0:02}:{1:02}".format(self.minutes, self.seconds)
        timer_string = font.render(displayed_string, True, BLACK)

        if self.game_over:
            screen.fill(BLACK)
            font = pygame.font.SysFont("Courier",30)
            game_over_text = font.render("Game Over. Click to Play Again", True, WHITE)
            center_text_x = (SCREEN_WIDTH // 2) - (game_over_text.get_width() // 2)
            center_text_y = (SCREEN_HEIGHT // 2) - (game_over_text.get_height() // 2)

            screen.blit(game_over_text, [center_text_x, center_text_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

            screen.blit(score_text, [10, 10])

            screen.blit(timer_string, [450, 10])

            pygame.draw.circle(screen, WHITE, self.snowflake_item, 2)

            pygame.display.flip()

    def game_events(self):
        """Contains Game Processes & Events (Controls)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            for self.block in good_blocks_hit_list:
                self.score += 1
                self.game_over_hit_count += 1
                good_block_sound.play()
                print(self.score)

            #Bad Collisions
            for self.block in bad_blocks_hit_list:
                self.score -= 1
                bad_block_sound.play()
                print(self.score)

            #Game Over Condition
            if self.score == 20 or self.score == -5 or self.seconds_total == 0 or self.game_over_hit_count == 30:
                self.game_over = True

            #Countdown Timer
            self.seconds_total = self.start_time - (self.frame_count // self.frame_rate)
            if self.seconds_total < 0:
                self.seconds_total = 0
            # Modulus Remainder Calcs Seconds
            self.minutes = self.seconds_total // 60
            self.seconds = self.seconds_total % 60

            self.frame_count += 1

            #Snowflake Drawing
            for self.snowflake_item in self.snowflake_list:
                self.snowflake_item[1] += 1

                #Snowflake Reappears above screen
                if self.snowflake_item[1] > 400:
                    self.snowflake_item[1] = random.randrange(-20,-5)
                    self.snowflake_item[0] = random.randrange(700)

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

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Save Snowy Village!")

    done = False

    clock = pygame.time.Clock()

    game = Game()

    while not done:

        done = game.game_events()

        game.game_logic()

        game.display_screen(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
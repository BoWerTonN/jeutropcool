import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, name, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f"../sprites/{name}.png")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            "up": self.get_image(0, 96),
            "down": self.get_image(0, 0),
            "right": self.get_image(0, 64),
            "left": self.get_image(0, 32)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 1.2

    def save_location(self): self.old_position = self.position.copy()

    def move_player(self, type):
        self.image = self.images[type]
        self.image.set_colorkey([0, 0, 0])
        if type == "up":
            self.position[1] -= self.speed
        elif type == "down":
            self.position[1] += self.speed
        elif type == "right":
            self.position[0] += self.speed
        elif type == "left":
            self.position[0] -= self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.update()

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

class Player(Entity):

    def __init__(self):
        super().__init__("player", 0, 0)

class NPC(Entity):

    def __init__(self, name):
        super().__init__(name, 0, 0)
        self.nb_points = nb_points

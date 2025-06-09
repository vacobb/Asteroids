import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # Player sprite
    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, other_object):
        return pygame.math.Vector2.distance_to(self.position, other_object.position) <= (self.radius + other_object.radius)
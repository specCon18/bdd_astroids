import circleshape
import constants
import pygame

class Player(circleshape.CircleShape):
    
    containers = []

    def __init__(self,x,y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)


    def rotate(self,dt,dir):
        if dir == "right":
            self.rotation += dt*constants.PLAYER_ROTATION_SPEED
        else:
            self.rotation += -dt*constants.PLAYER_ROTATION_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt,"left")
        if keys[pygame.K_d]:
            self.rotate(dt,"right")
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt 

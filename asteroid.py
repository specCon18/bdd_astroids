import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    
    containers = []

    def __init__(self, x, y, radius):
         super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(rand_angle)
            new_velocity2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = new_velocity2 * 1.2

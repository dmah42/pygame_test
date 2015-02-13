import pygame
import sys

from pygame.locals import *
from random import randint, uniform

if not pygame.font: print 'Warning: fonts disabled'

SIZE = WIDTH, HEIGHT = 640, 400
BG_COLOR = (240, 245, 250)
NUM_BALLS = 10

MAX_SPEED = 5


class Ball(pygame.sprite.Sprite):
  def __init__(self, image, x, y, speed):
    pygame.sprite.Sprite.__init__(self)
    self._speed = speed
    self.image = pygame.image.load(image)
    self.rect = self.image.get_rect().move(x, y)

  def update(self):
    self.rect = self.rect.move(self._speed)
    if self.rect.left < 0 or self.rect.right > WIDTH:
      self._speed[0] = self._speed[0] * -0.9
    if self.rect.top < 0 or self.rect.bottom > HEIGHT:
      self._speed[1] = self._speed[1] * -0.99

    self._speed[1] += 0.1

  def maybe_pop(self, pos):
    return self.rect.collidepoint(pos)

def create_balls(num_balls):
  balls = []
  for b in range(num_balls):
    balls.append(
        Ball('ball.gif',
             randint(0, WIDTH),
             randint(0, HEIGHT / 2),
             [uniform(-MAX_SPEED, MAX_SPEED), 0]))
  return balls


def main():
  pygame.init()

  screen = pygame.display.set_mode(SIZE)
  pygame.display.set_caption('BALLS')

  # Create the background and show it as soon as possible.
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill(BG_COLOR)

  if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render('Pop the balloons!', 1, (10, 10, 10))
    textpos = text.get_rect(centerx = background.get_width() / 2)
    background.blit(text, textpos)

  screen.blit(background, (0, 0))
  pygame.display.flip()

  # Finish set up
  balls = create_balls(NUM_BALLS)
  ballsprites = pygame.sprite.RenderPlain(tuple(balls))

  clock = pygame.time.Clock()

  while True:
    clock.tick(60)

    for ev in pygame.event.get():
      if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
        return
      elif ev.type == MOUSEBUTTONDOWN:
        for b in balls:
          if b.maybe_pop(ev.pos):
            print('*** POP ***')
            balls.remove(b)
            ballsprites.remove(b)
            break
        if len(balls) == 0:
          return

    for b in balls:
      b.update()

    # draw
    screen.blit(background, (0, 0))
    ballsprites.draw(screen)
    pygame.display.flip()

if __name__ == "__main__":
  main()

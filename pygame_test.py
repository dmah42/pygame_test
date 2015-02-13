import pygame
import sys

from random import randint, uniform

pygame.init()

SIZE = WIDTH, HEIGHT = 640, 400
BG_COLOR = (240, 245, 250)
NUM_BALLS = 10

TIMEREVENT = pygame.USEREVENT

FPS = 60

MAX_SPEED = 5

class Ball:
  def __init__(self, image, x, y, speed):
    self._speed = speed
    self.image = image
    self.pos = image.get_rect().move(x, y)

  def move(self):
    self.pos = self.pos.move(self._speed)
    if self.pos.left < 0 or self.pos.right > WIDTH:
      self._speed[0] = self._speed[0] * -0.9
    if self.pos.top < 0 or self.pos.bottom > HEIGHT:
      self._speed[1] = self._speed[1] * -0.99

    self._speed[1] += 0.1

def main():
  pygame.init()
  pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

  screen = pygame.display.set_mode(SIZE)

  image = pygame.image.load("ball.gif")

  balls = []
  for b in range(NUM_BALLS):
    balls.append(
        Ball(image,
             randint(0, WIDTH),
             randint(0, HEIGHT - image.get_rect().height),
             [uniform(-MAX_SPEED, MAX_SPEED), 0]))

  while True:
    ev = pygame.event.wait()

    if ev.type == TIMEREVENT:
      if len(balls) == 0:
        break

      for b in balls:
        b.move()

      screen.fill(BG_COLOR)

      for b in balls:
        screen.blit(b.image, b.pos)

      pygame.display.flip()
    elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:  # CONSTANT
      for b in balls:
        if ev.pos[0] > b.pos.left and ev.pos[0] < b.pos.right and \
           ev.pos[1] < b.pos.bottom and ev.pos[1] > b.pos.top:
          print "*** POP ***"
          balls.remove(b)
          break
    elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
      break

if __name__ == "__main__":
  main()

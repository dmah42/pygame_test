import sys, pygame

pygame.init()

SIZE = WIDTH, height = 320, 200
BLACK = (0,0,0)

TIMEREVENT = pygame.USEREVENT

FPS = 60

class Ball:
  def __init__(self, image, x, y, speed):
    self._speed = speed
    self.image = image
    self.pos = image.get_rect().move(x, y)

  def move(self):
    self.pos = self.pos.move(self._speed)
    if self.pos.left < 0 or self.pos.right > WIDTH:
      self._speed[0] = self._speed[0] * -0.9
    if self.pos.top < 0 or self.pos.bottom > height:
      self._speed[1] = self._speed[1] * -0.9

    self._speed[1] += 0.1

def main():
  pygame.init()
  pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

  screen = pygame.display.set_mode(SIZE)

  image = pygame.image.load("ball.gif")

  ball = Ball(image, 0, 0, [2, 0])

  while True:
    ev = pygame.event.wait()

    if ev.type == TIMEREVENT:
      ball.move()

      screen.fill(BLACK)
      screen.blit(ball.image, ball.pos)

      pygame.display.flip()
    elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
      break

if __name__ == "__main__":
  main()

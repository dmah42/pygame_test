import sys, pygame

pygame.init()

size = width, height = 320, 200
speed = [2,0]
black = (0,0,0)

TIMEREVENT = pygame.USEREVENT

FPS = 60

def main():
  pygame.init()
  pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

  screen = pygame.display.set_mode(size)

  ball = pygame.image.load("ball.gif")
  ballrect = ball.get_rect()

  while True:
    ev = pygame.event.wait()

    if ev.type == TIMEREVENT:
      ballrect = ballrect.move(speed)
      if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -0.9 * speed[0]
      if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -0.9 * speed[1]

      speed[1] = speed[1] + 0.1

      screen.fill(black)
      screen.blit(ball, ballrect)
      pygame.display.flip()
    elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
      break

if __name__ == "__main__":
  main()

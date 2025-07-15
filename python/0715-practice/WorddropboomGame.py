import pygame

# 초기화
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("PYGAME!")
clock = pygame.time.Clock()

screen.fill((0,0,0))

FONT = pygame.font.SysFont("malgun gothic", 48)
text = FONT.render("Intel", True, (255,255,255))

# TIMER = pygame.USER ,이미지를 컨트롤하는 함수

#img = pygame.image.load("C:\workspace\helldivers2.jpg")
#img = pygame.transform.scale(img, (200, 150))
x = 330
y = 0
#x1 = 250
#y1 = 150

#event handler
while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
#            elif event.key == pygame.K_RIGHT:
#                x1 += 10
#            elif event.key == pygame.K_LEFT:
#                x1 -= 10
#            elif event.key == pygame.K_UP:
#                y1 -= 10
#            elif event.key == pygame.K_DOWN:
#                y1 += 10

    #elif event.key == pygame.K_LEFT

    #screen.blit(text, (330, 0)) #pont를 스크린에 띄우는 함수 -> 위치. 고정시킬 수도 있고 반복문을 통해 움직이게 할 수 있다.

    #update 해서 화면에 출력
    y += 1
    if y > 600:
        y = 0
#    screen.blit(img,(250, 150)) # 이미지를 화면에 위치시키는 함수
  
    screen.blit(text,(x, y)) # 글자를 화면에 위치시키는 함수
    
    pygame.display.update() # 준비된 이미지, 글자를 화면에 띄우는 함수
    

    clock.tick(30) # fps조절할 수 있는 함수 -> operation에서 사용한 시간 측정해서 프레임을 조절하는 함수
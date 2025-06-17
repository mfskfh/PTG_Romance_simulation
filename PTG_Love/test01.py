#-*- 

import pygame


pygame.init()
pygame.font.init()
pygame.mixer.init()

# game_font_L = pygame.font.Font("PTG_Love/source/font/MP_B.ttf", 25)
game_font_B = pygame.font.Font("PTG_Love/source/font/game_font_B.ttf", 40)

# Sound_key = pygame.mixer.Sound("PTG_Love/source/sound/Tennis Hit.wav")

print("민재바보")

def gameText(words, xPos, yPos):
    text = game_font_B.render("", True, (255, 151, 185))

    text_width = text.get_rect().size[0]
    text_height = text.get_rect().size[1]  
    
    for textNo in range(len(words)+1):
        # 딜레이 : $ 다음 5자리 숫자 ㄷ
        if words[textNo-1:textNo] == "$":
            delayTime = words[textNo:textNo+5]
            pygame.time.delay(int(delayTime))
            words = words.replace("$" + delayTime, "", 1)
            continue
    
        text = game_font_B.render(words[0:textNo], True, (255, 151, 185))
        screen.blit(text, (xPos, yPos))
        pygame.display.update()
        # Sound_key.play()
        pygame.time.delay(100)

        if words[0:textNo] == words:
            break

    

class imageload:
    def __init__(self):
        self.x = 0
        self.y = 0
    def put_img(self, address):
        self.img = pygame.image.load(address)
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))
    def get_rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#배경
start_bg = imageload()
start_bg.put_img("PTG_Love/source/image/start_bg2.png")

corridor_bg = imageload()
corridor_bg.put_img("PTG_Love/source/image/bg.png")

market_bg = imageload()
market_bg.put_img("PTG_Love/source/image/start_bg.png")

class_bg = imageload()
class_bg.put_img("PTG_Love/source/image/start_bg.png")

#UI
start_button = imageload()
start_button.put_img("PTG_Love/source/image/button.png")
start_button.change_size(400, 200)
start_button.x = (screen_width / 2) - (start_button.img.get_size()[0] / 2)
start_button.y = 5 * (screen_height / 7)
start_button.get_rect()

text_bar = imageload()
text_bar.put_img("PTG_Love/source/image/text_bar.png")
text_bar.change_size(1550, 300)
text_bar.x = (screen_width-text_bar.img.get_size()[0]) / 2
text_bar.y = screen_height -text_bar.img.get_size()[1] - 25
text_bar.get_rect()
text_init_xPos = 50
text_init_yPos = 500

#초기 실행 코드
start_bg.show()
start_button.show()
# text_bar.show()

gameText("나는 사실.....$01000 왕수오를 좋아해!", 100, 100)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        
    pygame.display.update()

pygame.quit()
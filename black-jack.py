import pygame
import random
import os
import sys

# Pygameの初期化
pygame.init()

# 画面サイズの設定
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ブラックジャック")

# 色の定義
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
LIGHT_GRAY = (211, 211, 211)
RED = (255, 0, 0)

# フォントの設定
FONT = pygame.font.SysFont('arial', 24)
BIG_FONT = pygame.font.SysFont('arial', 36)

# カードのパス
CARD_DIR = 'cards'  # カード画像が保存されているディレクトリ

# カードの定義
suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = (
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'jack', 'queen', 'king', 'ace'
)
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10,
    'king': 10, 'ace': 11
}

# カード画像の読み込み
card_images = {}
for suit in suits:
    for rank in ranks:
        card_name = f"{rank}_of_{suit}"
        path = os.path.join(CARD_DIR, f"{card_name}.png")
        try:
            image = pygame.image.load(path)
            image = pygame.transform.scale(image, (80, 120))
            card_images[card_name] = image
        except:
            # 画像が見つからない場合、Noneを設定
            card_images[card_name] = None

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.image = card_images.get(f"{rank}_of_{suit}")

    def __str__(self):
        return f"{self.rank.capitalize()} of {self.suit.capitalize()}"

class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_button(surface, rect, text, color, hover_color, font):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect.collidepoint(mouse):
        pygame.draw.rect(surface, hover_color, rect)
    else:
        pygame.draw.rect(surface, color, rect)

    pygame.draw.rect(surface, BLACK, rect, 2)  # ボーダー

    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

def main():
    clock = pygame.time.Clock()
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # 最初の2枚を配る
    for _ in range(2):
        player_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

    game_over = False
    player_bust = False
    dealer_bust = False
    result = ""

    # ボタンの設定
    button_width, button_height = 150, 50
    hit_button = pygame.Rect(200, 500, button_width, button_height)
    stand_button = pygame.Rect(400, 500, button_width, button_height)
    new_game_button = pygame.Rect(600, 500, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos

                if not game_over:
                    if hit_button.collidepoint(mouse_pos):
                        # ヒット
                        player_hand.add_card(deck.deal_one())
                        if player_hand.value > 21:
                            player_bust = True
                            game_over = True
                    elif stand_button.collidepoint(mouse_pos):
                        # スタンド
                        # ディーラーのターン
                        while dealer_hand.value < 17:
                            dealer_hand.add_card(deck.deal_one())
                        # 勝敗の判定
                        if dealer_hand.value > 21:
                            dealer_bust = True
                        if dealer_hand.value > player_hand.value and not dealer_bust:
                            result = "ディーラーの勝ちです！"
                        elif dealer_hand.value < player_hand.value and not player_bust:
                            result = "プレイヤーの勝ちです！"
                        elif dealer_hand.value == player_hand.value:
                            result = "引き分けです。"
                        game_over = True
                else:
                    if new_game_button.collidepoint(mouse_pos):
                        # 新しいゲーム
                        deck = Deck()
                        player_hand = Hand()
                        dealer_hand = Hand()
                        for _ in range(2):
                            player_hand.add_card(deck.deal_one())
                            dealer_hand.add_card(deck.deal_one())
                        game_over = False
                        player_bust = False
                        dealer_bust = False
                        result = ""

        # 画面の描画
        screen.fill(GREEN)

        # ディーラーの手札
        draw_text("ディーラーの手:", FONT, WHITE, screen, 50, 50)
        for i, card in enumerate(dealer_hand.cards):
            if i == 0 and not game_over:
                # 最初のカードを裏向きに表示
                pygame.draw.rect(screen, WHITE, (50 + i*90, 80, 80, 120))
                draw_text("裏向き", FONT, BLACK, screen, 50 + i*90 + 10, 80 + 50)
            else:
                if card.image:
                    screen.blit(card.image, (50 + i*90, 80))
                else:
                    pygame.draw.rect(screen, WHITE, (50 + i*90, 80, 80, 120))
                    draw_text(str(card), FONT, BLACK, screen, 50 + i*90 + 5, 80 + 50)
        if game_over:
            draw_text(f"ディーラーの合計: {dealer_hand.value}", FONT, WHITE, screen, 50, 80 + 130)

        # プレイヤーの手札
        draw_text("プレイヤーの手:", FONT, WHITE, screen, 50, 250)
        for i, card in enumerate(player_hand.cards):
            if card.image:
                screen.blit(card.image, (50 + i*90, 280))
            else:
                pygame.draw.rect(screen, WHITE, (50 + i*90, 280, 80, 120))
                draw_text(str(card), FONT, BLACK, screen, 50 + i*90 + 5, 280 + 50)
        draw_text(f"プレイヤーの合計: {player_hand.value}", FONT, WHITE, screen, 50, 280 + 130)

        # 結果の表示
        if game_over:
            if player_bust:
                result = "プレイヤーがバーストしました。ディーラーの勝ちです！"
            elif dealer_bust:
                result = "ディーラーがバーストしました。プレイヤーの勝ちです！"
            draw_text(result, BIG_FONT, WHITE, screen, 50, 450)
        
        # ボタンの描画
        if not game_over:
            # ヒットとスタンドのボタンを表示
            draw_button(screen, hit_button, "ヒット", LIGHT_GRAY, GRAY, FONT)
            draw_button(screen, stand_button, "スタンド", LIGHT_GRAY, GRAY, FONT)
            # 新しいゲームボタンは非表示
        else:
            # 新しいゲームのボタンを表示
            draw_button(screen, new_game_button, "新しいゲーム", LIGHT_GRAY, GRAY, FONT)

        # 結果の表示
        if game_over:
            if player_bust:
                result = "プレイヤーがバーストしました。ディーラーの勝ちです！"
            elif dealer_bust:
                result = "ディーラーがバーストしました。プレイヤーの勝ちです！"
            draw_text(result, BIG_FONT, WHITE, screen, 50, 450)

        pygame.display.flip()
        clock.tick(30)

def draw_button(surface, rect, text, color, hover_color, font):
    mouse = pygame.mouse.get_pos()
    if rect.collidepoint(mouse):
        pygame.draw.rect(surface, hover_color, rect)
    else:
        pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, BLACK, rect, 2)  # ボーダー
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

if __name__ == "__main__":
    main()

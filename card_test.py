"""
2024-10-31
- pygameでプルダウンからトランプの画像を表示させるスクリプト
- デバック用にコードを部分的にコピーしてテストする
- ChatGPTの力を借りて、自分で修正
- トランプの画像をまだ、選択できない。
- スペードのエースを表示させることはできた。

2024-11-06
- リロードして、カード表示を切り替える機能を実装した

"""


import pygame
import os
import random

# Pygameの初期化
pygame.init()

# 画面の設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("カード画像の表示")

# カード画像の読み込み
card_images = {}
suits = ["hearts", "diamonds", "clubs", "spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

# トランプ関数：すべてのカード画像を読み込み
for suit in suits:
    for value in values:
        card_name = f"{value}_of_{suit}.png"
        image_path = os.path.join("png", card_name)  # 画像が格納されているフォルダ
        if os.path.exists(image_path):
            card_images[f"{value}_{suit}"] = pygame.image.load(image_path)

# リロードボタンの設定
button_color = (200, 200, 200)
button_rect = pygame.Rect(650, 500, 120, 50)
button_text = "Reload"

# ランダムカードを選択するフラグ
card_selected = False
selected_card_key = None

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                card_selected = False  # リロードボタンがクリックされたらランダム選択を再開

    # 背景を緑色に設定（テーブルの色）
    screen.fill((0, 128, 0))

    # カードを表示
    if not card_selected and card_images:
        selected_card_key = random.choice(list(card_images.keys()))
        card_selected = True

    if card_selected and selected_card_key:
        card_image = card_images[selected_card_key]
        screen.blit(card_image, (100, 100))  # カード画像を位置 (100, 100) に描画

    # リロードボタンを描画
    pygame.draw.rect(screen, button_color, button_rect)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(button_text, True, (0, 0, 0))
    screen.blit(text_surface, (button_rect.x + 10, button_rect.y + 10))

    # 画面を更新
    pygame.display.flip()

# Pygameの終了処理
pygame.quit()

"""
2024-10-30
pygameでプルダウンからトランプの画像を表示させるスクリプト
何回、修正してもエラーが消えない
根本的な問題の解決が必要
"""


import pygame
import os
import pygame_menu

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

for suit in suits:
    for value in values:
        card_name = f"{value}_of_{suit}.png"
        image_path = os.path.join("png", card_name)  # 画像が格納されているフォルダ
        if os.path.exists(image_path):
            card_images[f"{value}_{suit}"] = pygame.image.load(image_path)

# 画像を表示するための関数
def display_card(image, x, y):
    screen.blit(image, (x, y))

# 選択されたカードを保持する変数
selected_card = None

# メニューの設定
menu = pygame_menu.Menu(title='カードを選択', width=screen_width, height=screen_height, theme=pygame_menu.themes.THEME_GREEN)

def set_card(suit, value):
    global selected_card
    selected_card = f"{value}_{suit}"

# メニューにスートと値の選択肢を追加
for suit in suits:
    for value in values:
        menu.add_button(f"{value} of {suit}", lambda s=suit, v=value: set_card(s, v))

menu.add_button('終了', pygame_menu.events.EXIT)

# メインループ
running = True
while running:
    screen.fill((0, 128, 0))  # 背景を緑色に設定（テーブルの色）

    # メニューを描画
    if menu.is_enabled():
        menu.update(pygame.event.get())
        menu.draw(screen)

    # 選択されたカードを表示
    if selected_card and selected_card in card_images:
        display_card(card_images[selected_card], 100, 100)
    elif selected_card:
        print("指定されたカード画像が見つかりません。")

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 画面の更新
    pygame.display.flip()

# Pygameの終了処理
pygame.quit()

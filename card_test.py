"""
2024-10-31
- pygameでプルダウンからトランプの画像を表示させるスクリプト
- デバック用にコードを部分的にコピーしてテストする
- ChatGPTの力を借りて、自分で修正
- トランプの画像をまだ、選択できない。
- スペードのエースを表示させることはできた。

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

# コード挿入：トランプ関数
for suit in suits:
    for value in values:
        card_name = f"{value}_of_{suit}.png"
        image_path = os.path.join("png", card_name)  # 画像が格納されているフォルダ
        if os.path.exists(image_path):
            card_images[f"{value}_{suit}"] = pygame.image.load(image_path)

#挿入：終わり

"""
ここから先は、ChatGPTの提示したコード
"""
# ウィンドウを開いたままにするためのメインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 128, 0))  # 必要に応じて画面を更新する

#コードを挿入:任意のカード画像を表示（例：スペードのエース）
    card_key = "ace_spades"
    if card_key in card_images:
        card_image = card_images[card_key]
        screen.blit(card_image, (100, 100))  # カード画像を位置 (100, 100) に描画

#挿入：終わり

    pygame.display.flip()  # 画面を更新

pygame.quit()


"""
ここから先は、オリジナル


# メインループ
running = True
while running:
    screen.fill((0, 128, 0))  # 背景を緑色に設定（テーブルの色）

    # 画面の更新
    pygame.display.flip()

# Pygameの終了処理
pygame.quit()

"""
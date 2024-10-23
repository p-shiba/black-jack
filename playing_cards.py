from PIL import Image, ImageDraw, ImageFont
import os

# カードのサイズを設定
card_width, card_height = 250, 350

# スートと数字のリストを作成
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# フォントを設定（システムにインストールされているフォントを使用）
font = ImageFont.truetype("arial.ttf", 36)

# 保存用のディレクトリを作成
if not os.path.exists('cards'):
    os.makedirs('cards')

# 52枚のカードを生成
for suit in suits:
    for rank in ranks:
        # 新しい白いイメージを作成
        img = Image.new('RGB', (card_width, card_height), color='white')
        d = ImageDraw.Draw(img)
        
        # カードの枠を描画
        d.rectangle([10, 10, card_width-10, card_height-10], outline='black')
        
        # スートと数字を描画
        d.text((20, 20), f"{rank}{suit}", font=font, fill='black')
        d.text((card_width-60, card_height-60), f"{rank}{suit}", font=font, fill='black')
        
        # カードを保存
        img.save(f'cards/{rank}{suit}.png')

print("52枚のカード画像が生成されました。")
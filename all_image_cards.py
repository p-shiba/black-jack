from PIL import Image
import os

# ランク（数字や名前）とスート（マーク）のリストを作成
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

# 画像ファイルの保存されているディレクトリ
image_directory = 'png'  # 画像が保存されているフォルダ名を指定

# すべてのカード画像を順に開く
for rank in ranks:
    for suit in suits:
        # ファイル名を組み立てる
        file_name = f'{rank}_of_{suit}.png'
        # 画像パスを組み立てる
        image_path = os.path.join(image_directory, file_name)

        # ファイルが存在するか確認
        if not os.path.exists(image_path):
            print(f"エラー: ファイル '{image_path}' が見つかりません。")
        else:
            try:
                # 画像を開く
                card_image = Image.open(image_path)
                # 画像を表示
                card_image.show()
            except Exception as e:
                print(f"画像を開く際にエラーが発生しました: {e}")

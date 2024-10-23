from PIL import Image
import os

# カードの画像ファイルへのパスを指定
# アップロードされたファイル名を反映
image_path = 'png/2_of_clubs.png'

# ファイルが存在するか確認
if not os.path.exists(image_path):
    print(f"エラー: ファイル '{image_path}' が見つかりません。パスを確認してください。")
else:
    try:
        # 画像を開く
        card_image = Image.open(image_path)
        # 画像を表示
        card_image.show()
    except Exception as e:
        print(f"画像を開く際にエラーが発生しました: {e}")

import os
import cairosvg

# スクリプトのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# SVGとPNGのフォルダパス
svg_dir = os.path.join(script_dir, 'svg-cards')
png_dir = os.path.join(script_dir, 'png-cards')

# PNG保存用のディレクトリを作成
os.makedirs(png_dir, exist_ok=True)

# svg-cardsフォルダ内のすべてのSVGファイルを変換
for filename in os.listdir(svg_dir):
    if filename.endswith('.svg'):
        svg_path = os.path.join(svg_dir, filename)
        png_filename = os.path.splitext(filename)[0] + '.png'
        png_path = os.path.join(png_dir, png_filename)
        # SVGをPNGに変換して保存
        cairosvg.svg2png(url=svg_path, write_to=png_path)
        print(f"変換完了: {png_filename}")

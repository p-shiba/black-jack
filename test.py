"""
2024-11-01更新
- 一部のファイルしかpushできないので、原因を解明

# リモートリポジトリへプッシュする手順

# 1. 変更をステージングエリアに追加する
# 特定のファイルを追加する場合
# git add ファイル名
# 例:
# git add index.html

# すべての変更を追加する場合
# git add .

# 2. 変更をコミットする
# git commit -m "コミットメッセージ"
# 例:
# git commit -m "新しい機能を追加"

# 3. リモートリポジトリにプッシュする
# git push origin ブランチ名
# 例:
# git push origin main

# ローカルリポジトリへプルする手順

# 1. リモートリポジトリの変更を取り込む
# git pull origin ブランチ名
# 例:
# git pull origin main

"""

tax_offices ={"tsu","matsusaka","ise","ueno","owase"}
tax_offices_list = list(tax_offices)


print(tax_offices_list)






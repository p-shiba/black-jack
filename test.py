"""
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

class Dog:
    def __init__(self, name, age):
        self.name = name  # オブジェクトの名前を設定
        self.age = age    # オブジェクトの年齢を設定

    def bark(self):
        print(f"{self.name} says: Woof!")

if __name__ == "__main__":
    # Dogクラスのインスタンスを作成
    my_dog = Dog("ぴりか", 8)
    
    # 属性にアクセスして表示
    print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
    
    # メソッドを呼び出す
    my_dog.bark()
    
    # 別のインスタンスを作成してテスト
    another_dog = Dog("Max", 5)
    print(f"Another dog's name is {another_dog.name} and he is {another_dog.age} years old.")
    another_dog.bark()

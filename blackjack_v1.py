"""
コメントを追加しました。
"""

import random

# カードの定義
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Jack', 'Queen', 'King', 'Ace'
)
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
    'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
    'King': 10, 'Ace': 11
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # エースの数を追跡

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        # エースの値を調整（11または1）
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

def take_bet():
    while True:
        try:
            bet = int(input("賭け金を入力してください: "))
            if bet > 0:
                return bet
            else:
                print("賭け金は正の整数でなければなりません。")
        except ValueError:
            print("有効な数値を入力してください。")

def hit(deck, hand):
    card = deck.deal_one()
    hand.add_card(card)
    print(f"カードを引きました: {card}")

def hit_or_stand(deck, hand):
    while True:
        x = input("ヒットしますか？ (h: ヒット, s: スタンド): ").lower()
        if x == 'h':
            hit(deck, hand)
            return True
        elif x == 's':
            print("スタンドします。")
            return False
        else:
            print("無効な入力です。'h' または 's' を入力してください。")

def show_some(player, dealer):
    print("\nディーラーの手:")
    print(" <カード非表示>")
    print('', dealer.cards[1])
    print("\nプレイヤーの手:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nディーラーの手:", *dealer.cards, sep='\n ')
    print(f"ディーラーの合計値: {dealer.value}")
    print("\nプレイヤーの手:", *player.cards, sep='\n ')
    print(f"プレイヤーの合計値: {player.value}")

def player_busts():
    print("プレイヤーがバーストしました。ディーラーの勝ちです！")

def player_wins():
    print("プレイヤーの勝ちです！")

def dealer_busts():
    print("ディーラーがバーストしました。プレイヤーの勝ちです！")

def dealer_wins():
    print("ディーラーの勝ちです！")

def push():
    print("引き分けです。")

def play_game():
    print("ブラックジャックへようこそ！")

    # デッキの準備
    deck = Deck()
    deck.shuffle()

    # プレイヤーとディーラーのハンドを作成
    player_hand = Hand()
    dealer_hand = Hand()

    # 最初の2枚を配る
    for _ in range(2):
        player_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

    # 賭け金の入力（オプション）
    # bet = take_bet()

    # 最初のカードを表示（ディーラーは1枚隠す）
    show_some(player_hand, dealer_hand)

    playing = True
    while playing:
        # プレイヤーのアクション
        playing = hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        # プレイヤーがバーストした場合
        if player_hand.value > 21:
            player_busts()
            return

    # ディーラーのターン
    show_all(player_hand, dealer_hand)

    while dealer_hand.value < 17:
        hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)

    # ディーラーのバースト
    if dealer_hand.value > 21:
        dealer_busts()
    # 勝敗の判定
    elif dealer_hand.value > player_hand.value:
        dealer_wins()
    elif dealer_hand.value < player_hand.value:
        player_wins()
    else:
        push()

if __name__ == "__main__":
    while True:
        play_game()
        new_game = input("\nもう一度プレイしますか？ (y/n): ").lower()
        if new_game != 'y':
            print("ゲームを終了します。ありがとうございました！")
            break

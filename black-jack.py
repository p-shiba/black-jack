import random
import tkinter as tk
from tkinter import messagebox

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

class BlackjackGUI:
    def __init__(self, master):
        self.master = master
        master.title("ブラックジャック")

        # デッキとハンドの初期化
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand()

        # UIのセットアップ
        self.setup_ui()

        # ゲームの開始
        self.start_game()

    def setup_ui(self):
        # フレームの作成
        self.dealer_frame = tk.LabelFrame(self.master, text="ディーラーの手", padx=10, pady=10)
        self.dealer_frame.pack(padx=10, pady=5)

        self.dealer_cards_label = tk.Label(self.dealer_frame, text="", font=("Helvetica", 12))
        self.dealer_cards_label.pack()

        self.player_frame = tk.LabelFrame(self.master, text="プレイヤーの手", padx=10, pady=10)
        self.player_frame.pack(padx=10, pady=5)

        self.player_cards_label = tk.Label(self.player_frame, text="", font=("Helvetica", 12))
        self.player_cards_label.pack()

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=10)

        self.hit_button = tk.Button(self.buttons_frame, text="ヒット", width=10, command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=5)

        self.stand_button = tk.Button(self.buttons_frame, text="スタンド", width=10, command=self.stand)
        self.stand_button.grid(row=0, column=1, padx=5)

        self.new_game_button = tk.Button(self.master, text="新しいゲーム", width=20, command=self.new_game)
        self.new_game_button.pack(pady=10)
        self.new_game_button.config(state='disabled')

    def start_game(self):
        # プレイヤーとディーラーに2枚ずつカードを配る
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_one())
            self.dealer_hand.add_card(self.deck.deal_one())

        self.update_ui(initial=True)

    def update_ui(self, initial=False):
        # ディーラーのカードを表示（最初は1枚だけ表示）
        if initial:
            dealer_text = f"1. <カード非表示>\n2. {self.dealer_hand.cards[1]}"
        else:
            dealer_text = "\n".join(str(card) for card in self.dealer_hand.cards)
            dealer_text += f"\nディーラーの合計値: {self.dealer_hand.value}"

        self.dealer_cards_label.config(text=dealer_text)

        # プレイヤーのカードを表示
        player_text = "\n".join(str(card) for card in self.player_hand.cards)
        player_text += f"\nプレイヤーの合計値: {self.player_hand.value}"
        self.player_cards_label.config(text=player_text)

    def hit(self):
        self.player_hand.add_card(self.deck.deal_one())
        self.update_ui(initial=True)

        if self.player_hand.value > 21:
            self.end_game(player_bust=True)

    def stand(self):
        self.dealer_turn()

    def dealer_turn(self):
        # ディーラーの手札を全て表示
        self.update_ui(initial=False)

        # ディーラーが17未満ならヒット
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal_one())
            self.update_ui(initial=False)

        # 勝敗の判定
        self.determine_winner()

    def determine_winner(self):
        player_val = self.player_hand.value
        dealer_val = self.dealer_hand.value

        if dealer_val > 21:
            message = "ディーラーがバーストしました。プレイヤーの勝ちです！"
        elif dealer_val > player_val:
            message = "ディーラーの勝ちです！"
        elif dealer_val < player_val:
            message = "プレイヤーの勝ちです！"
        else:
            message = "引き分けです。"

        self.end_game(message=message)

    def end_game(self, player_bust=False, message=None):
        if player_bust:
            message = "プレイヤーがバーストしました。ディーラーの勝ちです！"

        messagebox.showinfo("ゲーム結果", message)

        # ボタンの状態を変更
        self.hit_button.config(state='disabled')
        self.stand_button.config(state='disabled')
        self.new_game_button.config(state='normal')

    def new_game(self):
        # ゲームのリセット
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand()

        self.player_cards_label.config(text="")
        self.dealer_cards_label.config(text="")

        self.hit_button.config(state='normal')
        self.stand_button.config(state='normal')
        self.new_game_button.config(state='disabled')

        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    gui = BlackjackGUI(root)
    root.mainloop()

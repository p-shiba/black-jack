import random
import pygame
import sys

# カードの値の設定
def card_value(card):
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 11
    else:
        return int(card)

# デッキの生成
def create_deck():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = cards * 4
    random.shuffle(deck)
    return deck

# 手札の合計を計算
def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    ace_count = hand.count("A")
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

# ブラックジャックのメイン関数
def blackjack():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blackjack Game")
    font = pygame.font.SysFont("arial", 36)
    clock = pygame.time.Clock()

    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    game_over = False
    player_turn = True
    replay_button = None
    end_button = None

    hit_button = pygame.Rect(150, 450, 200, 50)
    stand_button = pygame.Rect(400, 450, 200, 50)

    def draw_text(text, x, y):
        rendered_text = font.render(text, True, (255, 255, 255))
        screen.blit(rendered_text, (x, y))

    def draw_button(rect, color, text, text_x, text_y):
        pygame.draw.rect(screen, color, rect, border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), rect, 3, border_radius=10)  # Outline
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    while True:
        screen.fill((0, 128, 0))
        draw_text("Your hand: " + " ".join(player_hand) + f" (Total: {hand_value(player_hand)})", 20, 300)
        draw_text("Dealer's visible card: " + dealer_hand[0], 20, 100)

        if not player_turn:
            draw_text("Dealer's hand: " + " ".join(dealer_hand) + f" (Total: {hand_value(dealer_hand)})", 20, 200)

        if game_over:
            if hand_value(player_hand) > 21:
                draw_text("You busted. You lose.", 20, 350)
            elif hand_value(dealer_hand) > 21 or hand_value(player_hand) > hand_value(dealer_hand):
                draw_text("You win!", 20, 350)
            elif hand_value(player_hand) < hand_value(dealer_hand):
                draw_text("You lose.", 20, 350)
            else:
                draw_text("It's a tie.", 20, 350)

            replay_button = pygame.Rect(150, 520, 200, 50)
            end_button = pygame.Rect(400, 520, 200, 50)
            draw_button(replay_button, (0, 255, 0), "Play Again", 175, 530)
            draw_button(end_button, (255, 0, 0), "End Game", 375, 530)

        draw_button(hit_button, (0, 0, 255), "Hit", 175, 460)
        draw_button(stand_button, (255, 165, 0), "Stand", 425, 460)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_turn and not game_over:
                    if hit_button.collidepoint(event.pos):
                        player_hand.append(deck.pop())
                        if hand_value(player_hand) > 21:
                            game_over = True
                            player_turn = False
                    elif stand_button.collidepoint(event.pos):
                        player_turn = False
                elif game_over:
                    if replay_button and replay_button.collidepoint(event.pos):
                        blackjack()  # Restart the game
                    elif end_button and end_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.KEYDOWN:
                if player_turn and not game_over:
                    if event.key == pygame.K_h:  # ヒット
                        player_hand.append(deck.pop())
                        if hand_value(player_hand) > 21:
                            game_over = True
                            player_turn = False
                    elif event.key == pygame.K_s:  # スタンド
                        player_turn = False

        if not player_turn and not game_over:
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            game_over = True

        pygame.display.flip()
        clock.tick(30)

# ゲームの開始
if __name__ == "__main__":
    blackjack()

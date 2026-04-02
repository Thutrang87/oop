import random
class Card:
    RANK_NAMES = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
    SUITS = ['♠','♥','♦','♣']
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        self.__faceUp = False
    def flip(self):
        self.__faceUp = not self.__faceUp
    def getRank(self):
        return self.__rank
    def getSuit(self):
        return self.__suit
    def isFaceUp(self):
        return self.__faceUp
    def compareTo(self, other):
        return self.__rank - other.getRank()
    def __repr__(self):
        if not self.__faceUp:
            return "[??]"
        name = Card.RANK_NAMES.get(self.__rank, str(self.__rank))
        return f"[{name}{self.__suit}]"
class Deck:
    def __init__(self):
        self.__cards = [
        Card(rank, suit) for suit in Card.SUITS for rank in range(2, 15)]
    def shuffle(self):
        random.shuffle(self.__cards)
    def topCard(self):
        return self.__cards[-1] if self.__cards else None
    def dealTo(self, player):
        if self.__cards:
            card = self.__cards.pop()
            player.receiveCard(card)
    def cardsLeft(self):
        return len(self.__cards)
class Hand:
    def __init__(self):
        self.__cards = []
    def addCard(self, card):
        if len(self.__cards) < 2:
            self.__cards.append(card)
    def clear(self):
        self.__cards = []
    @property
    def value(self):
        return sum(card.getRank() for card in self.__cards)
    def compareTo(self, other):
        return self.value - other.value
    def showAll(self):
        for card in self.__cards:
            if not card.isFaceUp():
                card.flip()
    def __repr__(self):
        return " ".join(repr(card) for card in self.__cards)
class Player:
    def __init__(self, name, chips=1000):
        self._name = name
        self._chips = chips
        self._bet = 0
        self._hand = Hand()
        self._isInPlay = True
    def receiveCard(self, card):
        self._hand.addCard(card)
    def bet_amount(self, amount):
        amount = min(amount, self._chips)
        self._chips -= amount
        self._bet += amount
        return amount
    def check(self):
        print(f"{self._name} checks.")
    def call(self, current_bet):
        to_call = current_bet - self._bet
        actual = self.bet_amount(to_call)
        print(f"{self._name} calls {actual} chips.")
    def fold(self):
        self._isInPlay = False
        print(f"{self._name} folds.")
    def raise_(self, amount):
        actual = self.bet_amount(amount)
        print(f"{self._name} raises {actual} chips. (Total bet: {self._bet})")
        return self._bet
    def resetRound(self):
        self._bet = 0
        self._hand.clear()
        self._isInPlay = True
    def makeMove(self, current_bet):
        raise NotImplementedError
    def __repr__(self):
        return f"{self._name} (Chips: {self._chips}"
class HumanPlayer(Player):
    def makeMove(self, current_bet):
        self._hand.showAll()
        print(f"\n {self._name}'s hand: {self._hand} (value: {self._hand.value})")
        print(f" Chips: {self._chips} | Bet: {self._bet} | To call: {current_bet - self._bet}")
        print(" Actions: [c]heck, [a]ll-in, [f]old, [r]aise")
        action = input("Choose action: ").strip().lower()
        if action == 'c':
            self.check()
            return 'check'
        elif action == 'a':
            return self.raise_(self._chips)  # All-in
        elif action == 'f':
            self.fold()
        elif action == 'r':
            amt = int(input(" Raise amount: "))
            return self.raise_(amt)
        return current_bet
class ComputerPlayer(Player):
    def __init__(self, name, chips=1000, difficulty=1):
        super().__init__(name, chips)
        self.__difficulty = difficulty
    def makeMove(self, current_bet):
        hand_val = self._hand.value
        threshold = 10 + self.__difficulty * 3
        if hand_val < threshold -5:
            self.fold()
        elif hand_val > threshold +5:
            raise_amt = 50*self.__difficulty
            return self.raise_(raise_amt)
        else:
            self.call(current_bet)
        return current_bet
class PockerGame:
    def __init__(self, players):
        if not (2 <= len(players) <= 6):
            raise ValueError("Number of players must be between 2 and 6.")
        self.__players = players
        self.__deck = Deck()
        self.__round = 0
        self.__currentPlayer = 0
    def playRound(self):
        self.__round += 1
        print(f"\n{'='*50}")
        print(f" VÁN {self.__round} BẮT ĐẦU ")
        print(f"{'='*50}")
        for player in self.__players:
            player.resetRound()
        self.__deck = Deck()
        self.__deck.shuffle()
        for _ in range(2):
            for player in self.__players:
                self.__deck.dealTo(player)
        print("\n--- Đã chia bài! ---")
        current_bet = 0
        for player in self.__players:
            if player._isInPlay:
                result = player.makeMove(current_bet)
                if result is not None:
                    current_bet = max(current_bet, result)
        active = [p for p in self.__players if p._isInPlay]
        if len(active) == 1:
            winner = active[0]
            print(f"\n{winner._name} thắng ván này vì mọi người khác đã bỏ bài!")
        else:
            print("\n So sánh bài:")
            for player in active:
                player._hand.showAll()
                print(f" {player._name:<15}: {player._hand} (value: {player._hand.value})")
            winner = max(active, key=lambda p: p._hand.value)
            print(f"\n{winner._name} thắng ván này với bài {winner._hand}!")
        pot = sum(p._bet for p in self.__players)
        winner._chips += pot
        print(f" Pot: {pot} chips -> {winner._name}")
        print(f"\n Chip standings:")
        for player in sorted(self.__players, key=lambda x: x._chips, reverse=True):
            print(f" {player._name:<15}: {player._chips} chips")
if __name__ == "__main__":
    players = [
        HumanPlayer("Thu Trang"),
        ComputerPlayer("Alice", difficulty=1),
        ComputerPlayer("Bob",   difficulty=2),
    ]
    game = PockerGame(players)
    for _ in range(3):
        game.playRound()
        print()

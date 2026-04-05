import random


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card):

        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner = random.choice([card1, card2])
        loser = card2 if winner == card1 else card1

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:

        sorted_cards = sorted(self.cards.values(),
                              key=lambda c: c.rating, reverse=True)

        leaderboard = []

        for card in sorted_cards:
            leaderboard.append(
                f"{card.name} - Rating: {card.rating} "
                f"({card.wins}-{card.losses})"
            )

        return leaderboard

    def generate_tournament_report(self) -> dict:

        total_cards = len(self.cards)

        avg_rating = sum(card.rating for card in
                         self.cards.values()) // total_cards

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }

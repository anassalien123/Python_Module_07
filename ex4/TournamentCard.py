from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, card_id, name, cost, rarity, attack, health):
        super().__init__(name, cost, rarity)

        self.card_id = card_id
        self.attack_power = attack
        self.health = health

        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {"card": self.name, "action": "played"}

    def attack(self, target) -> dict:
        return {"attacker": self.name, "target": target,
                "damage": self.attack_power}

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage

        return {"damage_taken": incoming_damage,
                "remaining_health": self.health}

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        self.rating = 1200 + (self.wins) - (self.losses)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {"rating": self.rating, "wins": self.wins,
                "losses": self.losses}

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
        }

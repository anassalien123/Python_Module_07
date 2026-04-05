from typing import Any, Dict

from .Card import Card


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError(
                "Attack and Health must be positive integers"
            )

        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: Any) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> Dict:
        info: Dict = super().get_card_info()
        info.update(
            {
                "attack": self.attack,
                "health": self.health,
            }
        )
        return info

from typing import Dict, List
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack_power
        self.health: int = 10
        self.mana: int = 0

    # Card abstract method
    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters the battlefield"
        }

    # Combatable methods
    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(3, incoming_damage)  # fixed block for demo
        damage_taken = max(0, incoming_damage - blocked)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack_power": self.attack_power,
            "health": self.health
        }

    # Magical methods
    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        mana_used = len(targets)  # demo: 1 mana per target
        self.mana -= mana_used
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            "mana": self.mana
        }

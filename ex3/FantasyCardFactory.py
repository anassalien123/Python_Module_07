from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):

        if name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

        return CreatureCard("Fire Dragon", 5, "Epic", 7, 5)

    def create_spell(self, name_or_power=None):
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(self, name_or_power=None):
        return ArtifactCard("Mana Ring", 2, "Common", "mana")

    def create_themed_deck(self, size: int):

        deck = [
            self.create_creature(),
            self.create_creature("goblin"),
            self.create_spell(),
        ]

        return {"deck": deck[:size]}

    def get_supported_types(self) -> dict:

        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

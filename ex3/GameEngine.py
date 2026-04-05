class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory, strategy) -> None:

        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:

        hand = [
            self.factory.create_creature(),
            self.factory.create_creature("goblin"),
            self.factory.create_spell(),
        ]

        self.cards_created += len(hand)

        battlefield = []

        actions = self.strategy.execute_turn(hand, battlefield)

        self.turns += 1
        self.total_damage += actions["damage_dealt"]

        return {
            "hand": hand,
            "strategy": self.strategy.get_strategy_name(),
            "actions": actions,
        }

    def get_engine_status(self) -> dict:

        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }

from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main():

    print("=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")

    result = engine.simulate_turn()

    hand = result["hand"]

    print("Hand:", [f"{c.name} ({c.cost})" for c in hand])

    print("\nTurn execution:")
    print("Strategy:", result["strategy"])
    print("Actions:", result["actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern:"
          " Maximum flexibility achieved!")


if __name__ == "__main__":
    main()

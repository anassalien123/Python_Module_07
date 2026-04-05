from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main():

    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")

    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary", 7, 5)

    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Rare", 5, 6)

    platform.register_card(dragon)
    platform.register_card(wizard)

    print(f"\n{dragon.name} (ID: {dragon.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", dragon.rating)
    print("- Record: 0-0")

    print(f"\n{wizard.name} (ID: {wizard.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", wizard.rating)
    print("- Record: 0-0")

    print("\nCreating tournament match...")

    result = platform.create_match("dragon_001", "wizard_001")

    print("Match result:", result)

    print("\nTournament Leaderboard:")

    leaderboard = platform.get_leaderboard()

    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry}")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()

    deck.add_card(
        SpellCard("Lightning Bolt", 4, "Common", "Deal 3 damage to target")
    )
    deck.add_card(
        ArtifactCard("Mana Crystal", 3, "Rare", 3, "+1 mana per turn")
    )
    deck.add_card(
        CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    )

    print("Deck stats:", deck.get_deck_stats())
    print("\nDrawing and playing cards:")

    deck.shuffle()

    while True:
        try:
            card = deck.draw_card()
        except ValueError:
            break

        print(
            f"\nDrew: {card.name} "
            f"({card.__class__.__name__.replace('Card','')})"
        )
        result = card.play({})
        print("Play result:", result)

    print(
        "\nPolymorphism in action: Same interface, "
        "different card behaviors!"
    )


if __name__ == "__main__":
    main()

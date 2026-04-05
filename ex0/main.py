from .CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    try:
        card = CreatureCard(
            "Fire Dragon",
            5,
            "Legendary",
            7,
            5
        )

        print("CreatureCard Info:")
        print(card.get_card_info())

        print("\nPlaying Fire Dragon with 6 mana available:")
        playable = card.is_playable(6)
        print("Playable:", playable)

        if playable:
            result = card.play({})
            print("Play result:", result)

        print("\nFire Dragon attacks Goblin Warrior:")
        attack_result = card.attack_target("Goblin Warrior")
        print("Attack result:", attack_result)

        print("\nTesting insufficient mana (3 available):")
        print("Playable:", card.is_playable(3))

        print("\nAbstract pattern successfully demonstrated!")

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

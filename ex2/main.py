from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    elite = EliteCard("Arcane Warrior", 5, "Legendary", 5)

    print("EliteCard capabilities:")
    print(
        "- Card:",
        [
            func
            for func in dir(EliteCard)
            if func in ["play", "get_card_info", "is_playable"]
        ],
    )
    print(
        "- Combatable:",
        [
            func
            for func in dir(EliteCard)
            if func in ["attack", "defend", "get_combat_stats"]
        ],
    )
    print(
        "- Magical:",
        [
            func
            for func in dir(EliteCard)
            if func in ["cast_spell", "channel_mana", "get_magic_stats"]
        ],
    )

    print("\nPlaying Arcane Warrior (Elite Card):")
    print("\nCombat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(5))
    print("\nMagic phase:")
    print(
        "Spell cast:",
        elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]),
    )
    print("Mana channel:", elite.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()

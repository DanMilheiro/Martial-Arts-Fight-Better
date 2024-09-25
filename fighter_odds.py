def calculate_odds(fighter1_stats, fighter2_stats):
    odds1 = fighter1_stats['strength'] * 0.5 + fighter1_stats['stamina'] * 0.5
    odds2 = fighter2_stats['strength'] * 0.5 + fighter2_stats['stamina'] * 0.5
    return odds1, odds2

fighter1 = {'strength': 85, 'stamina': 90}
fighter2 = {'strength': 80, 'stamina': 85}

odds = calculate_odds(fighter1, fighter2)
print(f"Odds: Fighter 1: {odds[0]}, Fighter 2: {odds[1]}")

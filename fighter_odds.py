def calculate_odds(fighter1, fighter2):
    # Strength is calculated dynamically based on height and weight
    fighter1_strength = calculate_strength(fighter1.height, fighter1.weight)
    fighter2_strength = calculate_strength(fighter2.height, fighter2.weight)
    
    # Weighted scores for all attributes, including stamina and strength
    f1_score = (
        fighter1.grappling * 0.15 + 
        fighter1.striking * 0.2 + 
        fighter1.submission * 0.2 + 
        fighter1.stamina * 0.15 + 
        fighter1_strength * 0.2 + 
        fighter1.recent_activity * 0.1
    )
    
    f2_score = (
        fighter2.grappling * 0.15 + 
        fighter2.striking * 0.2 + 
        fighter2.submission * 0.2 + 
        fighter2.stamina * 0.15 + 
        fighter2_strength * 0.2 + 
        fighter2.recent_activity * 0.1
    )
    
    total = f1_score + f2_score
    
    f1_odds = (f1_score / total) * 100
    f2_odds = (f2_score / total) * 100
    
    return f1_odds, f2_odds

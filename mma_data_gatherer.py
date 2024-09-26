import requests
import json

# Base URL for the MMA Stats API
BASE_URL = 'https://rapidapi.com/chirikutsikuda/api/mma-stats'  # Use the correct base URL

def fetch_fighter_data(name):
    """Fetch data for a fighter by name."""
    url = f"{BASE_URL}/search?name={name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {name}: {response.json().get('error', 'Unknown error')}")
        return None

def fetch_fights_by_date(date):
    """Fetch fight details for a specific date."""
    url = f"{BASE_URL}/{date}"  # Adjusted URL format
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching fights for {date}: {response.json().get('error', 'Unknown error')}")
        return None

def save_to_json(data, filename):
    """Save data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    # Example usage
    fighter_name = "Themba Gorimbo"  # Replace with the fighter name you want to search
    fighter_data = fetch_fighter_data(fighter_name)
    
    if fighter_data:
        save_to_json(fighter_data, 'fighter_data.json')
    
    fight_date = "April_08_2023"  # Replace with the desired date
    fights_data = fetch_fights_by_date(fight_date)
    
    if fights_data:
        save_to_json(fights_data, 'fights_data.json')

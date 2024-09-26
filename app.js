// Fetch fighters from the API and populate the dropdowns
const apiKey = '4d67809696mshf8762356cd063b1p1e205bjsn641077296062'; // Your API key
const url = 'https://chirikutsikuda-mma-stats.p.rapidapi.com/fighters'; // Adjust if necessary

// Function to load fighters into the dropdowns
function loadFighters() {
    fetch(url, {
        method: 'GET',
        headers: {
            'x-rapidapi-host': 'chirikutsikuda-mma-stats.p.rapidapi.com',
            'x-rapidapi-key': apiKey,
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Populate fighter1 and fighter2 dropdowns
        const fighter1Dropdown = document.getElementById('fighter1');
        const fighter2Dropdown = document.getElementById('fighter2');

        data.forEach(fighter => {
            const option1 = document.createElement('option');
            option1.value = fighter.id; // Use the correct property for fighter ID
            option1.textContent = fighter.name; // Use the correct property for fighter name
            fighter1Dropdown.appendChild(option1);

            const option2 = document.createElement('option');
            option2.value = fighter.id; // Use the correct property for fighter ID
            option2.textContent = fighter.name; // Use the correct property for fighter name
            fighter2Dropdown.appendChild(option2);
        });
    })
    .catch(error => console.error('Error fetching fighters:', error));
}

// Call loadFighters on page load
window.onload = loadFighters;

// Existing fight button event listener
document.getElementById('fightButton').addEventListener('click', function() {
    const fighter1 = document.getElementById('fighter1').value;
    const fighter2 = document.getElementById('fighter2').value;

    // Assuming you have an API to calculate odds (based on fighter_odds.py)
    fetch(`/calculate-odds?fighter1=${fighter1}&fighter2=${fighter2}`)
        .then(response => response.json())
        .then(data => {
            // Display result
            document.getElementById('result').innerText = `Fighter 1 has ${data.fighter1_odds}% chance of winn

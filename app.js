// Fetch fighters from the API and populate the dropdowns
const apiKey = '4d67809696mshf8762356cd063b1p1e205bjsn641077296062'; // Your API key

// Function to load fighters based on a search term
function loadFighters(searchTerm = '') { // Default to empty string if no term is provided
    const url = `https://mma-stats.p.rapidapi.com/search?name=${searchTerm}`;

    fetch(url, {
        method: 'GET',
        headers: {
            "x-rapidapi-host": "mma-stats.p.rapidapi.com",
            "x-rapidapi-key": apiKey
        }
    })
    .then(response => response.json())
    .then(data => {
        // Check if data contains fighters
        if (data && data.fighters) {
            const fighter1Select = document.getElementById('fighter1');
            const fighter2Select = document.getElementById('fighter2');
            
            // Clear existing options
            fighter1Select.innerHTML = '';
            fighter2Select.innerHTML = '';

            // Populate the dropdowns
            data.fighters.forEach(fighter => {
                const option = document.createElement('option');
                option.value = fighter.id; // or use a unique identifier for each fighter
                option.textContent = fighter.name; // Adjust based on the actual data structure

                fighter1Select.appendChild(option.cloneNode(true)); // Append option for Fighter 1
                fighter2Select.appendChild(option); // Append same option for Fighter 2
            });
        } else {
            console.error('No fighters found');
        }
    })
    .catch(error => console.error('Error fetching fighters:', error));
}

// Call loadFighters when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    loadFighters(); // Call with empty string to load fighters on page load
});

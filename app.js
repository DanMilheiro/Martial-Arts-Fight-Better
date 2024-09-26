// Fetch fighters based on a search term and populate the dropdowns
function fetchFighters(searchTerm = '') {
    const apiKey = '4d67809696mshf8762356cd063b1p1e205bjsn641077296062'; // Your API key
    const url = `https://mma-stats.p.rapidapi.com/search?q=${searchTerm}`;

    const headers = {
        "x-rapidapi-host": "mma-stats.p.rapidapi.com",
        "x-rapidapi-key": apiKey
    };

    fetch(url, { headers })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const fighters = data.results; // Adjust based on the actual structure of the response
            const fighter1Select = document.getElementById('fighter1');
            const fighter2Select = document.getElementById('fighter2');

            // Clear existing options
            fighter1Select.innerHTML = '';
            fighter2Select.innerHTML = '';

            // Populate the dropdowns with fighter names
            fighters.forEach(fighter => {
                const option1 = document.createElement('option');
                option1.value = fighter.name; // Assuming the fighter object has a 'name' property
                option1.textContent = fighter.name;
                fighter1Select.appendChild(option1);

                const option2 = document.createElement('option');
                option2.value = fighter.name; // Assuming the fighter object has a 'name' property
                option2.textContent = fighter.name;
                fighter2Select.appendChild(option2);
            });

            // Refresh Select2 dropdown
            $('.fighter-select').select2(); // Re-initialize Select2 to reflect new options
        })
        .catch(error => console.error('Error:', error));
}

// Call the function with an empty search term to initially populate the dropdown
fetchFighters();

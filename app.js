// Fetch fighter data from the API and populate the dropdowns
fetch('/api/fighters')
    .then(response => response.json())
    .then(fighters => {
        const fighter1Dropdown = document.getElementById('fighter1');
        const fighter2Dropdown = document.getElementById('fighter2');

        fighters.forEach(fighter => {
            const option1 = document.createElement('option');
            option1.value = fighter.id; // Use the unique ID or other identifier
            option1.textContent = fighter.nickname; // Change this to your preferred property

            const option2 = document.createElement('option');
            option2.value = fighter.id; // Same ID for the second dropdown
            option2.textContent = fighter.nickname; // Same name for the second dropdown

            fighter1Dropdown.appendChild(option1);
            fighter2Dropdown.appendChild(option2);
        });

        // Re-initialize Select2 after adding options
        $('.fighter-select').select2({
            placeholder: 'Select a Fighter',
            allowClear: true
        });
    })
    .catch(error => {
        console.error('Error fetching fighters:', error);
    });

document.getElementById('fightButton').addEventListener('click', function() {
    const fighter1 = document.getElementById('fighter1').value;
    const fighter2 = document.getElementById('fighter2').value;

    // Assuming you have an API to calculate odds (based on fighter_odds.py)
    fetch(`/calculate-odds?fighter1=${fighter1}&fighter2=${fighter2}`)
        .then(response => response.json())
        .then(data => {
            // Display result
            document.getElementById('result').innerText = `Fighter 1 has ${data.fighter1_odds}% chance of winning, Fighter 2 has ${data.fighter2_odds}%`;

            // Update probability chart (using Chart.js)
            const ctx = document.getElementById('probabilityChart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Fighter 1', 'Fighter 2'],
                    datasets: [{
                        data: [data.fighter1_odds, data.fighter2_odds],
                        backgroundColor: ['#36A2EB', '#FF6384']
                    }]
                }
            });

            // Show Fighter Details (this assumes the API sends more detailed info)
            document.getElementById('fighter1Details').innerText = `Strength: ${data.fighter1_strength}, Stamina: ${data.fighter1_stamina}`;
            document.getElementById('fighter2Details').innerText = `Strength: ${data.fighter2_strength}, Stamina: ${data.fighter2_stamina}`;
        })
        .catch(error => console.error('Error:', error));
});

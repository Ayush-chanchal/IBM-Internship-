document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Gathering form data
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Sending data to the Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // Displaying result
        document.getElementById('result').innerHTML = `
            <p><strong>Prediction:</strong> ${result.prediction}</p>
            <p><strong>Suggestion:</strong> ${result.suggestion}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

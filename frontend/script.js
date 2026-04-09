// frontend/script.js

// Handle API interactions and UI updates 

// Example function to fetch data from an API
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Example function to update UI
function updateUI(data) {
    const output = document.getElementById('output');
    output.innerHTML = JSON.stringify(data, null, 2);
}

// Example usage
// fetchData('https://api.example.com/data').then(updateUI);
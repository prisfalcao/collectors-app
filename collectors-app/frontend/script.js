const API_BASE_URL = 'http://localhost:8000';

document.getElementById('add-game-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const newGame = {
        name: document.getElementById('name').value,
        platform: document.getElementById('platform').value,
        release_year: document.getElementById('release_year').value,
        developer: document.getElementById('developer').value,
        condition: document.getElementById('condition').value
    };
    try {
        await fetch(`${API_BASE_URL}/add_game`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newGame)
        });
        fetchGames();
    } catch (error) {
        console.error('Error adding the game: ', error);
    }
});

async function fetchGames() {
    try {
        const response = await fetch(`${API_BASE_URL}/games`);
        const games = await response.json();

        const gameList = document.getElementById('game-list');
        gameList.innerHTML = '';

        games.forEach((game) => {
            const gameItem = document.createElement('li');
            const gameInfo = document.createElement('div');
            gameInfo.innerHTML = `<strong>${game.name}</strong> For: ${game.platform} - released in ${game.release_year} <br>
                                   Developed by: ${game.developer} <br>
                                   Condition of the item: ${game.condition}`;

            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.onclick = () => removeGame(game.id);

            gameItem.appendChild(gameInfo);
            gameItem.appendChild(removeButton);
            gameList.appendChild(gameItem);
        });
    } catch (error) {
        console.error('Error fetching the game list:', error);
    }
}

async function removeGame(gameId) {
    try {
        await fetch(`${API_BASE_URL}/remove/${gameId}`, {method: 'DELETE'});
        fetchGames();
    } catch (error) {
        console.error('Error removing game:', error);
    }
}

document.addEventListener("DOMContentLoaded", fetchGames);
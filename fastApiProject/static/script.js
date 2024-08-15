const baseUrl = "http://127.0.0.1:8000";

// Fetch all teams
document.getElementById('getTeams').addEventListener('click', () => {
    fetch(`${baseUrl}/teams`)
        .then(response => response.json())
        .then(data => {
            const teamList = document.getElementById('teamList');
            teamList.innerHTML = "";
            data.forEach(team => {
                const li = document.createElement('li');
                li.textContent = `${team.name} - ${team.city}`;
                teamList.appendChild(li);
            });
        });
});

// Fetch team by ID
document.getElementById('getTeamById').addEventListener('click', () => {
    const teamId = document.getElementById('teamId').value;
    fetch(`${baseUrl}/teams/${teamId}`)
        .then(response => response.json())
        .then(data => {
            const teamDetail = document.getElementById('teamDetail');
            teamDetail.innerHTML = `Name: ${data.name}, City: ${data.city}`;
        })
        .catch(() => {
            document.getElementById('teamDetail').innerText = "Team not found";
        });
});

// Create a new team
document.getElementById('createTeam').addEventListener('click', () => {
    const teamName = document.getElementById('teamName').value;
    const teamCity = document.getElementById('teamCity').value;

    fetch(`${baseUrl}/teams`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: teamName, city: teamCity })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('createResponse').innerText = `Created team: ${data.name} in ${data.city}`;
    })
    .catch(() => {
        document.getElementById('createResponse').innerText = "Failed to create team";
    });
});

// Fetch teams by city
document.getElementById('getTeamsByCity').addEventListener('click', () => {
    const cityName = document.getElementById('cityName').value;
    fetch(`${baseUrl}/teams/by_city/?city=${cityName}`)
        .then(response => response.json())
        .then(data => {
            const cityTeamList = document.getElementById('cityTeamList');
            cityTeamList.innerHTML = "";
            if (data.length > 0) {
                data.forEach(team => {
                    const li = document.createElement('li');
                    li.textContent = `${team.name} - ${team.city}`;
                    cityTeamList.appendChild(li);
                });
            } else {
                cityTeamList.innerHTML = "No teams found in the specified city";
            }
        })
        .catch(() => {
            document.getElementById('cityTeamList').innerText = "Error fetching teams by city";
        });
});

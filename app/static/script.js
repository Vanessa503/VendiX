fetch("/users/")
    .then(response => response.json())
    .then(data => {
        document.getElementById("data").innerText = JSON.stringify(data, null, 2);
    });

fetch("/dashboard-data/")
    .then(response => response.json())
    .then(data => {
        document.getElementById("total-users").innerText = data.total_users;
        document.getElementById("total-purchases").innerText = data.total_purchases;
        document.getElementById("total-reviews").innerText = data.total_reviews;
        document.getElementById("avg-rating").innerText = data.avg_rating;
    })
    .catch(error => {
        console.error("Erro ao carregar os dados do dashboard:", error);
    });

async function loadProducts() {

    const response =
        await fetch("http://localhost:8002/products");

    const data =
        await response.json();

    document.getElementById("products").innerHTML =
        JSON.stringify(data, null, 2);
}


async function loadUsers() {

    const response =
        await fetch("http://localhost:8003/users");

    const data =
        await response.json();

    document.getElementById("users").innerHTML =
        JSON.stringify(data, null, 2);
}

async function searchProducts() {

    const q =
        document.getElementById("searchInput").value;

    const response =
        await fetch(
            `http://localhost:8004/search?q=${q}`
        );

    const data =
        await response.json();

    document.getElementById("searchResult").innerHTML =
        JSON.stringify(data, null, 2);
}
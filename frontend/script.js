async function counterAPI() {
    const api = await fetch("https://fnrr9hhx7a.execute-api.ap-southeast-1.amazonaws.com/count");
    const data = await api.json();
    document.getElementById("counterr").textContent = data.count;
}

counterAPI();
async function counterAPI() {
    const api = await fetch("https://d1q5ag8e6d.execute-api.ap-southeast-1.amazonaws.com/count");
    const data = await api.json();
    document.getElementById("counterr").textContent = data.count;
}

counterAPI();
async function organizar() {
    const tareas = document.getElementById("tareas").value;

    const response = await fetch('/organizar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ tareas })
    });

    const data = await response.json();

    document.getElementById("resultado").textContent = data.resultado || data.error;
}
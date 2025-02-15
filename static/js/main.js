document.getElementById("submit_button").addEventListener('click', () => {
    fetch('/query')
    .then(response => response.json())
    .then(data => {
        // Ensure the main element exists
        let main = document.querySelector("main");
        if (!main) {
            main = document.createElement("main");
            document.body.appendChild(main);
        }

        // Clear previous content
        main.innerHTML = "";

        // Display the fetched data
        data.forEach(item => {
            let output = document.createElement("p");
            output.textContent = `Title: ${item.TITLE}, Description: ${item.DESCRIPTION}, URL: ${item.URL}`;
            main.appendChild(output);
        });
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
});

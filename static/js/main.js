document.querySelector("#submit_button").addEventListener('click', () => {
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
            /*
            let output = document.createElement("p");
            output.textContent = `Title: ${item.title}, Description: ${item.description}, URL: ${item.url}`;
            main.appendChild(output);
            */
            
            // create display card
            let card = document.createElement("div");
            card.setAttribute("class","course-display-card");

            // Course Title
            let courseTitle = document.createElement("h2");
            courseTitle.setAttribute("class", "card-title");
            courseTitle.textContent= `${item.title}`;

            // Faculty here
            let courseDesc = document.createElement("h4");
            courseDesc.setAttribute("class", "card-desc");
            courseDesc.textContent= `${item.description}`;

            // Description here
            let courseURL = document.createElement("p");
            courseURL.setAttribute("class", "card-url");
            courseURL.textContent= `${item.url}`;


            card.appendChild(courseTitle);
            card.appendChild(courseDesc); 
            card.appendChild(courseURL);  
            main.appendChild(card);
        });
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
});

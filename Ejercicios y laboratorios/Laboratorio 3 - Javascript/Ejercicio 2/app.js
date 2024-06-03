
document.addEventListener("DOMContentLoaded", function () {
    const tableBody = document.querySelector("#pokemonTable tbody");

    // Fetch data from the API
    fetch("https://pokeapi.co/api/v2/pokemon/")
      .then((response) => response.json())
      .then((data) => {
        // Iterate over each Pokemon
        data.results.forEach((pokemon) => {
          const row = document.createElement("tr");
          const nameCell = document.createElement("td");
          const linkCell = document.createElement("td");
          const link = document.createElement("a");

          nameCell.textContent = pokemon.name;
          link.textContent = "Detalles";
          link.href = `https://pokeapi.co/api/v2/pokemon/`;

          linkCell.appendChild(link);
          row.appendChild(nameCell);
          row.appendChild(linkCell);
          tableBody.appendChild(row);
        });
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  });

  
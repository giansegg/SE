document
  .getElementById("distanceForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const city1 = document.getElementById("city1").value;
    const country1 = document.getElementById("country1").value;
    const city2 = document.getElementById("city2").value;
    const country2 = document.getElementById("country2").value;

    const option = document.getElementById("option").value;

    fetch(
      `http://127.0.0.1:5000/data?city1=${city1}&country1=${country1}&city2=${city2}&country2=${country2}&option=${option}`
    )
      .then((response) => {
        if (!response.ok) {
          throw new Error("Error en la solicitud");
        }
        return response.json();
      })
      .then((data) => {
        document.getElementById(
          "result"
        ).innerText = `La distancia entre ${city1}, ${country1} y ${city2}, ${country2} es: ${data.distance} km`;
      })
      .catch((error) => {
        document.getElementById("result").innerText = `Error: ${error.message}`;
      });
  });

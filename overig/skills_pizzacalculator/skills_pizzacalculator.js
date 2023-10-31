// Wacht tot de DOM volledig is geladen voordat de code wordt uitgevoerd
document.addEventListener("DOMContentLoaded", function () {
    // Haal referenties op naar verschillende HTML-elementen
    const pizzaForm = document.getElementById("pizza-form");
    const calculateButton = document.getElementById("calculate-button");
    const orderSummary = document.getElementById("order-summary");
    const orderList = document.getElementById("order-list");
    const totalPrice = document.getElementById("total-price");
    const currentYear = document.getElementById("current-year");

    // Definieer de prijzen van pizzamaten in een object
    const pizzaPrices = {
        small: 5,
        medium: 7,
        large: 10
    };

    // Voeg een klikgebeurtenisluisteraar toe aan de knop voor berekening
    calculateButton.addEventListener("click", function () {
        // Initialiseer een leeg object om de bestelling bij te houden
        const order = {};
        // Initialiseer een variabele om het totaalbedrag bij te houden
        let total = 0;

        // Loop door de pizzaprijzen en controleer de geselecteerde hoeveelheden
        for (const size in pizzaPrices) {
            // Haal de geselecteerde hoeveelheid op uit de bijbehorende invoervelden
            const quantity = parseInt(document.getElementById(size + "-pizza").value);
            // Als er minstens één pizza van deze maat is besteld, voeg deze toe aan de bestelling en bereken de totaalprijs
            if (quantity > 0) {
                order[size] = quantity;
                total += quantity * pizzaPrices[size];
            }
        }

        // Als er iets is besteld (totale prijs groter dan 0), toon het besteloverzicht
        if (total > 0) {
            orderSummary.style.display = "block";
            // Vul de lijst met de bestelling en geef de totale prijs weer
            orderList.innerHTML = Object.entries(order)
                .map(([size, quantity]) => `<li>${quantity} ${size} Pizza</li>`)
                .join("");
            totalPrice.textContent = `Totaalprijs: €${total}`;
        }
    });

    // Geef het huidige jaar weer in het corresponderende HTML-element
    currentYear.textContent = new Date().getFullYear();
});

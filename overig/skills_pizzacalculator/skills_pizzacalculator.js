document.addEventListener("DOMContentLoaded", function () {
    const pizzaForm = document.getElementById("pizza-form");
    const calculateButton = document.getElementById("calculate-button");
    const orderSummary = document.getElementById("order-summary");
    const orderList = document.getElementById("order-list");
    const totalPrice = document.getElementById("total-price");
    const currentYear = document.getElementById("current-year");

    const pizzaPrices = {
        small: 5,
        medium: 7,
        large: 10
    };

    calculateButton.addEventListener("click", function () {
        const order = {};
        let total = 0;

        for (const size in pizzaPrices) {
            const quantity = parseInt(document.getElementById(size + "-pizza").value);
            if (quantity > 0) {
                order[size] = quantity;
                total += quantity * pizzaPrices[size];
            }
        }

        if (total > 0) {
            orderSummary.style.display = "block";
            orderList.innerHTML = Object.entries(order)
                .map(([size, quantity]) => `<li>${quantity} ${size} Pizza</li>`)
                .join("");
            totalPrice.textContent = `Totaalprijs: €${total}`;
        }
    });

    currentYear.textContent = new Date().getFullYear();
});
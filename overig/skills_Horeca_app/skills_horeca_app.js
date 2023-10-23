const order = {
    drinks: {},
    snacks: {},
};



function addDrinkToOrder() {
    const drink = document.getElementById('drink').value;
    const quantity = parseInt(document.getElementById('drink-quantity').value);

    if (order.drinks[drink]) {
        order.drinks[drink] += quantity;
    } else {
        order.drinks[drink] = quantity;
    }
}

function addSnackToOrder() {
    const snack = document.getElementById('snack').value;
    const quantity = parseInt(document.getElementById('snack-quantity').value);

    if (order.snacks[snack]) {
        order.snacks[snack] += quantity;
    } else {
        order.snacks[snack] = quantity;
    }
}

function showBill() {
    const billDiv = document.getElementById('bill');
    billDiv.style.display = 'block';
    billDiv.innerHTML = '<h2>Uw Rekening</h2>';

    // Toon drankjes
    if (Object.keys(order.drinks).length > 0) {
        billDiv.innerHTML += '<h3>Drankjes:</h3>';
        for (const drink in order.drinks) {
            const quantity = order.drinks[drink];
            const price = calculateDrinkPrice(drink);
            billDiv.innerHTML += `${drink}: ${quantity} x €${price} = €${quantity * price}<br>`;
        }
    }

    // Toon snacks
    if (Object.keys(order.snacks).length > 0) {
        billDiv.innerHTML += '<h3>Snacks:</h3>';
        for (const snack in order.snacks) {
            const quantity = order.snacks[snack];
            const price = calculateSnackPrice(snack);
            billDiv.innerHTML += `${snack}: ${quantity} x €${price} = €${quantity * price}<br>`;
        }
    }

    // Totaalprijs
    const total = calculateTotalPrice();
    billDiv.innerHTML += `<h3>Totaal: €${total}</h3>`;
}

function calculateDrinkPrice(drink) {
    // Voeg hier je prijzen voor drankjes toe
    const prices = {
        fris: 2.50,
        bier: 3.00,
        wijn: 4.00,
    };
    return prices[drink] || 0;
}

function calculateSnackPrice(snack) {
    // Voeg hier je prijzen voor snacks toe
    const prices = {
        frikandel: 2.00,
        bitterballen: 5.00,
        pizza: 7.00,
    };
    return prices[snack] || 0;
}

function calculateTotalPrice() {
    let total = 0;

    for (const drink in order.drinks) {
        total += order.drinks[drink] * calculateDrinkPrice(drink);
    }

    for (const snack in order.snacks) {
        total += order.snacks[snack] * calculateSnackPrice(snack);
    }

    return total;
}

// Toon het juiste bestelformulier op basis van de geselecteerde bestellingstype
document.getElementById('order-type').addEventListener('change', function() {
    const drinkOrderDiv = document.getElementById('drink-order');
    const snackOrderDiv = document.getElementById('snack-order');
    const orderType = this.value;

    if (orderType === 'drank') {
        drinkOrderDiv.style.display = 'block';
        snackOrderDiv.style.display = 'none';
    } else if (orderType === 'snack') {
        drinkOrderDiv.style.display = 'none';
        snackOrderDiv.style.display = 'block';
    }
});

function addSnackToOrder() {
    const snack = document.getElementById('snack').value;
    const quantity = parseInt(document.getElementById('snack-quantity').value);

    if (snack === 'bitterballen' && ![8, 16].includes(quantity)) {
        alert('U kunt alleen een keuze maken tussen 8 en 16. De snacks zijn niet toegevoegd aan de bestelling.');
        return;
    }

    if (snack === 'pizza' && (quantity < 1 || quantity > 12)) {
        alert('U kunt alleen tussen 1 en 12 slices pizza bestellen. De pizza is niet toegevoegd aan de bestelling.');
        return;
    }

    if (order.snacks[snack]) {
        order.snacks[snack] += quantity;
    } else {
        order.snacks[snack] = quantity;
    }
}




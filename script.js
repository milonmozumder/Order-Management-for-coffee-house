// Menu items with prices
const menu = {
  "Pizza": 40,
  "Pasta": 50,
  "Burger": 80,
  "Coffee": 55,
};

let orderTotal = 0; // To track the total amount
const orderedItems = []; // To store ordered items

// Select necessary elements
const addItemButton = document.getElementById("add-item");
const itemNameInput = document.getElementById("item-name");
const billTableBody = document.querySelector("#bill-table tbody");
const totalAmountElement = document.getElementById("total-amount");

// Add event listener for the "Add Item" button
addItemButton.addEventListener("click", () => {
  const itemName = itemNameInput.value.trim().toLowerCase(); // Get user input
  const formattedItemName = itemName.charAt(0).toUpperCase() + itemName.slice(1); // Capitalize first letter

  // Check if the item exists in the menu
  if (menu[formattedItemName]) {
    // Add the item to the order
    orderedItems.push({ name: formattedItemName, price: menu[formattedItemName] });
    orderTotal += menu[formattedItemName];

    // Update the bill receipt
    const row = document.createElement("tr");
    row.innerHTML = `<td>${formattedItemName}</td><td>tk${menu[formattedItemName]}</td>`;
    billTableBody.appendChild(row);

    // Update total amount
    totalAmountElement.textContent = `tk${orderTotal}`;

    // Clear input field
    itemNameInput.value = "";
  } else {
    // Show an alert if the item is not available
    alert(`Sorry, the item '${itemNameInput.value}' is not available in the menu.`);
  }
});

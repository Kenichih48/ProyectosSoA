import { ROOT } from './variables.js'

let currentHighlightedMenu = null;

function highlightMenu(item, index) {
  if (currentHighlightedMenu && currentHighlightedMenu.id === index) {
    removeHighlight(currentHighlightedMenu);
    return;
  }

  if (currentHighlightedMenu) {
    removeHighlight(currentHighlightedMenu);
  }

  const dish = document.getElementById(`dish-${index}`);
  const drink = document.getElementById(`drink-${index}`);
  const dessert = document.getElementById(`dessert-${index}`);

  dish.classList.add('highlight');
  drink.classList.add('highlight');
  dessert.classList.add('highlight');

  currentHighlightedMenu = { id: index, dish, drink, dessert };
}

function removeHighlight(highlightedMenu) {
  highlightedMenu.dish.classList.remove('highlight');
  highlightedMenu.drink.classList.remove('highlight');
  highlightedMenu.dessert.classList.remove('highlight');
  currentHighlightedMenu = null;
}

// Función para renderizar el menú en la página
function renderMenu(menu) {
  const dishContainer = document.getElementById('dish-container');
  const drinkContainer = document.getElementById('drink-container');
  const dessertContainer = document.getElementById('dessert-container');

  if (menu.length === 0) {
    dishContainer.innerHTML = '<p>No hay elementos en el menú.</p>';
    return;
  }

  menu.forEach((item, index) => {
    const menuDish = document.createElement('div');
    menuDish.classList.add('menu-item');
    menuDish.id = `dish-${index}`;
    menuDish.addEventListener('click', () => highlightMenu(item, index));

    const menuDrink = document.createElement('div');
    menuDrink.classList.add('menu-item');
    menuDrink.id = `drink-${index}`;
    menuDrink.addEventListener('click', () => highlightMenu(item, index));

    const menuDessert = document.createElement('div');
    menuDessert.classList.add('menu-item');
    menuDessert.id = `dessert-${index}`;
    menuDessert.addEventListener('click', () => highlightMenu(item, index));

    const dishName = document.createElement('h3');
    dishName.textContent = item.dish;

    const drinkName = document.createElement('h3');
    drinkName.textContent = item.drink;

    const dessertName = document.createElement('h3');
    dessertName.textContent = item.dessert;

    menuDish.appendChild(dishName);
    menuDrink.appendChild(drinkName);
    menuDessert.appendChild(dessertName);

    dishContainer.appendChild(menuDish);
    drinkContainer.appendChild(menuDrink);
    dessertContainer.appendChild(menuDessert);
  });
}

// Función principal
async function main() {
  //const menu = await fetchMenu();
  try {
    // Generar la URL con los parámetros
    const url = new URL(`${ROOT}/GetMenu`);

    // Realizar la solicitud GET al Backend Cloud Function
    const response = await fetch(url, {
      method: 'GET'
    });

    if (response.ok) {
      const menuData = await response.json();
      if (menuData.status_code === 200) {
        const menuItems = menuData.data;
        renderMenu(menuItems);
      }
    }

  } catch (error) {
    console.error('Error al obtener el menú:', error);
    return [];
  }
  
  
}

main();
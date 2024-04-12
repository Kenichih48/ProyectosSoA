import React, { useState, useEffect } from "react";
import '../Styles/menuStyle.css'
import Header from "./Header.js";

function MenuPage() {
  const [currentHighlightedMenu, setCurrentHighlightedMenu] = useState(null);
  const [menuItems, setMenuItems] = useState([]);

  useEffect(() => {
    async function fetchMenu() {
      try {
        const response = await fetch(`https://us-central1-soa-cloud.cloudfunctions.net/get_menu`);
        if (response.ok) {
          const menuData = await response.json();
          if (menuData.status_code === 200) {
            setMenuItems(menuData.data);
          }
        }
      } catch (error) {
        console.error('Error al obtener el menú:', error);
      }
    }

    fetchMenu();
  }, []);

  function highlightMenu(item, index) {
    if (currentHighlightedMenu && currentHighlightedMenu.id === index) {
      setCurrentHighlightedMenu(null);
      return;
    }

    setCurrentHighlightedMenu({ id: index });
  }
  
  return (
    
    <div className="MenuPage">
        <Header>
        </Header>
        <div className="container">
            <h1>Restaurant's Menu</h1>
            <h3>Please select an item to get recommendation <br/>(highlighted items are the recommendation paired with the selected menu item)</h3>
            <h2>Main Dishes</h2>
            <div className="dish-container" id="dish-container">
            {menuItems.map((item, index) => (
                <div
                key={index}
                className={`menu-item ${currentHighlightedMenu && currentHighlightedMenu.id === index ? 'highlight' : ''}`}
                onClick={() => highlightMenu(item, index)}
                >
                <h3>{item.dish}</h3>
                </div>
            ))}
            </div>
            <h2>Drinks</h2>
            <div className="drink-container" id="drink-container">
            {menuItems.map((item, index) => (
                <div
                key={index}
                className={`menu-item ${currentHighlightedMenu && currentHighlightedMenu.id === index ? 'highlight' : ''}`}
                onClick={() => highlightMenu(item, index)}
                >
                <h3>{item.drink}</h3>
                </div>
            ))}
            </div>
            <h2>Desserts</h2>
            <div className="dessert-container" id="dessert-container">
            {menuItems.map((item, index) => (
                <div
                key={index}
                className={`menu-item ${currentHighlightedMenu && currentHighlightedMenu.id === index ? 'highlight' : ''}`}
                onClick={() => highlightMenu(item, index)}
                >
                <h3>{item.dessert}</h3>
                </div>
            ))}
            </div>
        </div>
    </div>
  );
}

export default MenuPage;

﻿using System;
using System.Dynamic;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;


namespace MyServiceAPI.Controllers
{
    public class Menu
    {
        public string? dish { get; set; }
        public string? drink { get; set; }
        public string? dessert { get; set; }
    }

    public class DatabaseController
    {
        private readonly string filePath;

        public DatabaseController(string filePath)
        {
            this.filePath = filePath;
        }
        /// <summary>
        /// Searches for a full meal in the database based on the provided food and type.
        /// </summary>
        /// <param name="comida">The type of food to search for in the database.</param>
        /// <param name="tipo">The type of information to retrieve (e.g., "dish", "drink", or "dessert").</param>
        /// <returns>A JSON string representing the retrieved data of the menu item.
        /// If a menu item matching the provided food and type is found in the database,
        /// returns a JSON string containing the associated data (dish, drink, dessert).
        /// If no matching menu item is found, returns null.</returns>
        public string? SearchFullMeal(string comida, string tipo)
        {
            // Read the JSON file
            string jsonText = File.ReadAllText(filePath);

            // Parse the JSON array
            JArray menusArray = JArray.Parse(jsonText);

            // Search for the menu item matching the provided attribute and value
            JObject? matchingMenu = menusArray.Children<JObject>().FirstOrDefault(menu => (string?)menu[tipo] == comida);

            string? menuItemJson = null;

            if (matchingMenu != null)
            {
                // Menu item found, create a response
                var menuItem = new ExpandoObject() as IDictionary<string, object>;

                // Add non-null properties to the menu item object
                if (tipo != "dish" && matchingMenu["dish"] != null)
                    menuItem["dish"] = matchingMenu["dish"];

                if (tipo != "drink" && matchingMenu["drink"] != null)
                    menuItem["drink"] = matchingMenu["drink"];

                if (tipo != "dessert" && matchingMenu["dessert"] != null)
                    menuItem["dessert"] = matchingMenu["dessert"];

                // Serialize the menu item object to JSON format with indentation for readability
                menuItemJson = JsonConvert.SerializeObject(menuItem, Formatting.Indented);
            }
            // Return the JSON string representing the retrieved data of the menu item,
            // or null if no matching menu item is found
            return menuItemJson;
        }


        public (string,string) SearchDessert(string comida, string tipo)
        {
            // Read the JSON file
            string jsonText = File.ReadAllText(filePath);

            // Parse the JSON array
            JArray menusArray = JArray.Parse(jsonText);

            // Get a random index
            //int randomIndex = random.Next(0, menusArray.Count);
            return ("", "");
        }
        public (string, string) SearchDish(string comida, string tipo)
        {
            return ("","");
        }
        public (string, string) SearchDrink(string comida, string tipo)
        {
            return ("", "");
        }
    }
}

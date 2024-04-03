using System;
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

    public class MenuDatabaseController
    {
        private readonly string filePath;

        public MenuDatabaseController(string filePath)
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

            //Lower all user inputs
            tipo = tipo.ToLower();

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

        public string? getMenu ()
        {
            string? menuItemJson = null;

            // Read the JSON file
            string jsonText = File.ReadAllText(filePath);

            // Parse the JSON array
            JArray menusArray = JArray.Parse(jsonText);

            // Search for the menu item matching the provided attribute and value
            IEnumerable<JObject> allMenus = menusArray.Children<JObject>();

            if (!allMenus.Any()) 
            {
                return menuItemJson;
            } else
            {
                menuItemJson = JsonConvert.SerializeObject(allMenus, Formatting.Indented);
                return menuItemJson;
            }


        }


        public string? SearchSingle(string comida1, string tipo1, string request, string? comida2, string? tipo2)
        {
            bool setExists = true;

            // Read the JSON file
            string jsonText = File.ReadAllText(filePath);

            // Parse the JSON array
            JArray menusArray = JArray.Parse(jsonText);

            //Lower all user inputs
            tipo1 = tipo1.ToLower();

            if(tipo2 != null)
            {
                tipo2 = tipo2.ToLower();
            }
            

            // Search for the menu item matching the provided attribute and value
            JObject? matchingMenu = null;

            if (comida2 == null && tipo2 == null) // If only one parameter is provided
            {
                // Search for the menu item matching the provided attribute and value
                matchingMenu = menusArray.Children<JObject>().FirstOrDefault(menu => (string?)menu[tipo1] == comida1);
            }
            else // If two parameters are provided
            {
                // Check which parameters are provided and construct the query accordingly
                if (tipo1 == "dish" && tipo2 == "drink")
                {
                    matchingMenu = menusArray.Children<JObject>().FirstOrDefault(menu => (string?)menu["dish"] == comida1 && (string?)menu["drink"] == comida2);
                }
                else if (tipo1 == "dish" && tipo2 == "dessert")
                {
                    matchingMenu = menusArray.Children<JObject>().FirstOrDefault(menu => (string?)menu["dish"] == comida1 && (string?)menu["dessert"] == comida2);
                }
                else if (tipo1 == "drink" && tipo2 == "dish")
                {
                    matchingMenu = menusArray.Children<JObject>().FirstOrDefault(menu => (string?)menu["drink"] == comida1 && (string?)menu["dish"] == comida2);
                }
                else if (tipo1 == "drink" && tipo2 == "dessert")
                {
                    matchingMenu = menusArray.Children<JObject>().FirstOrDefault(menu => (string?)menu["drink"] == comida1 && (string?)menu["dessert"] == comida2);
                }
                else if (tipo1 == "dessert" && tipo2 == "dish")
                {
                    matchingMenu = menusArray.Children<JObject>().FirstOrDefault(menu => (string?)menu["dessert"] == comida1 && (string?)menu["dish"] == comida2);
                }
                else if (tipo1 == "dessert" && tipo2 == "drink")
                {
                    matchingMenu = menusArray.Children<JObject>().FirstOrDefault(menu => (string?)menu["dessert"] == comida1 && (string?)menu["drink"] == comida2);
                }
                if (matchingMenu == null)
                {
                    setExists = false;
                }
            }

            string? response = null;

            if (matchingMenu != null && setExists)
            {
                switch (request)
                {
                    case "1": // Search for dessert
                        response = (string?)matchingMenu["dessert"];
                        break;
                    case "2": // Search for dish
                        response = (string?)matchingMenu["dish"];
                        break;
                    case "3": // Search for drink
                        response = (string?)matchingMenu["drink"];
                        break;
                    default:
                        // Invalid request
                        return null;
                }

                // Construct a JSON object representing the dessert
                var responseObject = new
                {
                    response = response
                };

                // Serialize the menu item object to JSON format with indentation for readability
                response = JsonConvert.SerializeObject(responseObject, Formatting.Indented);
            }
            if (!setExists)
            {
                response = "515";
            }
            // Return the dessert associated with the specified dish or drink
            return response;
        }
    }
}

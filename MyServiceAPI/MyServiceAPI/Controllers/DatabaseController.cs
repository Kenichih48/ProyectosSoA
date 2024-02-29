﻿using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;


namespace MyServiceAPI.Controllers
{
    public class Menu
    {
        public string dish { get; set; }
        public string drink { get; set; }
        public string dessert { get; set; }
    }

    public class DatabaseController
    {

        public string filePath = "DataBase.json";

        private static Random random = new Random();

        public DatabaseController() { }


        public string SearchFullMeal()
        {
            // Read the JSON file
            string jsonText = File.ReadAllText(filePath);

            // Parse the JSON array
            JArray menusArray = JArray.Parse(jsonText);
            
            // Get a random index
            int randomIndex = random.Next(0, menusArray.Count);

            // Get the random menu object
            JObject randomMenuObject = (JObject)menusArray[randomIndex];
            
            // Deserialize the menu object into Menu class
            Menu randomMenu = randomMenuObject.ToObject<Menu>();


            string jsonMenu = JsonConvert.SerializeObject(randomMenu);


            return jsonMenu;
        }


        public (string,string) SearchDessert(string comida, string tipo)
        {
            // Read the JSON file
            string jsonText = File.ReadAllText(filePath);

            // Parse the JSON array
            JArray menusArray = JArray.Parse(jsonText);

            // Get a random index
            int randomIndex = random.Next(0, menusArray.Count);
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

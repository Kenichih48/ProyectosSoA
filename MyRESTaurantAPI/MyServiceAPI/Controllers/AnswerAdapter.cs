using System.Runtime.InteropServices;
using MyServiceAPI.Controllers;
using MyServiceAPI.Services;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace MyService.Data
{
    //Convierte las respuestas (dattapull, openai, endpoint) a un json de nuestra api.
    // header, body and status
    public class AnswerAdapter
    {
        private readonly string filePath1, filePath2;
        private readonly MenuDatabaseController menuDatabaseController;
        private readonly ReservationDatabaseController resDatabaseController;
        private AnswerGenerator answerGenerator = new AnswerGenerator();
        //private readonly InterfaceOpenAIService _openAIService;

        public AnswerAdapter(string filePath1, string filePath2)
        {
            this.filePath1 = filePath1;
            this.filePath2 = filePath2;
            this.menuDatabaseController = new MenuDatabaseController(filePath1);
            this.resDatabaseController = new ReservationDatabaseController(filePath2);
            //_openAIService = openAIService;
        }
        /// <summary>
        /// Retrieves data from the database based on the provided food and type.
        /// </summary>
        /// <param name="comida">The specified dish, drink or dessert to search for in the database.</param>
        /// <param name="tipo">The classification of the requested food (e.g., "dish", "drink", or "dessert").</param>
        /// <returns>A JSON string representing the response containing the retrieved data.
        /// If the requested menu item is found in the database, returns a success response
        /// containing the associated data (dish, drink, dessert).
        /// If the requested menu item does not exist, returns an error response.</returns>
        public string RetrieveDataFromMealDatabase(string comida1, string tipo1, string request, string? comida2, string? tipo2)
        {
            string? menuItemJson = null;

            if (request == "0")
            {
                menuItemJson = menuDatabaseController.SearchFullMeal(comida1, tipo1);
            }
            else if(request == "1" || request == "2" || request == "3")
            {
                menuItemJson = menuDatabaseController.SearchSingle(comida1, tipo1, request, comida2, tipo2);
            }
            else
            {
                // Invalid request
                return JsonConvert.SerializeObject(answerGenerator.GenerateErrorResponse(512, "Invalid request"), Formatting.Indented);
            }
            int status_code = 512;
            string errorMessage = "Requested menu item does not exist";

            if (menuItemJson == "515")
            {
                status_code = 515;
                errorMessage = "Set with both items does not exist";
                menuItemJson = null;
            }

            var response = menuItemJson != null ? answerGenerator.GenerateSuccessResponse(200, menuItemJson) : answerGenerator.GenerateErrorResponse(status_code, errorMessage);
            
            return JsonConvert.SerializeObject(response, Formatting.Indented);
        }

        public string RetrieveMenu()
        {
            string? menu = null;

            menu = menuDatabaseController.getMenu();

            int errorCode = 463;
            string errorMessage = "Menu items is empty";

            var response = menu != null ? answerGenerator.GenerateSuccessResponse(200, menu) : answerGenerator.GenerateErrorResponse(errorCode, errorMessage);

            return JsonConvert.SerializeObject(response, Formatting.Indented);
        }


        public string RetrieveDataFromReservationDatabase(string date, string time)
        {
            
            
            string reservationJson = this.resDatabaseController.SearchBestOptions(date, time);

            return reservationJson;
        }

    }
}
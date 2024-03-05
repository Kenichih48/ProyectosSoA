using System.Runtime.InteropServices;
using MyServiceAPI.Controllers;
using MyServiceAPI.Services;
using Newtonsoft.Json;

namespace MyService.Data
{
    //Convierte las respuestas (dattapull, openai, endpoint) a un json de nuestra api.
    // header, body and status
    public class AnswerAdapter
    {
        private readonly string filePath;
        private readonly DatabaseController databaseController;
        private readonly InterfaceOpenAIService _openAIService;

        public AnswerAdapter(string filePath,InterfaceOpenAIService openAIService)
        {
            this.filePath = filePath;
            this.databaseController = new DatabaseController(filePath);
            _openAIService = openAIService;
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
        public string RetrieveDataFromDatabase(string comida1, string tipo1, string request, string? comida2, string? tipo2)
        {
            // CHANGE jsonData TO WHATEVER WE USE TO GET THE DATA FROM THE DATABASE
            // jsonData = await AnswerAdapterData.GetData();
            string? menuItemJson = null;

            if (request == "0")
            {
                menuItemJson = databaseController.SearchFullMeal(comida1, tipo1);
            }
            else if(request == "1" || request == "2" || request == "3")
            {
                menuItemJson = databaseController.SearchSingle(comida1, tipo1, request, comida2, tipo2);
            }
            else
            {
                // Invalid request
                return JsonConvert.SerializeObject(GenerateErrorResponse(512, "Invalid request"), Formatting.Indented);
            }
            int status_code = 512;
            string errorMessage = "Requested menu item does not exist";

            if (menuItemJson == "519")
            {
                status_code = 519;
                errorMessage = "Set with both items does not exist";
                menuItemJson = null;
            }

            var response = menuItemJson != null ? GenerateSuccessResponse(200, menuItemJson) : GenerateErrorResponse(status_code, errorMessage);
            
            return JsonConvert.SerializeObject(response, Formatting.Indented);
        }

        public async Task<string> RetrieveDataFromOpenAIAPI(string comida, string tipo, string request)
        {
            string? response = null;
            
            if (request == "0")
            {
                response = await _openAIService.getFoodRecomendations(tipo+":"+comida);
            }
            else if (request == "1" )
            {
                response = await _openAIService.getFoodRecomendations(tipo + ":" + comida+ " I only want the dessert");
            }
            else if (request == "2" )
            {
                response = await _openAIService.getFoodRecomendations(tipo + ":" + comida + " I only want the dish");
            }
            else if (request == "3")
            {
                response = await _openAIService.getFoodRecomendations(tipo + ":" + comida + " I only want the drink");
            }
            else
            {
                // Invalid request
                return JsonConvert.SerializeObject(GenerateErrorResponse(512, "Invalid request"), Formatting.Indented);
            }

            var finalresponse = response != null ? GenerateSuccessResponse(200, response) : GenerateErrorResponse(513, "Error With OpenAI request");

            return JsonConvert.SerializeObject(finalresponse, Formatting.Indented);
            
        }
        public async Task<string> RetrieveDataFromExternalEndPoint(string comida1, string tipo1, string request, string? comida2 = null, string? tipo2 = null)
        {

            // CHANGE jsonData TO WHATEVER WE USE TO GET THE DATA FROM THE EXTERNALENDPOINTAPI
            HttpClient client = new HttpClient();
            string _url = formatUrl(comida1,tipo1,request,comida2,tipo2);
            HttpResponseMessage response = await client.GetAsync(_url);
            string jsonData = await response.Content.ReadAsStringAsync();
            return jsonData;
        }

        public string formatUrl(string comida1, string tipo1, string request, string? comida2 = null, string? tipo2 = null)
        {
            bool secondaryMeal = false;
            if (comida2 != null && tipo2 != null)
            {
                secondaryMeal = true;
            }
            if (tipo1 == "dish")
            {
                tipo1 = "meal";

                if ((tipo2 == "dish"))
                {
                    tipo2 = "meal";
                }
            }

            if (secondaryMeal)
            {
                return "http://soa41d-project1.eastus.azurecontainer.io/recommendation/custom?" + tipo1 + "=" + comida1 + "&" + tipo2 + "=" + comida2;
            }

            return "http://soa41d-project1.eastus.azurecontainer.io/recommendation/custom?" + tipo1 + "=" + comida1;

        }
        
        private string TransformJsonToDesiredFormat(string jsonData)
        {
            // LOGIC TO TRANSFORM ANY GIVEN DATA TO OUR NEEDED ANSWER FORMAT
            return jsonData;
        }

        /// <summary>
        /// Generates a success response object for the given input JSON.
        /// </summary>
        /// <param name="input">The JSON input</param>
        /// <returns>A success response object containing the input JSON</returns>
        private object GenerateSuccessResponse(int status_code, string input)
        {
            var jsonData = JsonConvert.DeserializeObject(input);

            var response = new
            {
                status_code = status_code,
                status = "success",
                data = jsonData
            };

            return response;
        }

        /// <summary>
        /// Generates an error response object
        /// </summary>
        /// <returns>An error response object</returns>
        private object GenerateErrorResponse(int status_code, string input)
        {
            // Construct the error response object
            var response = new
            {
                status_code = status_code,
                status = "error",
                message = input
            };

            return response;
        }
    }
}
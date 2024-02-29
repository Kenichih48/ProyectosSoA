using MyServiceAPI.Controllers;
using Newtonsoft.Json;

namespace MyService.Data
{
    //Convierte las respuestas (dattapull, openai, endpoint) a un json de nuestra api.
    // header, body and status
    public class AnswerAdapter
    {
        private readonly string filePath;
        private readonly DatabaseController databaseController;
        public AnswerAdapter(string filePath)
        {
            this.filePath = filePath;
            this.databaseController = new DatabaseController(filePath);
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
        public string RetrieveDataFromDatabase(string comida, string tipo)
        {
            // CHANGE jsonData TO WHATEVER WE USE TO GET THE DATA FROM THE DATABASE
            // jsonData = await AnswerAdapterData.GetData();

            string menuItemJson = databaseController.SearchFullMeal(comida, tipo);

            var response = menuItemJson != null ? GenerateSuccessResponse(menuItemJson) : GenerateErrorResponse();

            return JsonConvert.SerializeObject(response, Formatting.Indented);
        }

        public async Task<string> RetrieveDataFromOpenAIAPI()
        {
            // CHANGE jsonData TO WHATEVER WE USE TO GET THE DATA FROM THE OPENAI API
            //var response = await httpClient.GetAsync(openAIApiEndpoint);
            //var jsonData = await response.Content.ReadAsStringAsync();
            string jsonData = "";
            return jsonData;
        }
        public async Task<string> RetrieveDataFromExternalEndPoint()
        {
            // CHANGE jsonData TO WHATEVER WE USE TO GET THE DATA FROM THE EXTERNALENDPOINTAPI
            // var response = await httpClient.GetAsync(externalEndPointApiEndpoint);
            // var jsonData = await response.Content.ReadAsStringAsync();
            string jsonData = "";
            return jsonData;
        }

        /*
        public string AdaptAnswerToDesiredFormat(string source, string comida, string tipo)
        {
            string jsonData = "";

            switch (source)
            {
                case "database":
                    // Retrieve data from the database
                    jsonData = RetrieveDataFromDatabase();
                    break;
                case "openai":
                    // Retrieve data from the OpenAI API
                    jsonData = RetrieveDataFromOpenAIAPI().Result;
                    break;
                case "externalep":
                    // Retrieve data from the ExternalEndPoint API
                    jsonData = RetrieveDataFromExternalEndPoint().Result;
                    break;
                default:
                    throw new ArgumentException("Invalid data source provided.");
            }

            return TransformJsonToDesiredFormat(jsonData);
        }
        */
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
        private object GenerateSuccessResponse(string input)
        {
            var jsonData = JsonConvert.DeserializeObject(input);

            return new
            {
                status_code = 200,
                status = "success",
                data = jsonData
            };
        }

        /// <summary>
        /// Generates an error response object indicating that the requested menu item does not exist.
        /// </summary>
        /// <returns>An error response object indicating that the requested menu item does not exist.</returns>
        private object GenerateErrorResponse()
        {
            return new
            {
                status_code = 512,
                status = "error",
                message = "Requested menu item does not exist"
            };
        }

    }
}
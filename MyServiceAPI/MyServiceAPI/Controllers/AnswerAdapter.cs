using MyServiceAPI.Controllers;

namespace MyService.Data
{
    public class AnswerAdapter
    {   

        DatabaseController databaseController = new DatabaseController();
        public AnswerAdapter()
        {
        }
        public string RetrieveDataFromDatabase(string tipo, string comida)
        {
            // CHANGE jsonData TO WHATEVER WE USE TO GET THE DATA FROM THE DATABASE
            // jsonData = await AnswerAdapterData.GetData();
            string jsonData = "";

            if(tipo == "" && comida == "")
            {
                jsonData = databaseController.SearchFullMeal();
            }
            Console.WriteLine(jsonData);
            return jsonData;
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
        
    }
}
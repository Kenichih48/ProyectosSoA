using System;
using System.Dynamic;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;



namespace MyServiceAPI.Controllers
{
    public class Reservation
    {
        public string? date { get; set; }
        public string? time { get; set; }
    }

    public class ReservationDatabaseController
    {
        private readonly string filePath;
        private AnswerGenerator answerGenerator = new AnswerGenerator();

        public ReservationDatabaseController(string filePath)
        {
            this.filePath = filePath;
        }


        public string SearchBestOptions(string date, string time)
        {
            // Read the JSON file
            string jsonText = File.ReadAllText(filePath);

            // Parse the JSON array
            JArray reservationsArray = JArray.Parse(jsonText);



            // Search for the menu item matching the provided attribute and value
            JObject? exactMatch = reservationsArray.Children<JObject>()
                .FirstOrDefault(res => (string?)res["Date"] == date && (string?)res["Time"] == time && (string?)res["State"] == "Free");
            
            List<string> resPossibleList = new List<string>();

            string resItemJson = null;
            var resItem = new ExpandoObject() as IDictionary<string, object>;

            if (exactMatch == null)
            {
                List<JObject> notexactMatch = reservationsArray.Children<JObject>()
                    .Where(res => ((string?)res["Date"] == date || (string?)res["Time"] == time) && (string?)res["State"] == "Free").ToList();

                List<string> listResItemJson = new List<string>();
                foreach (JObject obj in notexactMatch)
                {
                    var resIItem = new ExpandoObject() as IDictionary<string, object>;
                    resIItem["Date"] = obj["Date"];
                    resIItem["Time"] = obj["Time"];
                    listResItemJson.Add(JsonConvert.SerializeObject(resIItem, Formatting.Indented));
                    

                }

                resItemJson = "[" + string.Join(",", listResItemJson) + "]";

                var resAnswer = notexactMatch.Count != 0 ? answerGenerator.GenerateSuccessResponse(201, resItemJson) : answerGenerator.GenerateErrorResponse(462, "Invalid date or time");

                return JsonConvert.SerializeObject(resAnswer, Formatting.Indented); ;
            }
            else
            {
                resItem["Date"] = exactMatch["Date"];
                resItem["Time"] = exactMatch["Time"];

                resItemJson = JsonConvert.SerializeObject(resItem, Formatting.Indented);

                resItemJson = "["+resItemJson+"]";

                var resAnswer = answerGenerator.GenerateSuccessResponse(200, resItemJson);

                //!!!!!CHANGE THE STATE FROM FREE TO TAKEN

                return JsonConvert.SerializeObject(resAnswer, Formatting.Indented);
            }
        }


    }
}

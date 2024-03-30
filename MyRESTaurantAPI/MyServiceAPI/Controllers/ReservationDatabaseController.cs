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

            string? resItemJson = null;
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
                    resIItem["Exact"] = "no";
                    listResItemJson.Add(JsonConvert.SerializeObject(resIItem, Formatting.Indented));

                }

                resItemJson = "[" + string.Join(",", listResItemJson) + "]";


            }
            else
            {
                resItem["Date"] = exactMatch["Date"];
                resItem["Time"] = exactMatch["Time"];
                resItem["Exact"] = "yes";

                resItemJson = JsonConvert.SerializeObject(resItem, Formatting.Indented);

                resItemJson = "["+resItemJson+"]";
            }

            // Serialize the menu item object to JSON format with indentation for readability
            

            // Return the JSON string representing the retrieved data of the menu item,
            // or null if no matching menu item is found
            return resItemJson;
        }


    }
}

using Microsoft.AspNetCore.Mvc;
using MyService.Data;
using MyServiceAPI.Services;
using Newtonsoft.Json;
using System;
//using System.Runtime.InteropServices.Marshalling;

namespace MyServiceAPI.Controllers
{
    [ApiController]
    
    public class UserRequestController
    {
        //private readonly InterfaceOpenAIService _openAIService;
        public AnswerAdapter answeradapter;

        public UserRequestController()
        {
            //_openAIService = openAIService;
            answeradapter = new AnswerAdapter("MealDataBase.json", "ReservationDataBase.json");
        }

        [HttpGet]
        [Route("GetAvailabilty")]
        public string GetAvailabilty(string? date, string? time)
        {
            string response;

            if (date == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(460, "Date is empty"), Formatting.Indented);

            }
            else if (time == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(461, "Time is empty"), Formatting.Indented);
            }

            response = ProcessReservation(date, time);

            return response;

        }

        [HttpGet]
        [Route("GetFullMeal")]
        public string GetFullMeal(string? comida, string? tipo)
        {
            /*if (Id == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(452, "Id is empty"), Formatting.Indented);
            }else */
            if (comida == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(453, "Comida is empty"), Formatting.Indented);
            }else if (tipo == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(454, "Tipo is empty"), Formatting.Indented);
            }
            string response = ProcessMeal(comida, tipo, "0", null, null);
            
            return response;
        }

        [HttpGet]
        [Route("GetDessert")]
        public string GetDessert(string? comida1, string? tipo1, string? comida2, string? tipo2)
        {
            /*if (Id == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(452, "Id is empty"), Formatting.Indented);
            }
            else */
            if (comida1 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(453, "Comida1 is empty"), Formatting.Indented);
            }
            else if (tipo1 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(454, "Tipo1 is empty"), Formatting.Indented);
            }
            else if (comida2 != null && tipo2 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(455, "Tipo2 is empty while Comida2 is not"), Formatting.Indented);
            }
            else if (comida2 == null && tipo2 != null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(456, "Comida2 is empty while Tipo2 is not"), Formatting.Indented);
            }
            string response = ProcessMeal(comida1, tipo1, "1", comida2, tipo2);
            return response;
        }

        [HttpGet]
        [Route("GetDish")]
        public string GetDish(string? comida1, string? tipo1, string? comida2, string? tipo2)
        {
            /*if (Id == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(452, "Id is empty"), Formatting.Indented);
            }
            else */
            if (comida1 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(453, "Comida1 is empty"), Formatting.Indented);
            }
            else if (tipo1 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(454, "Tipo1 is empty"), Formatting.Indented);
            }
            else if (comida2 != null && tipo2 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(455, "Tipo2 is empty while Comida2 is not"), Formatting.Indented);
            }
            else if (comida2 == null && tipo2 != null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(456, "Comida2 is empty while Tipo2 is not"), Formatting.Indented);
            }
            string response = ProcessMeal(comida1, tipo1, "2", comida2, tipo2);
            return response;
        }

        [HttpGet]
        [Route("GetDrink")]
        public string GetDrink(string? comida1, string? tipo1, string? comida2, string? tipo2)
        {
            /*if (Id == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(452, "Id is empty"), Formatting.Indented);
            }
            else */
            if (comida1 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(453, "Comida1 is empty"), Formatting.Indented);
            }
            else if (tipo1 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(454, "Tipo1 is empty"), Formatting.Indented);
            }
            else if (comida2 != null && tipo2 == null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(455, "Tipo2 is empty while Comida2 is not"), Formatting.Indented);
            }
            else if (comida2 == null && tipo2 != null)
            {
                return JsonConvert.SerializeObject(GenerateErrorResponse(456, "Comida2 is empty while Tipo2 is not"), Formatting.Indented);
            }
            string response = ProcessMeal(comida1, tipo1, "3", comida2, tipo2);
            return response;
        }

        private string ProcessMeal(string comida1, string tipo1, string request, string? comida2, string? tipo2)
        {
            string response = "";

            response = answeradapter.RetrieveDataFromMealDatabase(comida1, tipo1, request, comida2, tipo2);
            /*
            else if (key == "1")
            {
                response = answeradapter.RetrieveDataFromOpenAIAPI(comida1, tipo1, request).Result;
            }
            else if (key == "2")
            {
                response = answeradapter.RetrieveDataFromExternalEndPoint(comida1, tipo1, request, comida2, tipo2).Result;
            }
            */
            return response;
        }

        private string ProcessReservation(string date, string time)
        {
            string response = "";

            response = answeradapter.RetrieveDataFromReservationDatabase(date, time);

            return response;
        }

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

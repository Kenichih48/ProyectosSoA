using Microsoft.AspNetCore.Mvc;
using MyService.Data;
using MyServiceAPI.Services;
using System;
using System.Runtime.InteropServices.Marshalling;

namespace MyServiceAPI.Controllers
{
    [ApiController]
    
    public class UserRequestController
    {
        private readonly InterfaceOpenAIService _openAIService;
        public AnswerAdapter answeradapter;

        public UserRequestController(InterfaceOpenAIService openAIService)
        {
            _openAIService = openAIService;
            answeradapter = new AnswerAdapter("DataBase.json",openAIService);
        }


        [HttpGet]
        [Route("GetFullMeal")]
        public string GetFullMeal(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo, "0");
            
            return response;
        }

        [HttpGet]
        [Route("GetDessert")]
        public string GetDessert(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo, "1");
            return response;
        }

        [HttpGet]
        [Route("GetDish")]
        public string GetDish(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo, "2");
            return response;
        }

        [HttpGet]
        [Route("GetDrink")]
        public string GetDrink(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo, "3");
            return response;
        }

        private string ProcessKey(string key, string comida, string tipo, string request)
        {
            string response = "";
            if (key == "0")
            {
                response = answeradapter.RetrieveDataFromDatabase(comida, tipo, request);
            }
            else if (key == "1")
            {
                response = answeradapter.RetrieveDataFromOpenAIAPI(comida, tipo, request).Result;
            }
            else if (key == "2")
            {
                //response = ExternalAdapter
            }
            return response;
        }
    }
}

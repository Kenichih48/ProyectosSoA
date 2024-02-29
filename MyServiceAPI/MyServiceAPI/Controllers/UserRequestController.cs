using Microsoft.AspNetCore.Mvc;
using MyService.Data;
using System;

namespace MyServiceAPI.Controllers
{
    [ApiController]
    [Route("MyService")]
    public class UserRequestController
    {
        
        public AnswerAdapter answeradapter = new AnswerAdapter("DataBase.json");

        [HttpGet]
        [Route("GetFullMeal")]
        public string GetFullMeal(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida,tipo );
            
            return response;
        }

        [HttpGet]
        [Route("GetDessert")]
        public string GetDessert(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo);
            return response;
        }

        [HttpGet]
        [Route("GetDish")]
        public string GetDish(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo);
            return response;
        }

        [HttpGet]
        [Route("GetDrink")]
        public string GetDrink(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo);
            return response;
        }

        private string ProcessKey(string key, string comida, string tipo)
        {
            string response = "";
            if (key == "0")
            {
                response = answeradapter.RetrieveDataFromDatabase(comida, tipo);
            }
            else if (key == "1")
            {
                //response = AIAdapter
            }
            else if (key == "2")
            {
                //response = ExternalAdapter
            }
            return response;
        }
    }
}

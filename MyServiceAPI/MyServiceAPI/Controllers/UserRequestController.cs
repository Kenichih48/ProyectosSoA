using Microsoft.AspNetCore.Mvc;

namespace MyServiceAPI.Controllers
{
    [ApiController]
    [Route("MyService")]
    public class UserRequestController
    {
        //public KeyCheck keycheck = new KeyCheck();
        [HttpGet]
        [Route("GetFullMeal")]
        public string GetFullMeal(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo);
            return "1";
        }

        [HttpGet]
        [Route("GetDessert")]
        public string GetDessert(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo);
            return "1";
        }

        [HttpGet]
        [Route("GetLunch")]
        public string GetLunch(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo);
            return "1";
        }

        [HttpGet]
        [Route("GetDrink")]
        public string GetDrink(string Id, string comida, string tipo)
        {
            string response = ProcessKey(Id, comida, tipo);
            return "1";
        }

        private string ProcessKey(string key, string comida, string tipo)
        {
            string response = "";
            if (key == "0")
            {
                //response = Datapull
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

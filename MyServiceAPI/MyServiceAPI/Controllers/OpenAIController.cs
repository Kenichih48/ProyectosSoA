using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using MyServiceAPI.Configurations;
using MyServiceAPI.Services;

namespace MyServiceAPI.Controllers
{
    [ApiController]
    [Route("MyService")]
    public class OpenAIController
    {
        private readonly InterfaceOpenAIService _openAIService;



        [HttpGet]
        [Route("Test")]
        public string testMethod(string text)
        {
            string result = "Hola";

            return result;
        }
    }
}

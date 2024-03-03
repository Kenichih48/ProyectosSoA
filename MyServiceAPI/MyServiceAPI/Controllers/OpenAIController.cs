using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using MyServiceAPI.Configurations;
using MyServiceAPI.Services;
/*
namespace MyServiceAPI.Controllers
{
    [ApiController]
    [Route("MyService")]
    public class OpenAIController: ControllerBase
    {
        private readonly InterfaceOpenAIService _openAIService;

        public OpenAIController(InterfaceOpenAIService openAIService){
            _openAIService = openAIService;
        }

        [HttpGet]
        [Route("Test")]
        public async Task<IActionResult> testMethod(string text)
        {
            var result = await _openAIService.getFoodRecomendations(text);
            return Ok(result);
        }
    }
}
*/

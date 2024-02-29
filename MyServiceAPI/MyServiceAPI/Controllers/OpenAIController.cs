using Microsoft.AspNetCore.Mvc;

namespace MyServiceAPI.Controllers
{
    [ApiController]
    [Route("MyService")]
    public class OpenAIController
    {

        [HttpGet]
        [Route("Test")]
        public string test(string promt)
        {

            

        }
    }
}

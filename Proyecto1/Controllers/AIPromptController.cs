namespace FoodAPI.Controllers
{   
    var openAiService = new OpenAIService(new OpenAiOptions()  
    {
    ApiKey =  Environment.GetEnvironmentVariable("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") //Llave de jose ( no usar excepto jose >:( )
    });
    public class AIPromotController : Controller
    {
        public void sendPrompt(string AIPrompToSend)
        {   
            //Ask OpenApi for the needed response
            var completionResult = await openAiService.ChatCompletion.CreateCompletion(new ChatCompletionCreateRequest
            {
                Messages = new List<ChatMessage>
                {
                    ChatMessage.FromSystem("You are a master food critic that knows everything about food recommendations. The user will give you a dessert, a drink, or a main dish. Your job is to respond with your expert recommendations by filling in the missing drink, dessert and/or main dish, while responding in the following format: {dish:\"*name of dish*\", drink:\"*name of drink*\", dessert:\"*name of dessert*\". Make sure to only respond with that format and nothing else"),
                    ChatMessage.FromUser("Who won the world series in 2020?"),
                    ChatMessage.FromAssistant("The Los Angeles Dodgers won the World Series in 2020."),
                    ChatMessage.FromUser("Where was it played?")
                },
                Model = Models.ChatGpt3_5Turbo,
            });

            if (completionResult.Successful)
            {
            Console.WriteLine(completionResult.Choices.First().Message.Content);
            }

        }

    }
}
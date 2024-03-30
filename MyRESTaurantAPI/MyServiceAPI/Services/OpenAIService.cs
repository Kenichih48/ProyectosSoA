using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using MyServiceAPI.Configurations;
using MyServiceAPI.Services;

public class OpenAIService : InterfaceOpenAIService
{
    private readonly OpenAiConfiguration openAIConfig;
    public OpenAIService(
        IOptionsMonitor<OpenAiConfiguration> optionsMonitor)
    {
        openAIConfig = optionsMonitor.CurrentValue;
    }
    public async Task<string> getFoodRecomendations(string sendPrompt)
    {
        //setup api with the key
        var api = new OpenAI_API.OpenAIAPI(openAIConfig.Key);

        var chat = api.Chat.CreateConversation();

        chat.AppendSystemMessage("You are a master food critic that knows everything about food recommendations. The user will give you a dessert, a drink, or a main dish. Your job is to respond with your expert recommendations by filling in the missing drink, dessert and/or main dish, while responding in the following format: {dish:\"*name of dish*\", drink:\"*name of drink*\", dessert:\"*name of dessert*\". Make sure to only respond with that format and nothing else");

        chat.AppendUserInput(sendPrompt);

        var response = await chat.GetResponseFromChatbotAsync();

        return response;
    }
}
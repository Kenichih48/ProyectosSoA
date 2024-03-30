namespace MyServiceAPI.Services;

public interface InterfaceOpenAIService
{
    Task<string> getFoodRecomendations(string Text);
}
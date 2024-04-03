using MyServiceAPI.Configurations;
using MyServiceAPI.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.Configure<OpenAiConfiguration>(builder.Configuration.GetSection("OpenAI"));
builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddScoped<InterfaceOpenAIService, OpenAIService>();

builder.Services.AddCors(options => {


    options.AddDefaultPolicy(
        policy =>
        {
            policy.AllowAnyHeader();
            policy.AllowAnyMethod();
            policy.AllowAnyOrigin();

        });

});

var app = builder.Build();





// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.UseCors();

app.Run();

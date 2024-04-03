using Newtonsoft.Json;

namespace MyServiceAPI.Controllers
{
    public class AnswerGenerator
    {
        /// <summary>
        /// Generates a success response object for the given input JSON.
        /// </summary>
        /// <param name="input">The JSON input</param>
        /// <returns>A success response object containing the input JSON</returns>
        public object GenerateSuccessResponse(int status_code, string input)
        {
            var jsonData = JsonConvert.DeserializeObject(input);

            var response = new
            {
                status_code = status_code,
                status = "success",
                data = jsonData
            };

            return response;
        }

        /// <summary>
        /// Generates an error response object
        /// </summary>
        /// <returns>An error response object</returns>
        public object GenerateErrorResponse(int status_code, string input)
        {
            // Construct the error response object
            var response = new
            {
                status_code = status_code,
                status = "error",
                message = input
            };

            return response;
        }
    }
}

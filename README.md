
# AWSummarizeTech 🌐

AWSummarizeTech is a cloud-based solution that leverages AWS services to provide efficient text summarization. By integrating AWS Bedrock, Lambda, and API Gateway, this project ensures scalable and quick data processing.

## Architecture 🏗️

![AWSummarizeTech Architecture](./assets/Web%20App%20Reference%20Architecture.png)

1. **User**: Initiates a REST API request with the prompt.
2. **API Gateway**: Receives the request and forwards the prompt to AWS Lambda.
3. **Lambda**: Processes the event and invokes the LLM model via Bedrock.
4. **Bedrock**: Utilizes the Cohere Foundation Model to generate a summarized response.
5. **Lambda**: Receives the summarized response and sends it back to the API Gateway.
6. **API Gateway**: Returns the summarized response to the user.

## Features ✨

- **Seamless Integration**: Combines multiple AWS services for a cohesive and efficient text summarization process.
- **Scalable**: Designed to handle varying loads by leveraging AWS Lambda’s serverless architecture.
- **Quick Processing**: Ensures fast response times through optimized data handling and processing pipelines.
- **Robust Security**: Utilizes AWS’s security features to ensure data protection and secure communication.

## Prerequisites 📋

- AWS account with access to AWS Lambda, API Gateway, and Bedrock services.
- Node.js and npm installed locally for deploying the Lambda function.

## Setup 🚀

### 1. Create an AWS Lambda Function

- **Function Name**: `AWSummarizeTechFunction`
- **Responsibilities**:
  - **Connect to AWS Bedrock**: Utilize the Cohere Foundation Model to generate summaries based on user-provided prompts.
  - **Send the Summary**: Respond to requests via AWS API Gateway with the summarized text.

### 2. Grant the Right Permissions to Lambda Function (IAM Role)

- **IAM Role**: Create an IAM Role with the following policies attached for necessary permissions:
  - **AmazonBedrockFullAccess**: Grants full access to Bedrock services.
  - **Timeout Settings**: Configure the AWS Lambda function timeout settings to accommodate the time taken by Bedrock API to generate summaries.

### 3. Create a REST API Using AWS API Gateway

- **API Name**: `AWSummarizeTechAPI`
- **Functionality**: Allow users to submit a prompt and return the summarized text.
  - **Receive Prompt**: Users pass the text summarization prompt through the API.
  - **Return Summary**: Users receive the summarized text.

### 4. Test Using Postman API Tool 🛠️

- **Testing**: Use Postman to send requests to the `AWSummarizeTechAPI` and ensure the entire flow from prompt submission to summary retrieval functions correctly.

## Usage 📦

Send a POST request to the API Gateway endpoint with the following JSON payload:

```json
{
  "prompt": "Your text to be summarized"
}
```

The summarized response will be returned in the following format:

```json
{
  "summarizedResponse": "The summarized text"
}
```

## Contributing 🤝

We welcome contributions to AWSummarizeTech! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

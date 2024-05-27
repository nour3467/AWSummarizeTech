
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

## Generative AI with Bedrock: Step by Step – Pre-Requisites 📋

1. **Create an AWS Lambda Function** - `demoManufacturing`
2. **Check the boto3 version. Should be >= 1.28.63**
    - Use the following command to check the version:
      ```python
      print(boto3.__version__)
      ```
3. **Upgrade the boto3 version for AWS Lambda Function using Lambda Layer**
    - [AWS Knowledge Center: Lambda Python runtime errors](https://repost.aws/knowledge-center/lambda-python-runtime-errors)
    - Add Layer Version ARN
    - Check the boto3 version. Should be > 1.28.63

## Generative AI with Bedrock: Step by Step Guide 🚀

### 1. Create an IAM Role and Increase Timeout Limit

### 2. Code for Bedrock Invocation from AWS Lambda Function

- [Boto3 Documentation for Bedrock](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html)

### 3. Configure Test Event

```json
{ "prompt": "How is weather in Bengaluru" }
```

### Broad Steps for Writing Lambda Function

1. **Import boto3 and create client connection with bedrock**
2. a. **Store the input in a variable**
   b. **Print the event**
3. **Create Request Syntax** - Get details from console & body should be JSON object - use `json.dumps` for body
4. **Convert Streaming Body to Byte (`.read` method) and then Byte to String using `json.loads`**
5. a. **Print the event and type**
   b. **Store the input in a variable**
6. **Update the 'return' by changing the 'body'**

### 4. Create a REST API from API Gateway

- Resource – `demoManufacturing`
- Method - POST

### 5. API Gateway - Method Request

- URL query string parameters – Add input parameter

### 6. API Gateway - Integration Request

- `application/json`
```json
{ "prompt": "$input.params('prompt')" }
```

### 7. Deploy the API to a Stage

### 8. Test using API Gateway Console

### 9. Sample Text - Link

## Prompt for Summarization Task 📝

This is an on-site log report of turbine breakdown.
- **Issue Log Date** – 25-12-2023
- **Model Number** – TB-CL-7882
- **Issue** - Cracks appeared in the part MR 7882-9571 next to the rotor hub. The nut connecting the rotor blade to the rotor hub seems to be damaged. The Anemometer readings seem to be within range. The electric braking seems to be unused. No indication of damage to any other component of the turbine except normal wear and tear.
- **Potential Root Cause** – Seems due to reduced tensile strength of the nut connecting the blade to the rotor.
- **Last Maintenance Date** – 12-12-2023
- **Last Maintenance Issues Recorded** - No known issues recorded and all the parameters were within range.

**Summarize the text in 2 lines.**

## Possible and Actual – Completion from the Model

**Possible Response:**
- Model No-TB-CL-7882, Issue - The nut connecting the rotor blade to the rotor hub seems to be damaged, Potential Root Cause – Seems due to reduced tensile strength of the nut connecting the blade to the rotor. No known issues recorded in last maintenance.

**Actual Response:**
- The turbine experienced cracks in a part and possible damage to the nut connecting the rotor blade, but the anemometer readings were within range. It is unclear what has caused the issue, but it is assumed to be due to reduced tensile strength.


## 🎥 Demo Video

Watch the demo video below to see the AWS Movie Poster Creator in action:

https://github.com/nour3467/AWSummarizeTech/assets/71594772/f6e4b900-101f-410d-9370-97ad1b5b9628


## Contributing 🤝

We welcome contributions to AWSummarizeTech! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
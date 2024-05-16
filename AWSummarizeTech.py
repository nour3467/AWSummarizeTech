import json
import boto3

# Create client connection with Bedrock
client_bedrock = boto3.client("bedrock-runtime")


def lambda_handler(event, context):
    """
    AWS Lambda handler function to process text summarization using AWS Bedrock.

    :param event: The event data passed to the Lambda function, expected to contain the 'prompt' key.
    :param context: The context in which the Lambda function is executed.
    :return: A dictionary with the status code and the summarized text.
    """
    # Store the input prompt in a variable and print the event
    input_prompt = event["prompt"]
    print("Received prompt:", input_prompt)

    # Create a request to the Bedrock model
    client_bedrock_request = client_bedrock.invoke_model(
        contentType="application/json",
        accept="application/json",
        modelId="cohere.command-light-text-v14",
        body=json.dumps(
            {
                "prompt": input_prompt,
                "temperature": 0.9,
                "p": 0.75,
                "k": 0,
                "max_tokens": 100,
            }
        ),
    )

    # Convert streaming body to byte and then byte to string
    client_bedrock_byte = client_bedrock_request["body"].read()
    client_bedrock_string = json.loads(client_bedrock_byte)

    # Print the response for debugging
    print("Bedrock response:", client_bedrock_string)

    # Extract the summarized text from the response
    client_final_response = client_bedrock_string["generations"][0]["text"]
    print("Summarized response:", client_final_response)

    return {"statusCode": 200, "body": json.dumps(client_final_response)}

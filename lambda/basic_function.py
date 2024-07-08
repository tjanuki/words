import logging

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }

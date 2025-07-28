import os

def lambda_handler(event, context):
    stage = os.environ.get("STAGE_NAME", "unknown")
    return {
        "statusCode": 200,
        "body": f"Hello from the {stage} stage!"
    }


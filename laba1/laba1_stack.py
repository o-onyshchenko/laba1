from aws_cdk import (
    Stack,
    aws_lambda,
    aws_apigateway
)
from constructs import Construct

class Laba1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        myservice_lambda = aws_lambda.Function(self, "LambdaService",
            code=aws_lambda.Code.from_asset("laba1/service"),
            handler="index.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
        )

        api = aws_apigateway.RestApi(self, "Service-Api")
        lambda_integration = aws_apigateway.LambdaIntegration(myservice_lambda)
        api.root.add_method("GET", lambda_integration)

import aws_cdk as core
import aws_cdk.assertions as assertions

from laba1.laba1_stack import Laba1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in laba1/laba1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Laba1Stack(app, "laba1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

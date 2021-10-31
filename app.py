import os
from aws_cdk import core as cdk
from aws_cdk import core
from data_platform.data_lake.stack import DataLakeStack
from data_platform.kinesis.stack import KinesisStack

app = core.App()
data_lake_stack = DataLakeStack(app)
kinesis_stack = KinesisStack(app, data_lake_raw_bucket=data_lake_stack.data_lake_raw_bucket)
app.synth()

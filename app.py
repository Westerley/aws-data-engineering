from aws_cdk import core
from data_platform.data_lake.stack import DataLakeStack
from data_platform.common_stack import CommonStack
from data_platform.kinesis.stack import KinesisStack
from data_platform.dms.stack import DmsStack
from data_platform.glue_catalog.stack import GlueCatalogStack
from data_platform.athena.stack import AthenaStack

app = core.App()
data_lake_stack = DataLakeStack(app)
common_stack = CommonStack(app)
kinesis_stack = KinesisStack(app, data_lake_raw_bucket=data_lake_stack.data_lake_raw_bucket)
dms_stack = DmsStack(app, common_stack=common_stack, data_lake_raw_bucket=data_lake_stack.data_lake_raw_bucket)
glue_catalog_stack = GlueCatalogStack(app, raw_data_lake_bucket=data_lake_stack.data_lake_raw_bucket,
                                      staged_data_lake_bucket=data_lake_stack.data_lake_raw_staged)
athena_stack = AthenaStack(app)
app.synth()

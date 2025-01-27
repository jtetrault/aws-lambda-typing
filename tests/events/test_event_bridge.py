from aws_lambda_typing.events import EventBridgeEvent


def test_cloud_watch_events_message_event() -> None:
    event: EventBridgeEvent = {
        "version": "0",
        "id": "fe8d3c65-xmpl-c5c3-2c87-81584709a377",
        "detail-type": "RDS DB Instance Event",
        "source": "aws.rds",
        "account": "123456789012",
        "time": "2020-04-28T07:20:20Z",
        "region": "us-east-2",
        "resources": ["arn:aws:rds:us-east-2:123456789012:db:rdz6xmpliljlb1"],
        "detail": {
            "EventCategories": ["backup"],
            "SourceType": "DB_INSTANCE",
            "SourceArn": "arn:aws:rds:us-east-2:123456789012:db:rdz6xmpliljlb1",
            "Date": "2020-04-28T07:20:20.112Z",
            "Message": "Finished DB Instance backup",
            "SourceIdentifier": "rdz6xmpliljlb1",
        },
    }

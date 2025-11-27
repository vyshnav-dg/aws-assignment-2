import cfnresponse
import boto3

def handler(event, context):
    request_type = event["RequestType"]
    if request_type == "Delete":
        # gracefully handle delete of custom Resource
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
        return
    try:
        vpc_id = event["ResourceProperties"]["VpcId"]
        client = boto3.client("ec2")
        resp = client.describe_vpcs(VpcIds=[vpc_id])
        if resp['Vpcs']:
            to_send = {"CidrBlock": resp["Vpcs"][0]["CidrBlock"]}
            cfnresponse.send(event, context, cfnresponse.SUCCESS, to_send)
        else:
            cfnresponse.send(event, context, cfnresponse.FAILED, {"error": f"VPC with id {vpc_id} not found"})
    except Exception as e:
        cfnresponse.send(event, context, cfnresponse.FAILED, {'error': str(e)})
        raise e

from src.config import get_ec2_client

def create_instance():
    ec2 = get_ec2_client()

    response = ec2.run_instances(
        ImageId="ami-0c02fb55956c7d316",  # Ubuntu (exemplo)
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1,
        KeyName="minha-chave-ssh",
        SecurityGroupIds=["sg-xxxxxxxx"],
    )

    instance_id = response["Instances"][0]["InstanceId"]
    print("Instância criada:", instance_id)
    return instance_id

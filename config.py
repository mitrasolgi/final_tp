"""
configurations.py

This module defines configuration parameters for AWS and MySQL, including security credentials,
server IPs, and database details.

AWS Configuration:
    - security_group_name: The name of the AWS security group.
    - key_name: The name of the AWS key pair.
    - key_path: The path to the private key file.
    - region_name: The AWS region name.
    - aws_access_key_id: The AWS access key ID.
    - aws_secret_access_key: The AWS secret access key.
    - aws_session_token: The AWS session token.

AWS Instances:
    - MASTER_NODE_IP: IP address of the master node.
    - SLAVE_NODES_IPS: List of IP addresses for slave nodes.
    - PROXY_SERVER_IP: IP address of the proxy server.
    - PROXY_SERVER_INSTANCE_TYPE: Instance type for the proxy server.

MySQL Configuration:
    - MASTER_DB_HOST: Hostname or IP address of the master database.
    - MASTER_DB_USER: Username for the master database.
    - MASTER_DB_PASSWORD: Password for the master database.
    - MASTER_DB_DATABASE: Name of the master database.

    - SLAVE_DB_USER: Username for the slave databases.
    - SLAVE_DB_PASSWORD: Password for the slave databases.
    - SLAVE_DB_DATABASE: Name of the slave databases.

    - PROXY_DB_USER: Username for the proxy database.
    - PROXY_DB_PASSWORD: Password for the proxy database.
    - PROXY_DB_DATABASE: Name of the proxy database.
"""
security_group_name='FP'
key_name='vockey'
key_path='vockey.pem'
region_name = 'us-east-1'
aws_access_key_id='ASIAZKEDGPGAJDYMQSVU'
aws_secret_access_key='8HkD5U0qZNU5I4gH08MxI4KLuCTdjgIXRy65Nh6W'
aws_session_token='FwoGZXIvYXdzEBoaDLDOyMDxWq3xbU3PEyLHAUrRTotQUC8OMrxq7fZpqMHFX1ViSkuv45MD/BVwerAA7p2t3JU2cD67Oynwt/LU2KzPxZGZGwjOV1ulPr+Ob/qzKEn14e7FMTK8aoTcYOw5Hyvm/ESM2YmZoH30CK42qDTe1r1CZ1DH3WaraE3Z3rt4YEMMQdh5VoxNeRvDXBeiP16oT+lyq3g7WDnjvSVuIX0o4sOINO8NxGNHQIvGGRAUQXcYAnkwbfon037gwVanKVHxSJJ9Vj8EVKhRq6iTlqBUPF7kHe0o/vmrrAYyLa/KKzrivSRXtB/yPUxFRqOH5joOt1rBUKENJ7J+RsP9/vr2kTbp1UE7yPfEgg=='
class AWSConfig:
    MASTER_NODE_IP = "50.17.104.45"
    SLAVE_NODES_IPS = ["54.226.235.123", "34.228.70.150", "52.55.169.12"]
    PROXY_SERVER_IP = "54.83.121.193"
    PROXY_SERVER_INSTANCE_TYPE = "t2.large"

class MySQLConfig:
    MASTER_DB_HOST = AWSConfig.MASTER_NODE_IP
    MASTER_DB_USER = "myapp"
    MASTER_DB_PASSWORD = "1234Fa$$"
    MASTER_DB_DATABASE = "test_database"

    SLAVE_DB_USER = "myapp"
    SLAVE_DB_PASSWORD = "1234Fa$$"
    SLAVE_DB_DATABASE = "test_database"

    PROXY_DB_USER = "myapp"
    PROXY_DB_PASSWORD = "1234Fa$$"
    PROXY_DB_DATABASE = "test_database"
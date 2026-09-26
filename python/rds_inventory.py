import boto3
import json
import pymysql
import os

# AWS configuration
REGION = os.environ.get("AWS_REGION", "us-east-1")
SECRET_ID = os.environ["RDS_SECRET_ID"]

# RDS configuration
RDS_HOST = os.environ["RDS_HOST"]
DATABASE = os.environ.get("RDS_DATABASE", "terraformdb")


def get_database_credentials():
    """Retrieve database credentials securely from AWS Secrets Manager."""

    client = boto3.client(
        "secretsmanager",
        region_name=REGION
    )

    response = client.get_secret_value(
        SecretId=SECRET_ID
    )

    return json.loads(response["SecretString"])


def connect_to_database(credentials):
    """Connect to the private RDS MySQL database."""

    return pymysql.connect(
        host=RDS_HOST,
        user=credentials["username"],
        password=credentials["password"],
        database=DATABASE,
        port=3306
    )


def main():

    print("Retrieving credentials from AWS Secrets Manager...")

    credentials = get_database_credentials()

    print("Connecting to private RDS database...")

    connection = connect_to_database(credentials)

    try:
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM server_inventory")

            rows = cursor.fetchall()

            print("\nServer Inventory")
            print("----------------")

            for row in rows:
                print(row)

    finally:
        connection.close()

    print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()

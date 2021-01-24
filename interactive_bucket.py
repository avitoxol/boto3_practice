import boto3
import sys

aws_mgt = boto3.session.Session(profile_name = "s3_user")
s3_cli = aws_mgt.client(service_name = "s3", region_name = "us-east-1")

print("Welcome to this script, what action would you like to perform")
action = input("Create/Delete/List/Exit ?: ")

while True:

    if action.lower() == "create":
        bucket_name = input("Please provide a unique bucket name?: ")
        print("your bucket name will be", bucket_name)
        print("###############################################################################")
        print("")
        print("permissions: 'private'|'public-read'|'public-read-write'|'authenticated-read' ")
        perm_rights = input("What kind of permissions should the bucket have?: ")
        s3_cli.create_bucket(
                ACL = perm_rights.lower(),
                Bucket = bucket_name.lower(),
                )
        earu_illuvatar = input("Would you like to continue creation? Y/N ")
        if earu_illuvatar.lower() == 'n':
            break

    elif action.lower() == "list":
    #    list_buckets()
        print("#################")
        response = s3_cli.list_buckets(Buckets = ['Name'])
        for name in response['Buckets']:
            print(name['Name'])
        break 

    elif action.lower() == "delete":
        print("I have become death")
        delete_bucket = input("Please provide bucket name for deletion: ")
        s3_cli.delete_bucket(
                Bucket = delete_bucket,
                )
        delete_more = input("Would you like to destroy more? Y/N ")
        if delete_more.lower() == 'n':
            break
    else:
        print("Hasta la vista")
        break

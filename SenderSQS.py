import boto3
########################################INITIALIZE CONNECTION TO AWS VIA BOTO3 'CLIENT'#############################################
client = boto3.resource('sqs',aws_access_key_id='AKIAWO7IBCXAC5DJX272',aws_secret_access_key='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' ,region_name='us-east-1')
accthttp='https://us-east-1.queue.amazonaws.com/444478854592/'
print("##########################################")
print("AVAILABLE QUEUES : URLS")
#The response is NOT a resource, but gives you a message ID and MD5
for queue in client.queues.all():
    print(queue.url)
###INPUT THE IAM CREDENTIALS WITH PERMISSIONS TO THE AWS ACCOUNT444478854592 AND RESOURCE YOU'RE TRYING TO ACCESS.
def sendersqs(message,x='0'):
    store2 = 'Queue.fifo'  # input()
    url = accthttp + str(store2)
    store3 = message
    client.Queue(url=url).send_message(
        MessageBody=store3, MessageGroupId=x, MessageDeduplicationId=x)
    print('sent Message',message)

if __name__ == '__main__':
   import sys
   sendersqs(sys.argv[1],sys.argv[2])
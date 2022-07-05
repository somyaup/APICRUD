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
def deletesqs():
    store2 = 'Queue.fifo'  # input()
    url = accthttp + str(store2)
    receipt = client.Queue(url=url).receive_messages()
    print(receipt)
    for message in receipt:
        print(message.body)
        print(message)
        message.delete(QueueUrl=url, ReceiptHandle=message.receipt_handle)
        print("this message has been deleted.")
if __name__ == '__main__':
   import sys
   deletesqs(message)
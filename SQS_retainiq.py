import boto3
########################################INITIALIZE CONNECTION TO AWS VIA BOTO3 'CLIENT'#############################################
client = boto3.resource('sqs',aws_access_key_id='AKIAWO7IBCXAC5DJX272',aws_secret_access_key='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' ,region_name='us-east-1')


accthttp='https://us-east-1.queue.amazonaws.com/444478854592/'

###INPUT THE IAM CREDENTIALS WITH PERMISSIONS TO THE AWS ACCOUNT444478854592 AND RESOURCE YOU'RE TRYING TO ACCESS.


#
#
################################################CREATE SQS-QUEUES IN THE CLIENT-CONNECTED ACCOUNT##########################################
# response = client.create_queue(
#      QueueName='MyQueue'
# )
# # print(response)

print("##########################################")
print("AVAILABLE QUEUES : URLS")

#The response is NOT a resource, but gives you a message ID and MD5
for queue in client.queues.all():
    print(queue.url)
#
print("##########################################")
########################################################SQS SEND OR RECEIVE###############################################
while True:
    print("Would You Like to : 1) Send a Message 2) Receive a Message 3:) Exit Program ?")
    store = input()
    ####################################SEND A MESSAGE##############################################
    if int(store) == 1:
        print("Please Input the NAME of the QUEUE to send a message to:")
        store2 = 'Queue.fifo'#input()
        url = accthttp+str(store2)
        print("Please Input the Message")
        store3 = input()
        x='0'
        client.Queue(url=url).send_message(
            MessageBody=store3,MessageGroupId=x,MessageDeduplicationId =x)
     ###############################################################################################
    #####################################READ AND DELETE MESSAGES###################################
    if int(store) == 2:
        print("Please Input the NAME of the QUEUE read a message from:")
        store2 = 'Queue.fifo'
        #store2 = input()
        url = accthttp + str(store2)
        # receipt = client.Queue(url=url).receive_messages()
        # receipt1 = client.Queue(url=url).receive_messages()
        receipt = client.Queue(url=url).receive_messages()
        # print(receipt)
        for message in receipt:
            print(message.body)
            print(message)
            message.delete(QueueUrl=url, ReceiptHandle=message.receipt_handle)
            print("this message has been deleted.")
    if int(store) == 3:
        break




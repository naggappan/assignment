import boto3
import botocore
import sys
import requests
from multiprocessing import Process


def s3_object(url):
    bucket_name = url.split('/')[2]
    key = url.split('/')[3]
    s3 = boto3.resource('s3')

    try:
        print ("Downloading s3 object")
        s3.Bucket(bucket_name).download_file(key,key)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            print (e)

def http_object(url):
    file_name = url.split('/')[-1]
    req = requests.get(url)
    file = open(file_name, 'wb')
    print ("Downloading http object")
    for chunk in req.iter_content(100000):
        file.write(chunk)
    file.close()

if __name__ == "__main__":
    functions = {'s3': s3_object,'http':http_object, 'https':http_object}
    url_no = len(sys.argv)
    jobs = []
    for i in range(1,url_no):
        url = sys.argv[i]
        protocol = url.split('/')[0][:-1]
        if protocol in functions.keys():
            p = Process(target=functions[protocol], args=(url,))
            jobs.append(p)
            p.start()
        else:
            print("Protocol not implemented yet")

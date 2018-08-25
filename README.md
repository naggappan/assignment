# Create aws credentials file in below bath

    ~/.aws/config 

# Setup virtual environment as below & install required dependencies

    python3.6 -m venv venv
    pip install -r requirements.txt

# Execute the code as below example to download multiple files in parallel
    
    python downloader.py http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud-1603.qcow2.xz http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud-1503.qcow2.xz http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud-1605.qcow2.xz s3://glovo-public/systems-engineer-interview-1.0-SNAPSHOT.jar



# Steps to add a new protocol like s3 or http

   Add a new function to support the download based on the protocol
   add the function to the dictionary value in the given code downloader.py

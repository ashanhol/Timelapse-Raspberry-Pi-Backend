from azure.storage.blob import BlobService
import subprocess 
import uuid

print("debug")


blob_service = BlobService(account_name='{PUT YOUR ACCOUNT NAME HERE}', account_key='{PUT YOUR ACCOUNT KEY HERE}')

blob_service.create_container('mycontainer', x_ms_blob_public_access='container')
while True: 
	subprocess.call(['./campic.sh'])

	image="/home/pi/webcam/image.jpg"

	blob_service.put_block_blob_from_path(
		'mycontainer',
    		uuid.uuid1(),
    		image,
    		x_ms_blob_content_type='image/jpg'
	)


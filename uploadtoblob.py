from azure.storage.blob import BlobService
import subprocess 
import uuid

print("debug")

blob_service = BlobService(account_name='frickimages', account_key='xmQhvZyBj5mswE0Pk5Bk2VjHli1R3FXWCWqA4ALvbheCAXtoVEu+l2RC3JLeCSREYX17N7SsUUJtkM8kSx4erg==')


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


from google.cloud import storage
from google.oauth2 import service_account
from datetime import datetime, timedelta

def upload_file(bucket_name, source_file_name, destination_blob_name, credentials_path):
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    storage_client = storage.Client(credentials=credentials)

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} berhasil diunggah ke {destination_blob_name} di bucket {bucket_name}.")

def get_download_url(bucket_name, file_name, credentials_path):
    storage_client = storage.Client.from_service_account_json(credentials_path)

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_name)

    url = blob.generate_signed_url(
        version="v4",
        expiration= datetime.utcnow() + timedelta(days=7),
        method="GET"
    )

    return url


bucket_name = "surveyasia"
source_file_name = "coba.txt"
destination_blob_name = "coba.txt"
credentials_path = "service.json"
print(get_download_url(bucket_name, source_file_name, credentials_path))

# upload_file(bucket_name, source_file_name, destination_blob_name, credentials_path)


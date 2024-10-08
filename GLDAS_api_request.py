import os
import requests
import pandas as pd
import numpy as np
# Function to download GLDAS data using a token
def download_gldas_data_with_token(url, token, output_dir):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Stream the download and save it to the local machine
    response = requests.get(url, headers=headers, stream=True)
    
    if response.status_code != 200:
        raise Exception(f"Failed to download: {response.status_code} {response.text}")
    
    filename = os.path.join(output_dir, url.split("/")[-1])  # Get the file name from the URL
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    print(f"Downloaded: {filename}")
    return filename

# Main section to download a specific GLDAS file
if __name__ == "__main__":
    # GLDAS file URL (replace with the specific URL for the file you want)
    gldas_url = "https://data.gesdisc.earthdata.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.0/1948/001/GLDAS_NOAH025_3H.A19480101.0600.020.nc4"
    #gldas_url = "https://data.gesdisc.earthdata.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.0/1948/001/GLDAS_NOAH025_3H.A19480101.0900.020.nc4 https://data.gesdisc.earthdata.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.0/1948/001/GLDAS_NOAH025_3H.A19480101.1200.020.nc4"
    # Your Bearer token (ensure you replace this with your actual token)
    access_token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6ImRpZWdvZ3VlcnJlcm8xIiwiZXhwIjoxNzMzMzYwMzc1LCJpYXQiOjE3MjgxNzYzNzUsImlzcyI6Imh0dHBzOi8vdXJzLmVhcnRoZGF0YS5uYXNhLmdvdiJ9.TmIuUHjh09O0deby2jtn8CCLCPwaJU7QieDWIXxf-29wWlDbsHgRMNXzth-wJZBhuSBigVqlfKJRQi6sbv-VB3rxcWCLuy9MFQN2NlnxCJgQPUkXY-TAPnDmKaVTKUFqoAMvuyAKhPtGAOrDhmTYymLkGctYBOxDBisT3G3UFWu6Bs1fK27Yw8yFC0u6NbyiCBuyTEQFNEWnqxee78q9uUO_qauNPkzoJ5_6I1SuwX5ANQf9zgputvKI7tbi8S3ZnxKQVXnjzcDZG-y-UVRFZr1-BijyziMh1HtlbPb1lOrPc0zgzB5gTswrpHKn92VT5X7a0t_mPU09Nzp0CsRWZA"
    
    links = pd.read_csv('~/Documents/UNAM/9TH-SEMESTER/SpaceApps/links.csv')
    links = links.to_numpy()
    print(np.shape(links))
    print(links[0,0])
    # Directory to save the downloaded file
    output_dir = "/home/guerrero/Documents/UNAM/9TH-SEMESTER/SpaceApps/gldas_data"
    
    # Ensure the directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Download the file
    #galdas_op = open("/home/Downloads/subset_GLDAS_NOAH025_3H_2.0_20241006_005351_.txt")
    for i in range(len(links)): 
        downloaded_file = download_gldas_data_with_token(links[i,0], access_token, output_dir)


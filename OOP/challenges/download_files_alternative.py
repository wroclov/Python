import os
import re
import urllib.parse
import urllib.request

def download_files(first_url, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    # Split the URL into head and tail parts
    url_head, url_tail = os.path.split(first_url)

    # Find the numeric part of the filename
    match = re.search(r'(\d+)', url_tail)
    if match:
        first_index = match.group(0)  # This captures the numeric part
        zero_padding_length = len(first_index)  # Get length of the original number for zero padding
    else:
        print("No numeric index found in the URL.")
        return

    index_count, error_count = 0, 0

    while error_count < 5:
        next_index = str(int(first_index) + index_count).zfill(zero_padding_length)  # Maintain zero padding
        next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))

        try:
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            urllib.request.urlretrieve(next_url, output_file)
            print(f"Successfully downloaded {os.path.basename(next_url)}")
            index_count += 1  # Increment index only if download is successful
        except (IOError, urllib.error.HTTPError) as e:
            print(f"Could not retrieve {next_url}: {e}")
            error_count += 1  # Increase error count on failure

# Example usage
first_url = 'http://699340.youcanlearnit.net/image001.jpg'
output_dir = r'C:\python_tmp\pictures_downloaded'

download_files(first_url, output_dir)

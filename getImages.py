from imutils import paths
import requests
import os

text_file_name = "zhuanshu.txt"
outputDir = "zhuanshu"
# grab the list of URLs from the input file, then initialize the
# total number of images downloaded thus far
rows = open(text_file_name).read().strip().split("\n")
total = 0

# loop the URLs
for url in rows:
	try:
		# try to download the image
		r = requests.get(url, timeout=60)

		# save the image to disk
		p = os.path.sep.join(outputDir, "{}.jpg".format(str(total).zfill(8)))
		f = open(p, "wb")
		f.write(r.content)
		f.close()

		# update the counter
		print("[INFO] downloaded: {}".format(p))
		total += 1

	# handle if any exceptions are thrown during the download process
	except:
		print("[INFO] error downloading {}...skipping".format(url))

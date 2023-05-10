import requests
import base64
from jaseci.jsorc.live_actions import jaseci_action

API_TOKEN="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"
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


# You can access the image with PIL.Image for example

@jaseci_action(act_group=["text-to-image"],allow_remote=True)
def generate(txt):
	payload={
		"input":txt
    }
	response = requests.post(API_URL, headers=headers, json=payload)
	image_bytes=response.content
	image_bytes=base64.b64encode(image_bytes).decode("utf-8")
	return image_bytes


	

	
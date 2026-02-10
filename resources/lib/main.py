from codequick import Route, Listitem, run, Script, utils
from resources.lib.endpoints import Endpoints
import simplejson as json
import requests
        
@Route.register
def root(plugin):
    resp = requests.get(Endpoints.NAVIGATION.format(language="es_ES"))

    if resp.status_code == 200:
        root_elem = json.loads(resp.text)

        # Parse each category
        for elem in root_elem["items"]:
            item = Listitem()

            # The image tag contains both the image url and title
            # img = elem.find(".//img")

            # Set the thumbnail image
            # item.art["thumb"] = img.get("src")

            # Set the title
            item.label = elem["name"]

            # Fetch the url
            # url = elem.find("div/a").get("href")

            # This will set the callback that will be called when listitem is activated.
            # 'video_list' is the route callback function that we will create later.
            # The 'url' argument is the url of the category that will be passed
            # to the 'video_list' callback.
            # item.set_callback(video_list, url=url)

            # Return the listitem as a generator.
            yield item
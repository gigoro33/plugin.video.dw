from codequick import Route, Listitem, run, Script, utils
from resources.lib.EndPoints import EndPoints
from resources.lib.OnDemand import OnDemand
import simplejson as json
import requests
        
@Route.register
def root(plugin):
    language_id = 28
    resp = requests.get(EndPoints.NAVIGATION.format(language="es_ES"))

    if resp.status_code == 200:
        root_elem = json.loads(resp.text)

        # Parse each category
        for elem in root_elem["items"]:
            if elem["type"] == "ProgramGroups":
                item = Listitem()

                # The image tag contains both the image url and title
                # img = elem.find(".//img")

                # Set the thumbnail image
                # item.art["thumb"] = img.get("src")

                # Set the title
                item.label = elem["name"]

                item.set_callback(OnDemand.get_topics, language_id=language_id)

                # Return the listitem as a generator.
                yield item
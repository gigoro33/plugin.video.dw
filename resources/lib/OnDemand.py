from codequick import Route, Listitem, run, Script, utils, Resolver
from resources.lib.EndPoints import EndPoints
import simplejson as json
import requests

class OnDemand:
    @Route.register
    def get_topics(plugin, language_id):
        item = Listitem()
        item.label = "Todos los programas"
        item.set_callback(OnDemand.get_program_list, language_id=language_id)
        yield item

        resp = requests.get(EndPoints.TOPICS.format(language_id=language_id))

        if resp.status_code == 200:
            topics = json.loads(resp.text)
            for topic in topics:
                item = Listitem()

                # The image tag contains both the image url and title
                # img = elem.find(".//img")

                # Set the thumbnail image
                # item.art["thumb"] = img.get("src")

                # Set the title
                item.label = topic["name"]
 
                item.set_callback(OnDemand.get_program_list, language_id=language_id, programs_filter=topic.get("programIds"))

                # Return the listitem as a generator.
                yield item

    @Route.register
    def get_program_list(plugin, language_id, programs_filter=None):
        resp = requests.get(EndPoints.PROGRAM_LIST.format(language_id=language_id))

        if resp.status_code == 200:
            programs = json.loads(resp.text)
            programs_filter_set = set(programs_filter) if programs_filter else None
            for program in programs:
                if programs_filter_set is not None and program.get("id") not in programs_filter_set:
                    continue
                item = Listitem()

                # Set the thumbnail image
                sizes_image = program.get("image", {}).get("sizes", [])
                if sizes_image:
                    item.art["thumb"] = sizes_image[-1]["url"]
                
                sizes_background = program.get("backgroundImage", {}).get("sizes", [])
                if sizes_background:
                    item.art["fanart"] = sizes_background[-1]["url"]
                else:
                    item.art["fanart"] = sizes_image[-1]["url"]

                # Set the title
                item.label = program["name"]
                item.info["plot"] = program["teaser"]

                program_id = program["id"]
                item.set_callback(OnDemand.get_video_list, language_id=language_id, program_id=program_id)

                # Return the listitem as a generator.
                yield item

    @Route.register
    def get_video_list(plugin, language_id, program_id, page_number=1):
        resp = requests.get(EndPoints.VIDEO_LIST.format(program_id=program_id,language_id=language_id,page_number=page_number))

        if resp.status_code == 200:
            videos = json.loads(resp.text)
            for video in videos["items"]:
                
                item = Listitem()
                sizes_image = video.get("image", {}).get("sizes", [])
                if sizes_image:
                    item.art["thumb"] = sizes_image[-1]["url"]
                    item.art["fanart"] = sizes_image[-1]["url"]

                item.label = video["name"]
                item.info["plot"] = video["teaserText"]
                item.info["duration"] = video["duration"]
                item.info["date"] = video["displayDate"]

                video_id=video["reference"]["id"]
                item.set_callback(OnDemand.play_video, video_id=video_id)

                yield item

    @Resolver.register
    def play_video(plugin, video_id):
        resp = requests.get(EndPoints.VIDEO_DETAIL.format(video_id=video_id))

        if resp.status_code == 200:
            video = json.loads(resp.text)
            sources = (video.get("mainContent") or {}).get("sources") or []
            for s in sources:
                fmt = (s.get("format") or "").lower()
                if fmt == "hls":
                    return s.get("url")
            return None
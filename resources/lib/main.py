from codequick import Route, Listitem, run, Script, utils
from resources.lib.EndPoints import EndPoints
from resources.lib.OnDemand import OnDemand
import simplejson as json
import requests
import xbmcaddon
        
language_id = Script.setting["language"].upper()
addon = xbmcaddon.Addon()
_ = addon.getLocalizedString


@Route.register
def root(plugin):    
    # Shows
    item = Listitem()
    item.label = _(32009)
    item.set_callback(OnDemand.get_program_list, language_id=language_id,content_type="video")
    yield item

    # Podcast
    item = Listitem()
    item.label = _(32023)
    item.set_callback(OnDemand.get_program_list, language_id=language_id, content_type="audio")
    yield item
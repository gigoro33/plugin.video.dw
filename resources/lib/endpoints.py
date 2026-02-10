class Endpoints:
    BASE_URL = "https://api.dw.com/api"
    NAVIGATION = f"{BASE_URL}/navigation/{{language}}?product=smarttv&platform=androidtv"
    VIDEO_DETAILS = f"{BASE_URL}/detail/video/{{video_id}}"
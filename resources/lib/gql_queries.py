GET_SHOW_LIST = """
query getShowList($lang: Language!) {
  programsOverview(lang: $lang) {
    audioPrograms { ...ShowFields }
    videoPrograms { ...ShowFields }
  }
}
fragment ShowFields on UnifiedProgram {
  id
  name
  title
  teaser
  text
  isRtl
  mainContentImage { staticUrl }
  categories { originId name }
  namedUrl
  departments { name }
  trackingId
  trackingDate
  trackingTopicsCommaJoined
  language
}
"""

GET_SHOWS_EPISODES = """
query getShowEpisodes($keys: [ContentKeyInput]!, $amount: Int!) {
  __typename contents(keys: $keys) {
    __typename
    ... on UnifiedProgram {
      moreContentsFromUnifiedProgram(amount: $amount, types: [VIDEO, AUDIO]) {
        __typename
        ... on Audio {
          ... AudioFields
        }
        ... on Video {
          ... VideoFields
        }
      }
    }
  }
}

fragment VideoFields on Video {
  __typename id name title teaser duration posterImageUrl isRtl regions {
    __typename name regionCode countryCode
  }
  categories {
    __typename originId name
  }
  duration contentDate mainContentImage {
    __typename staticUrl
  }
  unifiedPrograms(amount: 1) {
    __typename id name autoDelivery mainContentImage {
      __typename staticUrl
    }
  }
  namedUrl departments {
    __typename name
  }
  trackingId trackingDate trackingTopicsCommaJoined trackingRegionsCommaJoined language subtitles {
    __typename language subtitleUrl
  }
}

fragment AudioFields on Audio {
  __typename id name title teaser duration posterImageUrl isRtl regions {
    __typename name regionCode countryCode
  }
  categories {
    __typename originId name
  }
  duration contentDate mainContentImage {
    __typename staticUrl
  }
  unifiedPrograms(amount: 1) {
    __typename id name autoDelivery mainContentImage {
      __typename staticUrl
    }
  }
  namedUrl departments {
    __typename name
  }
  trackingId trackingDate trackingTopicsCommaJoined trackingRegionsCommaJoined language
}
"""

GET_VIDEO_DETAILS = """
query getVideoDetails($id: Int!) {
  __typename content(id: $id) {
    __typename
    ... on Video {
      ... VideoFields hlsVideoSrc moreAvContentsByThematicFocusAndGlobal {
        __typename
        ... on Video {
          ... VideoFields
        }
      }
    }
    ... on Audio {
      ... AudioFields mp3Src
    }
  }
}

fragment VideoFields on Video {
  __typename id name title teaser duration posterImageUrl isRtl regions {
    __typename name regionCode countryCode
  }
  categories {
    __typename originId name
  }
  duration contentDate mainContentImage {
    __typename staticUrl
  }
  unifiedPrograms(amount: 1) {
    __typename id name autoDelivery mainContentImage {
      __typename staticUrl
    }
  }
  namedUrl departments {
    __typename name
  }
  trackingId trackingDate trackingTopicsCommaJoined trackingRegionsCommaJoined language subtitles {
    __typename language subtitleUrl
  }
}

fragment AudioFields on Audio {
  __typename id name title teaser duration posterImageUrl isRtl regions {
    __typename name regionCode countryCode
  }
  categories {
    __typename originId name
  }
  duration contentDate mainContentImage {
    __typename staticUrl
  }
  unifiedPrograms(amount: 1) {
    __typename id name autoDelivery mainContentImage {
      __typename staticUrl
    }
  }
  namedUrl departments {
    __typename name
  }
  trackingId trackingDate trackingTopicsCommaJoined trackingRegionsCommaJoined language
}
"""
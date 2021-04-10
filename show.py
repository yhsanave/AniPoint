import requests

class Show:
    # General Query that returns all necessary values for a show given its id
    query = '''query ($id: Int){
                            Media(type: ANIME, id: $id) {
                                id
                                title {
                                    english
                                    romaji
                                    native
                                }
                                description(asHtml: false)
                                season
                                seasonYear
                                studios(isMain: true) {
                                    nodes {
                                        name
                                    }
                                }
                                staff {
                                    edges {
                                        role
                                        node {
                                            name {
                                                full
                                            }
                                        }
                                    }
                                }
                                source
                                genres
                                duration
                                relations {
                                edges {
                                    relationType
                                    node {
                                        id
                                        title {
                                            english
                                        }
                                    }
                                }
                            }
                            siteUrl
                            coverImage{
                                medium
                            }
                        }
                    }'''
    
    #Dictionary of warning messages which are shown to the user if their flags are set
    warnMessages = {"noDirector": "Director not found", "noStudio": "Studio not found", "hasPrequel": "Prequel listed, please verify season", "episodeLength": "Episodes are not standard length", "shortDescription": "Description is short"}

    # Constructor
    def __init__(self, id: int):
        # Set default values for episode, subbed, dubbed, and gif path
        self.episode = "1"
        self.subbed = True
        self.dubbed = False
        self.gifPath = r".\default.gif"
        
        # Create dictionary of warning flags, all are False by default. Used to warn user about potential issues.
        self.warnings = {"noDirector": True, "noStudio": False, "hasPrequel": False, "episodeLength": False, "shortDescription": False}
        
        # API call using query, JSON response is converted into a dictionary
        self.data = requests.post("https://graphql.anilist.co", json={"query": Show.query, "variables": {"id": id}}).json()["data"]["Media"]
        
        # Parse response
        self.id = id
        
        # Get English title, or Romaji if english is none
        if self.data["title"]["english"] != None:
            self.titleENG = self.data["title"]["english"]
        else:
            self.titleENG = self.data["title"]["romaji"]

        self.titleJPN = self.data["title"]["native"]
        self.season = self.data["season"].capitalize() + f' {self.data["seasonYear"]}'
        self.source = self.data["source"].capitalize()
        self.duration = self.data["duration"]
        self.url = self.data["siteUrl"]
        self.cover = self.data["coverImage"]["medium"]

        # Description, discards everything after the first paragraph unless it is too short
        descParts = self.data["description"].replace("<br>\n", "<br>").replace("<br><br>","<br>").split("<br>")
        self.description = descParts.pop(0)
        while len(self.description) < 200:
            try:
                self.description += f" {descParts.pop(0)}"
            except IndexError:
                self.warnings["shortDescription"] = True
                break
        
        # Studio, sets warning flag if no studio is listed
        try:
            self.studio = self.data["studios"]["nodes"][0]["name"]
        except IndexError:
            self.studio = "Unknown"
            self.warnings["noStudio"] = True
        
        # Search through staff to find director, warn user if one is not found
        self.director = "Unknown"
        for i in self.data["staff"]["edges"]:
            if i["role"] == "Director":
                self.director = i["node"]["name"]["full"]
                self.warnings["noDirector"] = False
                break
            else:
                self.warnings["noDirector"] = True

        # Genres, if there are more than 3, use only the first 3
        self.genres = ""
        if len(self.data["genres"]) > 3:
            self.genres += f"{self.data['genres'][0]}, "
            self.genres += f"{self.data['genres'][1]}, "
            self.genres += f"{self.data['genres'][2]}"
        else:
            for i in self.data["genres"]:
                self.genres += f"{i}, "
            self.genres = self.genres[:-2]

        # Check for prequels and set warning if any exist
        for i in self.data["relations"]["edges"]:
            if i["relationType"] == "PREQUEL":
                self.warnings["hasPrequel"] = True
                break
        
        # Check if episodes are not standard length (20-30 minutes)
        if self.duration > 30 or self.duration < 20:
            self.warnings["episodeLength"] = True

    # Set the episode string (defined by user)
    def setEpisode(self, ep: str):
        self.episode = ep
        return self.episode

    # Toggle Subbed (defined by user)
    def toggleSub(self):
        self.subbed = not self.subbed
        return self.subbed

    # Toggle Dubbed (defined by user)
    def toggleDub(self):
        self.dubbed = not self.dubbed
        return self.dubbed

    # Set the path for the gif
    def setGifPath(self, path: str):
        self.gifPath = path
        return self.gifPath

    # Get warnings for a show as a list of relevant warning messages
    def warn(self):
        warnOut = ""
        for i in self.warnings.keys():
            if self.warnings[i]:
                warnOut += f"{Show.warnMessages[i]}\n"
        return warnOut[:-1]

    # Getters, self explanatory
    def getID(self):
        return self.id

    def getTitleENG(self):
        return self.titleENG

    def getTitleJPN(self):
        return self.titleJPN

    def getDescription(self):
        return self.description

    def getEpisode(self):
        return self.episode

    def getSeason(self):
        return self.season

    def getStudio(self):
        return self.studio

    def getSource(self):
        return self.source

    def getDirector(self):
        return self.director

    def getGenres(self):
        return self.genres

    def getWarnings(self):
        return self.warnings

    def getURL(self):
        return self.url

    def getSub(self):
        return self.subbed

    def getDub(self):
        return self.dubbed

    def getGifPath(self):
        return self.gifPath

    def getCoverUrl(self):
        return self.cover

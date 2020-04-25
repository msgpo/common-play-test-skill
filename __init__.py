from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
import re

class CPKodiSkill(CommonPlaySkill):
    def __init__(self):
        super(CPKodiSkill, self).__init__('Kodi Skill')
        self.regexes = {}

    def CPS_match_query_phrase(self, phrase):
        """ This method responds wether the skill can play the input phrase.
            The method is invoked by the PlayBackControlSkill.
            Returns: tuple (matched phrase(str),
                            match level(CPSMatchLevel),
                            optional data(dict))
                     or None if no match was found.
        """
        self.log.info('CPKodiSkill received the following phrase: ' + phrase)
        deviceID = "chromecast"
        chromecast_specified = deviceID in phrase
        phrase = re.sub(self.translate_regex(deviceID), '', phrase)
        match_level = CPSMatchLevel.MULTI_KEY
        match = self.specific_query(phrase)
        # If nothing was found check for a generic match
        if match == NOTHING_FOUND:
            match = self.generic_query(phrase)
            match_level = CPSMatchLevel.GENERIC

        self.log.info('CPKodiSkill match: {}'.format(match))
        self.log.info('CPKodiSkill matched the following: ' + match)
        if match == NOTHING_FOUND:
            self.log.debug('Nothing found on CPKodiSkill')
            return None
        else:
            return (phrase,
                    (CPSMatchLevel.EXACT if chromecast_specified else match_level),
                    {'playlist': match[0],
                     'playlist_type': match[2],
                     'library_type': match[3]
                     })

        return None

    def CPS_start(self, phrase, data):
        """ Starts playback.

            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        self.log.info('CPKodi Skill received the following phrase and Data: ' + phrase, data)
        pass

    def translate_regex(self, regex):
        if regex not in self.regexes:
            path = self.find_resource(regex + '.regex', 'dialog')
            if path:
                with open(path) as f:
                    string = f.read().strip()
                self.regexes[regex] = string
        return self.regexes[regex]

def create_skill():
    return CPKodiSkill()
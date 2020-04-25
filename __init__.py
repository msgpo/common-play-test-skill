from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
import re

class CPKodiSkill(CommonPlaySkill):
    def __init__(self):
        super(CPKodiSkill, self).__init__('CPKodiSkill')
        self.regexes = {}

    def CPS_match_query_phrase(self, phrase):
        """
            The method is invoked by the PlayBackControlSkill.
        """
        self.log.info('CPKodiSkill received the following phrase: ' + phrase)
        device_list = ['chromecast', 'kodi']
        for device_id in device_list:
            if device_id in phrase:
                match_level = CPSMatchLevel.EXACT
                playback_device = device_id
        data = {
            "track": "my Movie Name"
        }
        if match_level:
            return (phrase, match_level, data)
        else:
            return None

    def CPS_start(self, phrase, data):
        """ Starts playback.

            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        self.log.info('CPKodi Skill received the following phrase and Data: ' + phrase + ' ' + data['track'])
        pass


def create_skill():
    return CPKodiSkill()
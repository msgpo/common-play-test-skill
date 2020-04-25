from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel

class CPKodiSkill(CommonPlaySkill):
    def CPS_match_query_phrase(self, phrase):
        """ This method responds wether the skill can play the input phrase.
            The method is invoked by the PlayBackControlSkill.
            Returns: tuple (matched phrase(str),
                            match level(CPSMatchLevel),
                            optional data(dict))
                     or None if no match was found.
        """
        self.log.info('Checking CPKodi Skill received the following phrase: ' + phrase)

        return None

    def CPS_start(self, phrase, data):
        """ Starts playback.

            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        self.log.info('CPKodi Skill received the following phrase and Data: ' + phrase, data)
        pass


def create_skill():
    return CPKodiSkill()
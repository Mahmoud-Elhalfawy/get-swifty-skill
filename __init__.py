from mycroft import MycroftSkill, intent_file_handler


class GetSwifty(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('swifty.get.intent')
    def handle_swifty_get(self, message):
        self.speak_dialog('swifty.get')


def create_skill():
    return GetSwifty()


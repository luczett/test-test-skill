from mycroft import MycroftSkill, intent_file_handler


class TestTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.test.intent')
    def handle_test_test(self, message):
        day = message.data.get('day')
        answerday = ''

        self.speak_dialog('test.test', data={
            'day': day,
            'answerday': answerday
        })


def create_skill():
    return TestTest()


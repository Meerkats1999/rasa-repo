## happy path 1 (/tmp/tmp1csgu3li/c322348583f24e6abdc17ae12adc1e34_conversation_tests.md)
* greet: hello there!   <!-- predicted: None: hello there! -->
    - utter_greet
* mood_great: amazing   <!-- predicted: None: amazing -->
    - utter_happy


## happy path 2 (/tmp/tmp1csgu3li/c322348583f24e6abdc17ae12adc1e34_conversation_tests.md)
* greet: hello there!   <!-- predicted: None: hello there! -->
    - utter_greet
* mood_great: amazing   <!-- predicted: None: amazing -->
    - utter_happy
* goodbye: bye-bye!   <!-- predicted: None: bye-bye! -->
    - utter_goodbye


## sad path 1 (/tmp/tmp1csgu3li/c322348583f24e6abdc17ae12adc1e34_conversation_tests.md)
* greet: hello   <!-- predicted: None: hello -->
    - utter_greet
* mood_unhappy: not good   <!-- predicted: None: not good -->
    - utter_cheer_up
    - utter_did_that_help
* affirm: yes   <!-- predicted: None: yes -->
    - utter_happy


## sad path 2 (/tmp/tmp1csgu3li/c322348583f24e6abdc17ae12adc1e34_conversation_tests.md)
* greet: hello   <!-- predicted: None: hello -->
    - utter_greet
* mood_unhappy: not good   <!-- predicted: None: not good -->
    - utter_cheer_up
    - utter_did_that_help
* deny: not really   <!-- predicted: None: not really -->
    - utter_goodbye


## say goodbye (/tmp/tmp1csgu3li/c322348583f24e6abdc17ae12adc1e34_conversation_tests.md)
* goodbye: bye-bye!   <!-- predicted: None: bye-bye! -->
    - utter_goodbye


## bot challenge (/tmp/tmp1csgu3li/c322348583f24e6abdc17ae12adc1e34_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: None: are you a bot? -->
    - utter_iamabot



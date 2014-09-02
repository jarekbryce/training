import easygui
flavor = easygui.enterbox("What flavor of ice cream is your favorite?",
                           default = 'Vanilla')
easygui.msgbox ("You entered " + flavor)

import easygui
flavor = easygui.enterbox("What flavor of ice cream is your favorite?",
                           default = 'Valnilla')
easygui.msgbox ("You entered " + flavor)

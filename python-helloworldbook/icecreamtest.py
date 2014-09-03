import easygui
flavor = easygui.buttonbox("What is your favorite flavor of ice cream?",
                 choices = ('Vanilla', 'Chocolate', 'Strawberry') )

easygui.msgbox ("You picked " + flavor)

import easygui
flavor = easygui.choicebox("What is your favorite flavor of ice cream?",
                 choices = ('Vanilla', 'Chocolate', 'Strawberry') )

easygui.msgbox ("you picked " + flavor)

﻿screen say:
    window:
        id"window"
        has vbox:
            style"say_vbox"
        if who:
            text who id"who"
        text what id"what"
screen choice:
    window:
        style "menu_window"xalign.5 yalign.5
        vbox:
            style"menu"
            for caption, action, chosen in items:
                if action:
                    button:
                        action action
                        style"menu_choice_button"
                        text caption style"menu_choice"
                else:
                    text caption style"menu_caption"
screen input:
    pass
screen main_menu:
    image"kg.w"
    text"Три в ряд"style"mcnn"xalign.5 yalign.5
    imagebutton idle"#00000000"action Start()
screen navigation:
    pass
screen file_picker:
    pass
screen save:
    textbutton""action Preference("display","window")
    text"Пауза"style"mcnn"xalign.5 yalign.5
screen load:
    pass
screen preferences:
    pass
screen yesno_prompt:
    modal True
    timer.1 action(yes_action)
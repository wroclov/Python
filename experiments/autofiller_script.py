import pyautogui
import pyperclip
import time
import random

# for https://www.jetpunk.com/user-quizzes/1268665/save-the-humanity-by-guessing-countries

words = ["france", "uk", "spain","portugal","malta","monaco","vatican","san marino","liechtenstein","luxembourg",
        "ireland","iceland","norway","sweden","finland","denmark","estonia","latvia","lithuania","belarus",
         "russia","ukraine","moldova","romania","bulgaria","poland","germany","netherlands","belgium","switzerland",
         "czechia","slovakia","hungary","austria","croatia","serbia","slovenia","bosnia","albania","kosovo",
         "montenegro","macedonia","greece","italy","andorra",
         "georgia","armenia","azerbaijan","turkey","turkmenistan","kazakhstan",
         "uzbekistan","tajikistan","mongolia","north korea","south korea","japan","china","nepal","bhutan","taiwan",
         "philippines","vietnam","laos","cambodia","myanmar","thailand","indonesia","malaysia","brunei","timor leste",
         "bangladesh","pakistan","india","afghanistan","iran","iraq","syria","oman","yemen","uae","kuwait","qatar",
         "bahrain","israel","lebanon","jordan","saudi arabia","cyprus","maldives","sri lanka","singapore","kyrgyzstan",
         "egypt","libya","algeria","tunisia","morocco","mauritania","sudan","south sudan","ethiopia","eritrea","djibouti",
         "somalia","kenya","tanzania","uganda","rwanda","burundi","malawi","chad","niger","nigeria","burkina faso",
         "mali","senegal","gambia","guinea","guinea bissau","liberia","sierra leone","ghana","togo","benin","cameroon",
         "ivory coast","cape verde","sao tome","seychelles","madagascar","mauritius","comoros","mozambique","congo",
         "angola","namibia","south africa","swaziland","lesotho","botswana","zambia","zimbabwe","equatorial guinea",
         "central african republic","gabon",
         "brazil","argentina","bolivia","chile","uruguay","peru","paraguay","colombia","venezuela","ecuador",
         "suriname","guyana","mexico","usa","canada","panama","costa rica","nicaragua","el salvador","guatemala",
         "honduras","cuba","jamaica","haiti","belize","trinidad","antigua","saint lucia","saint kitts","saint vincent",
         "bahamas","barbados","dominica","dominican republic","grenada"
         "australia","papua new guinea","new zealand","solomon islands","vanuatu","nauru","palau","tuvalu","fiji",
         "samoa","tonga","kiribati","micronesia","marshall islands"
         ]

# it will cause problems with "guinea"
# random.shuffle(words)

# just to clear box content in case of old text stored there
# it is slow, as strip() function and others take some time
def read_box():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    #time.sleep(0.004)
    return pyperclip.paste().strip()

def clear_box():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

print("You have 3 seconds to click in the input box...")
time.sleep(3)

for w in words:
    pyautogui.typewrite(w)
    pyautogui.press("enter")
    # time.sleep(random.uniform(0.005,0.001))
    # Check if page cleared the box automatically
    #if read_box() != "":
        # Wrong word → manually clear
    #    clear_box()

print("Done!")
import gratient
import fade
import progressbar
import time
import os
os.system("title ۜ\(סּںסּَ` )/ۜ  Gratient And Fade Module Showcase!")

# Function to create
def animated_marker1():
	
	widgets = ['Loading Gradients: ', progressbar.AnimatedMarker()]
	bar = progressbar.ProgressBar(widgets=widgets).start()
	
	for i in range(10):
		time.sleep(0.1)
		bar.update(i)

def animated_marker():
	
	widgets = ['Loading Faded Text: ', progressbar.AnimatedMarker()]
	bar = progressbar.ProgressBar(widgets=widgets).start()
	
	for i in range(10):
		time.sleep(0.1)
		bar.update(i)

tex = """
    `7MMF'   `7MF'` 7MM"'"YMM   `7MN.   `7MF'      ma       `YMM'   `MP' 
      `MA     ,V     MM    `7     MMN.    M       ;MM:        VMb.  ,P   
       VM:   ,V      MM   d       M YMb   M      ,V^MM.        `MM.M'    
        MM.  M'      MMmmMM       M  `MN. M     ,M  `MM          MMb     
        `MM A'       MM   Y  ,    M   `MM.M     AbmmmqMA       ,M'`Mb.   
         :MM;        MM     ,M    M     YMM    A'     VML     ,P   `MM.  
          VF       .JMMmmmmMMM  .JML.    YM  .AMA.   .AMMA. .MM:.  .:MMa.

 [!] Please subscribe to my Github profile @venaxyt for more modules like this one.
 [!] Follow my Github profile (@pndaboi) for more amazing repos like this one!
"""
grad=""" ██████╗ ██████╗  █████╗ ████████╗██╗███████╗███╗   ██╗████████╗██╗
██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║██╔════╝████╗  ██║╚══██╔══╝██║
██║  ███╗██████╔╝███████║   ██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║
██║   ██║██╔══██╗██╔══██║   ██║   ██║██╔══╝  ██║╚██╗██║   ██║   ╚═╝
╚██████╔╝██║  ██║██║  ██║   ██║   ██║███████╗██║ ╚████║   ██║   ██╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝
                                                                   """
fade1= """███████╗ █████╗ ██████╗ ███████╗██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██║
█████╗  ███████║██║  ██║█████╗  ██║
██╔══╝  ██╔══██║██║  ██║██╔══╝  ╚═╝
██║     ██║  ██║██████╔╝███████╗██╗
╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝
                                   """
# Driver's code
gratient_text = gratient.purple(tex)
print(gratient_text)
print("")
text1 = ("Modules made by @venaxyt on Github And Program To Showcase Both Of @venaxyt's Modules Is By @pndaboi!")
gratient_text1 = gratient.purple(text1)
print(gratient_text1)
print("")
time.sleep(3)
animated_marker1()
print("")
print("")
print("Gradient Text: ")
print("")
gratient_banner = gratient.blue(grad)
print(gratient_banner)

gratient_text = gratient.black(grad)
print(gratient_text)

gratient_text = gratient.purple(grad)
print(gratient_text)

gratient_text = gratient.red(grad)
print(gratient_text)

gratient_text = gratient.yellow(grad)
print(gratient_text)
time.sleep(3)
# Driver's code
animated_marker()
print("")
print("")
print("Faded Text: ")
print("")

# Fading a ascii art text (black-white)
faded_text = fade.blackwhite(fade1)
print(faded_text)

# Fading a ascii art text (purple-pink)
faded_text = fade.purplepink(fade1)
print(faded_text)

# Fading a ascii art text (green-blue)
faded_text = fade.greenblue(fade1)
print(faded_text)

# Fading a ascii art text (darkblue-blue)
faded_text = fade.water(fade1)
print(faded_text)

# Fading a ascii art text (yellow-red)
faded_text = fade.fire(fade1)
print(faded_text)

# Fading a ascii art text (pink-red)
faded_text = fade.pinkred(fade1)
print(faded_text)

# Fading a ascii art text (purple-blue)
faded_text = fade.purpleblue(fade1)
print(faded_text)

# Fading a ascii art text (green-yellow)
faded_text = fade.brazil(fade1)
print(faded_text)

# Fading a ascii art text (random)
faded_text = fade.random(fade1)
print(faded_text)

print("")
text1 = ("Modules Made By @venaxyt on Github!")
gratient_text1 = gratient.purple(text1)
print(gratient_text1)
text1 = ("""Program To Showcase Both Of @venaxyt's Modules Is By @Pndaboi!

Follow my Github profile (@pndaboi) for more amazing repos like this one!""")
gratient_text1 = gratient.purple(text1)
print(gratient_text1)
print("")
text1 = ("Press Any Key To Exit!")
gratient_text1 = gratient.purple(text1)
input(gratient_text1)

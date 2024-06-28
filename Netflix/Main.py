import GuiMaker as gm
import Tests as test


test.showExecionTime()

guiMaker = gm.GuiMakerClass('https://www.dataquest.io/wp-content/uploads/2020/11/ViewingActivity-sample.csv')
guiMaker.create_gui()




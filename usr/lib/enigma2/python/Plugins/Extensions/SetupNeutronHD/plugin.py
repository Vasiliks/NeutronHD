# -*- coding: UTF-8 -*-
## SetupNeutronHD
## Coded by Sirius
##
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Components.Language import language
from Components.ConfigList import ConfigListScreen
from Components.config import config, ConfigYesNo, ConfigSubsection, getConfigListEntry, ConfigSelection
from Tools.Directories import fileExists
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_SKIN_IMAGE, SCOPE_LANGUAGE
from os import environ
from os import system
import gettext
import os

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("SetupNeutronHD", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/SetupNeutronHD/locale"))

def _(txt):
	t = gettext.dgettext("SetupNeutronHD", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

textcolor = [
	("#00f4f4f4", _("white")),
	("#00c0c0c0", _("lightgrey")),
	("#008f8f8f", _("grey")),
	("#00555555", _("darkgrey")),
	("#00ffff55", _("yellow")),
	("#00ffcc33", _("gold")),
	("#00ff80ff", _("pink")),
	("#00ff8000", _("orange")),
	("#00ff0000", _("red")),
	("#00800000", _("maroon")),
	("#00804000", _("brown")),
	("#0000ffff", _("aqua")),
	("#0080ff00", _("lime")),
	("#0000ff00", _("green")),
	("#00008000", _("darkgreen")),
	("#000099ff", _("skyblue")),
	("#000000ff", _("blue")),
	("#00000080", _("darkblue")),
	("#008080ff", _("glaucous")),
	("#00400080", _("purple"))]
style = [
	("white", _("white")),
	("grey", _("grey")),
	("yellow", _("yellow")),
	("red", _("red")),
	("green", _("green")),
	("aqua", _("aqua")),
	("skyblue", _("skyblue")),
	("purple", _("purple")),
	("blue", _("blue"))]
progresscolor = [
	("white", _("white")),
	("yellow", _("yellow")),
	("gold", _("gold")),
	("pink", _("pink")),
	("orange", _("orange")),
	("red", _("red")),
	("maroon", _("maroon")),
	("brown", _("brown")),
	("aqua", _("aqua")),
	("lime", _("lime")),
	("green", _("green")),
	("darkgreen", _("darkgreen")),
	("skyblue", _("skyblue")),
	("blue", _("blue")),
	("darkblue", _("darkblue")),
	("glaucous", _("glaucous")),
	("purple", _("purple"))]
dish = [
	("Dish-1", _("on left")),
	("Dish-2", _("on right"))]
scrollbarmode = [
	("showNever", _("no")),
	("showOnDemand", _("yes"))]
fonts = [
	("Roboto-Regular", _("regular")),
	("Roboto-Medium", _("medium")),
	("Roboto-Bold", _("bold")),
	("Roboto-Italic", _("italic")),
	("Roboto-MediumItalic", _("mediumitalic")),
	("Roboto-BoldItalic", _("bolditalic"))]

if fileExists("/usr/lib/enigma2/python/Components/Converter/AlwaysTrue.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/CaidInfo2.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/CamdInfo3.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/ConverterRotator.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/EventName2.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/FrontendInfo2.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/ProgressDiskSpaceInfo.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/RouteInfo.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/RWeather.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceInfoEX.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceName2.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Renderer/PiconUni.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Renderer/RendVolumeText.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Renderer/Watches.py"):
	numberchannel = [
		("TemplatesInfoBarNumber1", _("no")),
		("TemplatesInfoBarNumber2", _("yes"))]
	styleinfobar = [
		("TemplatesInfoBarTvPicon", _("default")),
		("TemplatesInfoBarTvPiconProv", _("picon provider")),
		("TemplatesInfoBarTvPiconSat", _("picon sattelite")),
		("TemplatesInfoBarTvPiconProvSat", _("picon provider, picon sattelite")),
		("TemplatesInfoBarTvPiconTuner", _("tuner")),
		("TemplatesInfoBarTvPiconProvTuner", _("picon provider, tuner")),
		("TemplatesInfoBarTvPiconSatTuner", _("picon sattelite, tuner")),
		("TemplatesInfoBarTvPiconProvSatTuner", _("picon provider, picon sattelite, tuner")),
		("TemplatesInfoBarTvPiconAnalogTuner", _("analog tuner")),
		("TemplatesInfoBarTvPiconProvAnalogTuner", _("picon provider, analog tuner")),
		("TemplatesInfoBarTvPiconSatAnalogTuner", _("picon sattelite, analog tuner")),
		("TemplatesInfoBarTvPiconProvSatAnalogTuner", _("picon provider, picon sattelite, analog tuner"))]
	technicalinfobar = [
		("TemplatesInfoBarTechnical1", _("no")),
		("TemplatesInfoBarTechnical2", _("pid")),
		("TemplatesInfoBarTechnical3", _("ecm, caids")),
		("TemplatesInfoBarTechnical4", _("crypt, ecm, camd"))]
	ecmepgpanel = [
		("TemplatesInfoBarEcmEpg1", _("no")),
		("TemplatesInfoBarEcmEpg2", _("ecm centre")),
		("TemplatesInfoBarEcmEpg3", _("ecm right")),
		("TemplatesInfoBarEcmEpg4", _("ecm left")),
		("TemplatesInfoBarEcmEpg5", _("epg centre")),
		("TemplatesInfoBarEcmEpg6", _("epg right")),
		("TemplatesInfoBarEcmEpg7", _("epg left")),
		("TemplatesInfoBarEcmEpg8", _("ecm centre, epg centre")),
		("TemplatesInfoBarEcmEpg9", _("ecm right, epg left")),
		("TemplatesInfoBarEcmEpg10", _("ecm left, epg right"))]
	epgchannelselection = [
		("TemplatesChannelSelectionInfoEPG1", _("no")),
		("TemplatesChannelSelectionInfoEPG2", _("now")),
		("TemplatesChannelSelectionInfoEPG3", _("now, next")),
		("TemplatesChannelSelectionInfoEPG4", _("9 programs"))]
	infochannelselection = [
		("TemplatesChannelSelectionInfoChannel1", _("no")),
		("TemplatesChannelSelectionInfoChannel2", _("picons")),
		("TemplatesChannelSelectionInfoChannel3", _("channel info")),
		("TemplatesChannelSelectionInfoChannel4", _("picon channel, channel info")),
		("TemplatesChannelSelectionInfoChannel5", _("picon channel, picon provider, channel info")),
		("TemplatesChannelSelectionInfoChannel6", _("picon channel, picon provider, picon sattelite, channel info"))]
	clockpanel = [
		("TemplatesClock1", _("no")),
		("TemplatesClock2", _("12:00")),
		("TemplatesClock3", _("saturday, 01 january 12:00")),
		("TemplatesClock4", _("saturday, 01.01.2010 12:00"))]
else:
	numberchannel = [
		("TemplatesInfoBarNumber1", _("no"))]
	styleinfobar = [
		("TemplatesInfoBarTvPicon", _("default")),
		("TemplatesInfoBarTvPiconTuner", _("tuner"))]
	technicalinfobar = [
		("TemplatesInfoBarTechnical1", _("no"))]
	ecmepgpanel = [
		("TemplatesInfoBarEcmEpg1", _("no")),
		("TemplatesInfoBarEcmEpg5", _("epg centre")),
		("TemplatesInfoBarEcmEpg6", _("epg right")),
		("TemplatesInfoBarEcmEpg7", _("epg left"))]
	epgchannelselection = [
		("TemplatesChannelSelectionInfoEPG1", _("no")),
		("TemplatesChannelSelectionInfoEPG2", _("now"))]
	infochannelselection = [
		("TemplatesChannelSelectionInfoChannel1", _("no")),
		("TemplatesChannelSelectionInfoChannel2", _("picons"))]
	clockpanel = [
		("TemplatesClock1", _("no"))]
if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/TMBD/plugin.pyo")\
	and fileExists("/usr/lib/enigma2/python/Components/Renderer/RatingTmbd.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Renderer/CoverTmbd.py"):
	coverinfopanel = [
	("TemplatesInfoBarInfoMovieCover1", _("no")),
	("TemplatesInfoBarInfoMovieCover2", _("poster")),
	("TemplatesInfoBarInfoMovieCover3", _("poster, description"))]
	infomovieselection =[
	("TemplatesMovieSelectionInfoMovie1", _("no")),
	("TemplatesMovieSelectionInfoMovie3", _("standard")),
	("TemplatesMovieSelectionInfoMovie4", _("TMDB plugin"))]
else:
	coverinfopanel = [
	("TemplatesInfoBarInfoMovieCover1", _("no"))]
	infomovieselection =[
	("TemplatesMovieSelectionInfoMovie1", _("no")),
	("TemplatesMovieSelectionInfoMovie2", _("standard"))]
if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/Calendar/plugin.pyo")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/CalendarToText.py")\
	and fileExists("/usr/lib/enigma2/python/Plugins/Extensions/WeatherMSN/plugin.pyo")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/MSNWeather2.py"):
	otherinfobar = [
	("TemplatesInfoBarOther1", _("no")),
	("TemplatesInfoBarOther2", _("rambler weather")),
	("TemplatesInfoBarOther3", _("msn weather")),
	("TemplatesInfoBarOther4", _("msn weather full")),
	("TemplatesInfoBarOther5", _("calendar")),
	("TemplatesInfoBarOther6", _("rambler weather, calendar")),
	("TemplatesInfoBarOther7", _("msn weather, calendar")),
	("TemplatesInfoBarOther8", _("msn weather full, calendar"))]
elif fileExists("/usr/lib/enigma2/python/Plugins/Extensions/Calendar/plugin.pyo")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/CalendarToText.py"):
	otherinfobar = [
	("TemplatesInfoBarOther1", _("no")),
	("TemplatesInfoBarOther2", _("rambler weather")),
	("TemplatesInfoBarOther5", _("calendar")),
	("TemplatesInfoBarOther6", _("rambler weather, calendar"))]
elif fileExists("/usr/lib/enigma2/python/Plugins/Extensions/WeatherMSN/plugin.pyo")\
	and fileExists("/usr/lib/enigma2/python/Components/Converter/MSNWeather2.py"):
	otherinfobar = [
	("TemplatesInfoBarOther1", _("no")),
	("TemplatesInfoBarOther2", _("rambler weather")),
	("TemplatesInfoBarOther3", _("msn weather")),
	("TemplatesInfoBarOther4", _("msn weather full"))]
else:
	otherinfobar = [
	("TemplatesInfoBarOther1", _("no")),
	("TemplatesInfoBarOther2", _("rambler weather"))]

config.skin.neutron = ConfigSubsection()
config.skin.neutron.style = ConfigSelection(default="grey", choices = style)
config.skin.neutron.numberchannel = ConfigSelection(default="TemplatesInfoBarNumber1", choices = numberchannel)
config.skin.neutron.styleinfobar = ConfigSelection(default="TemplatesInfoBarTvPiconTuner", choices = styleinfobar)
config.skin.neutron.technicalinfobar = ConfigSelection(default="TemplatesInfoBarTechnical1", choices = technicalinfobar)
config.skin.neutron.stylesecondinfobar = ConfigSelection(default="TemplatesInfoBarTvPiconTuner", choices = styleinfobar)
config.skin.neutron.technicalsecondinfobar = ConfigSelection(default="TemplatesInfoBarTechnical1", choices = technicalinfobar)
config.skin.neutron.ecmepgpanel = ConfigSelection(default="TemplatesInfoBarEcmEpg5", choices = ecmepgpanel)
config.skin.neutron.epgchannelselection = ConfigSelection(default="TemplatesChannelSelectionInfoEPG2", choices = epgchannelselection)
config.skin.neutron.infochannelselection = ConfigSelection(default="TemplatesChannelSelectionInfoChannel1", choices = infochannelselection)
config.skin.neutron.coverinfopanel = ConfigSelection(default="TemplatesInfoBarInfoMovieCover1", choices = coverinfopanel)
config.skin.neutron.infomovieselection = ConfigSelection(default="TemplatesMovieSelectionInfoMovie2", choices = infomovieselection)
config.skin.neutron.clockpanel = ConfigSelection(default="TemplatesClock1", choices = clockpanel)
config.skin.neutron.otherinfobar = ConfigSelection(default="TemplatesInfoBarOther1", choices = otherinfobar)
config.skin.neutron.dish = ConfigSelection(default="Dish-2", choices = dish)
config.skin.neutron.scrollbarmode = ConfigSelection(default="showNever", choices = scrollbarmode)
config.skin.neutron.fonts = ConfigSelection(default="Roboto-Regular", choices = fonts)
config.skin.neutron.titlecolor = ConfigSelection(default="#00ffcc33", choices = textcolor)
config.skin.neutron.textcolor = ConfigSelection(default="#00f4f4f4", choices = textcolor)
config.skin.neutron.avtextcolor = ConfigSelection(default="#008f8f8f", choices = textcolor)
config.skin.neutron.textcurcolor = ConfigSelection(default="#00ffcc33", choices = textcolor)
config.skin.neutron.progresscolor = ConfigSelection(default="gold", choices = progresscolor)

class SetupNeutronHD(ConfigListScreen, Screen):
	skin = """
	<!-- Setup NeutronHD -->
	<screen name="SetupNeutronHD" position="0,0" size="1280,720" title=" " flags="wfNoBorder" backgroundColor="transparent">
		<ePixmap position="30,25" size="700,600" pixmap="Neutron_hd/style/greymenu_1.png" alphatest="on" zPosition="-1" />
		<eLabel position="0,610" size="1280,110" backgroundColor="#50000000" zPosition="-2" />
		<ePixmap position="0,575" size="1280,35" pixmap="Neutron_hd/style/greymenubar.png" alphatest="off" zPosition="-2" />
		<ePixmap position="20,635" size="80,80" pixmap="Neutron_hd/menu/setting.png" alphatest="blend" />
		<widget source="Title" render="Label" position="30,25" size="700,36" font="Regular; 30" foregroundColor="#00ffcc33" backgroundColor="background" halign="center" transparent="1" borderWidth="2" />
		<widget name="config" position="45,70" size="670,540" scrollbarMode="showOnDemand" selectionPixmap="Neutron_hd/style/greysel.png" transparent="1" />
		<widget source="info_com" render="Label" position="110,640" size="750,44" font="Regular; 18" foregroundColor="#008f8f8f" backgroundColor="background" halign="left" valign="center" transparent="1" />
		<widget source="version_sk" render="Label" position="110,690" size="150,22" font="Regular; 18" foregroundColor="#008f8f8f" backgroundColor="background" halign="left" valign="center" transparent="1" />
		<widget source="info_sk" render="Label" position="260,690" size="80,22" font="Regular; 18" foregroundColor="#008f8f8f" backgroundColor="background" halign="left" valign="center" transparent="1" />
		<widget source="key_red" render="Label" position="750,615" size="400,25" font="Regular; 22" halign="right" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" />
		<widget source="key_green" render="Label" position="750,640" size="400,25" font="Regular; 22" halign="right" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" />
		<widget source="key_yellow" render="Label" position="750,665" size="400,25" font="Regular; 22" halign="right" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" />
		<widget source="key_blue" render="Label" position="750,690" size="400,25" font="Regular; 22" halign="right" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" />
		<ePixmap pixmap="Neutron_hd/buttons/key_info.png" position="1210,642" size="40,20" alphatest="blend" />
		<ePixmap pixmap="Neutron_hd/buttons/key_epg.png" position="1210,668" size="40,20" alphatest="blend" />
		<ePixmap pixmap="Neutron_hd/buttons/key_red.png" position="1160,616" size="40,20" alphatest="on" />
		<ePixmap pixmap="Neutron_hd/buttons/key_green.png" position="1160,642" size="40,20" alphatest="on" />
		<ePixmap pixmap="Neutron_hd/buttons/key_yellow.png" position="1160,668" size="40,20" alphatest="on" />
		<ePixmap pixmap="Neutron_hd/buttons/key_blue.png" position="1160,694" size="40,20" alphatest="on" />
	</screen>"""

	def __init__(self, session):

		Screen.__init__(self, session)
		self.session = session

		list = []
		list.append(getConfigListEntry(_("Style skins:"), config.skin.neutron.style))
		list.append(getConfigListEntry(_("Channel number in infobars:"), config.skin.neutron.numberchannel))
		list.append(getConfigListEntry(_("Widgets infobar:"), config.skin.neutron.styleinfobar))
		list.append(getConfigListEntry(_("Additional widget infobar:"), config.skin.neutron.technicalinfobar))
		list.append(getConfigListEntry(_("Widgets secondinfobar:"), config.skin.neutron.stylesecondinfobar))
		list.append(getConfigListEntry(_("Additional widget secondinfobar:"), config.skin.neutron.technicalsecondinfobar))
		list.append(getConfigListEntry(_("ECM, EPG panel in secondinfobar:"), config.skin.neutron.ecmepgpanel))
		list.append(getConfigListEntry(_("Panel EPG in channel selection:"), config.skin.neutron.epgchannelselection))
		list.append(getConfigListEntry(_("Additional widgets in channel selection:"), config.skin.neutron.infochannelselection))
		list.append(getConfigListEntry(_("Widget mediainfobar:"), config.skin.neutron.coverinfopanel))
		list.append(getConfigListEntry(_("Panel description in movie selection:"), config.skin.neutron.infomovieselection))
		list.append(getConfigListEntry(_("Clock in menu, infobars:"), config.skin.neutron.clockpanel))
		list.append(getConfigListEntry(_("Other widget in infobars:"), config.skin.neutron.otherinfobar))
		list.append(getConfigListEntry(_("Position dish:"), config.skin.neutron.dish))
		list.append(getConfigListEntry(_("Scrollbar in menu:"), config.skin.neutron.scrollbarmode))
		list.append(getConfigListEntry(_("Fonts:"), config.skin.neutron.fonts))
		list.append(getConfigListEntry(_("Title text color:"), config.skin.neutron.titlecolor))
		list.append(getConfigListEntry(_("Menu text color:"), config.skin.neutron.textcolor))
		list.append(getConfigListEntry(_("Additional text color:"), config.skin.neutron.avtextcolor))
		list.append(getConfigListEntry(_("Cursor text color:"), config.skin.neutron.textcurcolor))
		list.append(getConfigListEntry(_("Progress bar color:"), config.skin.neutron.progresscolor))
		ConfigListScreen.__init__(self, list)

		self["actions"] = ActionMap(["OkCancelActions", "ColorActions", "EPGSelectActions"],{"ok": self.save, "cancel": self.exit, "red": self.exit, "green": self.save, "yellow": self.default, "blue": self.install, "info": self.about}, -1)
		self["key_red"] = StaticText(_("Cancel"))
		self["key_green"] = StaticText(_("Save"))
		self["key_yellow"] = StaticText(_("Default settings"))
		self["key_blue"] = StaticText(_("Install components"))
		self["Title"] = StaticText(_("Setup NeutronHD"))
		self["version_sk"] = StaticText(_("Version skin:"))
		self["info_sk"] = StaticText()
		self["info_com"] = StaticText()

		self.infosk()
		self.infocom()

	def infosk(self):
		package = 0
		global status 
		if fileExists("/usr/lib/opkg/status"):
			status = "/usr/lib/opkg/status"
		elif fileExists("/var/lib/opkg/status"):
			status = "/var/lib/opkg/status"
		elif fileExists("/var/opkg/status"):
			status = "/var/opkg/status"
		for line in open(status):
			if line.find("neutron-hd") > -1:
				package = 1
			if line.find("Version:") > -1 and package == 1:
				package = 0
				try:
					self["info_sk"].text = line.split()[1]
				except:
					self["info_sk"].text = " "
				break

	def infocom(self):
		if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/TMBD/plugin.pyo")\
			and not fileExists("/usr/lib/enigma2/python/Components/Renderer/RatingTmbd.py")\
			and not fileExists("/usr/lib/enigma2/python/Components/Renderer/CoverTmbd.py"):
			self["info_com"] = StaticText(_("No install components TMBD !!!"))
		elif fileExists("/usr/lib/enigma2/python/Plugins/Extensions/Calendar/plugin.pyo")\
			and not fileExists("/usr/lib/enigma2/python/Components/Converter/CalendarToText.py"):
			self["info_com"] = StaticText(_("No install components Calendar !!! \nPress blue button to install !!!"))
		elif fileExists("/usr/lib/enigma2/python/Plugins/Extensions/WeatherMSN/plugin.pyo")\
			and not fileExists("/usr/lib/enigma2/python/Components/Converter/MSNWeather2.py"):
			self["info_com"] = StaticText(_("No install components WeatherMSN !!! \nPress blue button to install !!!"))
		elif fileExists("/usr/lib/enigma2/python/Components/Converter/AlwaysTrue.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/CaidInfo2.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/CamdInfo3.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/ConverterRotator.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/EventName2.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/FrontendInfo2.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/ProgressDiskSpaceInfo.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/RouteInfo.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/RWeather.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceInfoEX.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceName2.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Renderer/PiconUni.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Renderer/RendVolumeText.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Renderer/Watches.py"):
			self["info_com"] = StaticText(_(" "))
		else:
			self["info_com"] = StaticText(_("No install components !!! \nPress blue button to install !!!"))

	def save(self):
		for x in self["config"].list:
			if len(x) > 1:
				x[1].save()
		self.createSkin()

	def default(self):
		for x in self["config"].list:
			if len(x) > 1:
				self.setDefault(x[1])
				x[1].save()
		self.createSkin()
 
	def setDefault(self, configItem):
		configItem.setValue(configItem.default)

	def createSkin(self):
		skinpath = "/usr/share/enigma2/Neutron_hd/"
		try:
	# default skin
			os.system("cp %sdefskin.xml %sskin.xml" % (skinpath, skinpath))
	# color`s text
			os.system("sed -i 's/#10ffcc33/%s/w' %sskin.xml" % (config.skin.neutron.titlecolor.value, skinpath))
			os.system("sed -i 's/#10f4f4f4/%s/w' %sskin.xml" % (config.skin.neutron.textcolor.value, skinpath))
			os.system("sed -i 's/#108f8f8f/%s/w' %sskin.xml" % (config.skin.neutron.avtextcolor.value, skinpath))
			os.system("sed -i 's/#100099ff/%s/w' %sskin.xml" % (config.skin.neutron.textcurcolor.value, skinpath))
	# fonts	
			os.system("sed -i 's/Roboto-Regular/%s/w' %sskin.xml" % (config.skin.neutron.fonts.value, skinpath))
	# number channel
			os.system("sed -i 's/%s/TemplatesInfoBarNumber/w' %sskin.xml" % (config.skin.neutron.numberchannel.value, skinpath))
	# widgets infobar
			os.system("sed -i 's/TemplatesInfoBarTvBar/%s/w' %sskin.xml" % (config.skin.neutron.styleinfobar.value, skinpath))
	# additional infobar
			os.system("sed -i 's/TemplatesInfoBarTvTechnical/%s/w' %sskin.xml" % (config.skin.neutron.technicalinfobar.value, skinpath))
	# widgets secondinfobar
			os.system("sed -i 's/TemplatesInfoBarTvSecondBar/%s/w' %sskin.xml" % (config.skin.neutron.stylesecondinfobar.value, skinpath))
	# additional secondinfobar
			os.system("sed -i 's/TemplatesInfoBarTvSecondTechnical/%s/w' %sskin.xml" % (config.skin.neutron.technicalsecondinfobar.value, skinpath))
	# ecm-epg panel
			os.system("sed -i 's/%s/TemplatesInfoBarECM-EPG/w' %sskin.xml" % (config.skin.neutron.ecmepgpanel.value, skinpath))
	# epg channel selection
			os.system("sed -i 's/%s/TemplatesChannelSelectionInfoEPG/w' %sskin.xml" % (config.skin.neutron.epgchannelselection.value, skinpath))
	# info channel selection
			os.system("sed -i 's/%s/TemplatesChannelSelectionInfoChannel/w' %sskin.xml" % (config.skin.neutron.infochannelselection.value, skinpath))
	# cover info panel
			os.system("sed -i 's/%s/TemplatesInfoBarInfoMovie-Cover/w' %sskin.xml" % (config.skin.neutron.coverinfopanel.value, skinpath))
	# info movie selection
			os.system("sed -i 's/%s/TemplatesMovieSelectionInfoMovie/w' %sskin.xml" % (config.skin.neutron.infomovieselection.value, skinpath))
	# clock panel
			os.system("sed -i 's/%s/TemplatesClock/w' %sskin.xml" % (config.skin.neutron.clockpanel.value, skinpath))
	# other widgets infobar
			os.system("sed -i 's/TemplatesInfoBarTvOther/%s/w' %sskin.xml" % (config.skin.neutron.otherinfobar.value, skinpath))
	# dish
			os.system("sed -i 's/%s/Dish/w' %sskin.xml" % (config.skin.neutron.dish.value, skinpath))
	# scrollbar
			os.system("sed -i 's/showNever/%s/w' %sskin.xml" % (config.skin.neutron.scrollbarmode.value, skinpath))
	# style progress
			os.system("sed -i 's/goldprogress/%sprogress/w' %sskin.xml" % (config.skin.neutron.progresscolor.value, skinpath))
	# style skin`s
			os.system("sed -i 's/greymenu/%smenu/w' %sskin.xml" % (config.skin.neutron.style.value, skinpath))
			os.system("sed -i 's/greysel/%ssel/w' %sskin.xml" % (config.skin.neutron.style.value, skinpath))
			os.system("sed -i 's/greybg/%sbg/w' %sskin.xml" % (config.skin.neutron.style.value, skinpath))
	# end
		except:
			self.session.open(MessageBox, _("Error by processing !!!"), MessageBox.TYPE_ERROR)
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def install(self):
		pluginpath = "/usr/lib/enigma2/python/Plugins/Extensions/"
		componentspath = "/usr/lib/enigma2/python/Components/"
		try:
	# install converter
			os.system("cp %sSetupNeutronHD/components/AlwaysTrue.py %sConverter/AlwaysTrue.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/CaidInfo2.py %sConverter/CaidInfo2.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/CamdInfo3.py %sConverter/CamdInfo3.py" % (pluginpath, componentspath))
			os.system("cp %sCalendar/components/CalendarToText.py %sConverter/CalendarToText.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/ConverterRotator.py %sConverter/ConverterRotator.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/EventName2.py %sConverter/EventName2.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/FrontendInfo2.py %sConverter/FrontendInfo2.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/ProgressDiskSpaceInfo.py %sConverter/ProgressDiskSpaceInfo.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/RouteInfo.py %sConverter/RouteInfo.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/RWeather.py %sConverter/RWeather.py" % (pluginpath, componentspath))
			os.system("cp %sWeatherMSN/components/MSNWeather2.py %sConverter/MSNWeather2.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/ServiceInfoEX.py %sConverter/ServiceInfoEX.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/ServiceName2.py %sConverter/ServiceName2.py" % (pluginpath, componentspath))
	# install renderer
			os.system("cp %sSetupNeutronHD/components/PiconUni.py %sRenderer/PiconUni.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/RendVolumeText.py %sRenderer/RendVolumeText.py" % (pluginpath, componentspath))
			os.system("cp %sSetupNeutronHD/components/Watches.py %sRenderer/Watches.py" % (pluginpath, componentspath))
	# end
		except:
			self.session.open(MessageBox, _("Error by processing !!!"), MessageBox.TYPE_ERROR)
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def exit(self):
		for x in self["config"].list:
			x[1].cancel()
		self.close()

	def restart(self, answer):
		if answer is True:
			config.skin.primary_skin.value = 'Neutron_hd/skin.xml'
			config.skin.primary_skin.save()
			self.session.open(TryQuitMainloop, 3)

	def about(self):
		self.session.open(MessageBox, _("Skin NeutronHD\nDeveloper: Sirius0103 \nHomepage: www.gisclub.tv \n\nDonate:\nWMZ  Z395874509364\nWME  E284580190260\nWMR  R213063691482\nWMU  U658742613505"), MessageBox.TYPE_INFO)

def main(session, **kwargs):
	session.open(SetupNeutronHD)

def Plugins(**kwargs):
	return PluginDescriptor(name=_("Setup NeutronHD"),
	description=_("Setup skin NeutronHD"),
	where = [PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU],
	icon="plugin.png",
	fnc=main)

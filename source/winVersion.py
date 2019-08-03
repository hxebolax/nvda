#winVersion.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2017 NV Access Limited
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import sys
import os
import winUser

winVersion=sys.getwindowsversion()
winVersionText="{v.major}.{v.minor}.{v.build}".format(v=winVersion)
if winVersion.service_pack_major!=0:
	winVersionText+=" service pack %d"%winVersion.service_pack_major
	if winVersion.service_pack_minor!=0:
		winVersionText+=".%d"%winVersion.service_pack_minor
winVersionText+=" %s" % ("workstation","domain controller","server")[winVersion.product_type-1]

def isSupportedOS():
	# NVDA can only run on Windows 7 Service pack 1 and above
	return (winVersion.major,winVersion.minor,winVersion.service_pack_major) >= (6,1,1)

def canRunVc2010Builds():
	return isSupportedOS()

UWP_OCR_DATA_PATH = os.path.expandvars(r"$windir\OCR")
def isUwpOcrAvailable():
	return os.path.isdir(UWP_OCR_DATA_PATH)

def isWin10(version=1507, atLeast=True):
	"""
	Returns True if NVDA is running on the supplied release version of Windows 10. If no argument is supplied, returns True for all public Windows 10 releases.
	@param version: a release version of Windows 10 (such as 1903).
	@param atLeast: return True if NVDA is running on at least this Windows 10 build (i.e. this version or higher).
	"""
	from logHandler import log
	win10VersionsToBuilds={
		1507: 10240,
		1511: 10586,
		1607: 14393,
		1703: 15063,
		1709: 16299,
		1803: 17134,
		1809: 17763,
		1903: 18362
	}
	if atLeast and winVersion.major < 10:
		return False
	elif not atLeast and winVersion.major != 10:
		return False
	try:
		if atLeast:
			return winVersion.build >= win10VersionsToBuilds[version]
		else:
			return winVersion.build == win10VersionsToBuilds[version]
	except KeyError:
		log.error("Unknown Windows 10 version {}".format(version))
		return False

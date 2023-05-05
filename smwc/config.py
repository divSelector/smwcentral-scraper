from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
USER_HOME = Path.home()

####################################################################
#                                     Are These Paths Okay With You?
####################################################################

# The script should try to find these paths for you.
# If it fails or if you'd prefer to specify a different path, 
# # you can.

# RetroArch Binary
RETROARCH_BIN = ''

# Floating IPS Binary
FLIPS_BIN = ''

# RA Config Directory
RETROARCH_CONFIG_DIR = USER_HOME / '.config/retroarch'

# RA SNES Core
SNES_CORE = RETROARCH_CONFIG_DIR / 'cores/snes9x_libretro.so'

# Clean Vanilla Super Mario World ROM
CLEAN_ROM = BASE_DIR / 'cleansmw.sfc'

#####################################################################
#                                                        Okay, Great!
#####################################################################





















# Just Leave These Alone
DEFAULT_RA_CONFIG = RETROARCH_CONFIG_DIR / 'retroarch.cfg'            # RA Default Config
MODIFIED_RA_CONFIG = RETROARCH_CONFIG_DIR / 'retroarch-modified.cfg'  # Save location for copy of default 
                                                                      # config used for options like --no-rewind
# Temp Paths
# Just Leave These Alone
TMP_PATH = BASE_DIR / 'tmp'         # These Directories Will Be Deleted After Scrape
ZIPS_DL_PATH = TMP_PATH / 'zips'    # Used To Store Downloaded Zips During Scrape Phase
UNZIP_DL_PATH = TMP_PATH / 'unzip'  # Used to Store Unzipped Files During ROM Patch Phase
BPS_PATH = TMP_PATH / 'bps'         # Used to Store BPS patches pulled from Unzipped Archives

# Storage Paths
SFC_DIR = BASE_DIR / 'sfc'         # This is Whrere Your Patched ROMs Go

# Developer Options
# Just Leave These Alone
DEBUG_SCRAPER = {
    "ONE_PAGE_ONLY": True,         # If True, Scrapes Every Hack From Only One Page
    "ONE_HACK_ONLY": False,         # If True, Scrapes One Hack Only From Every Page,
                                    # If Both Options True, Scrapes One Hack From One Page
    "SKIP_DATABASE_INSERT": False



}
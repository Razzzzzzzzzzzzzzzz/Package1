Appium_Server_Url_Local = 'http://localhost:4723/wd/hub'
Hilton_Website = "https://www.hilton.com/en/"

capabilities  = dict(
    platformName='Android',
    deviceName='Pixel_Phone',
    udid="emulator-5554",
    platformVersion="35",
    newCommandTimeout=120,
    appPackage='com.hilton.android.hhonors',
    appActivity='com.mofo.android.hilton.core.activity.BootActivity',
    language='en',
    locale='US'
)
class MainPageLocators:
    CONTACT_LINK = ('css selector',
                    'a[href="/contacts"]')
    DOWNLOADS_LINK = ('css selector',
                      'div.sbisru-Footer__container .pb-16:nth-child(3) li.pb-16:nth-child(8) a')


class ContactPageLocators:
    BANNER_LINK = ('css selector',
                   'a.sbisru-Contacts__logo-tensor img')
    REGION_LINK = ('css selector',
                   'div.sbisru-Contacts__relative span.sbis_ru-Region-Chooser')
    PARTNERS_LINK = ('css selector',
                     'div[name="itemsContainer"] div.sbisru-Contacts-List__name')
    PARTNER_BLOCK_LINK = ('css selector',
                    'div.sbisru-Contacts-List__col')
    REQUIRED_REGION_LINK = ('css selector', 'span[title="Камчатский край"]')


class DownloadsPageLocators:
    PLUGINS_LINK = ('css selector', '[data-id="plugin"]')
    DOWNLOADS_LINK = ('css selector', 'div.ws-SwitchableArea__item[data-for="plugin"] .sbis_ru-DownloadNew-block .sbis_ru-DownloadNew-loadLink a')


class TensorPageLocators:
    ABOUT_LINK = ('css selector', 'div.tensor_ru-Index__block4-bg a.tensor_ru-link')
    POWER_BLOCK = ('css selector', 'div.tensor_ru-Index__block4-content')


class AboutPageLocators:
    PHOTOS = ('css selector', 'div.tensor_ru-About__block3 img')



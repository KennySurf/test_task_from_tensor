from .base_page import BasePage
from .locators import AboutPageLocators


class AboutPage(BasePage):

    def scroll_to_photos_block(self):
        self.scroll(AboutPageLocators.PHOTOS)

    def is_photos_block_present(self):
        self.is_element_present(AboutPageLocators.PHOTOS)

    def check_photos_height_width(self):
        photos = self.browser.find_elements(*AboutPageLocators.PHOTOS)
        first_photo_dimensions = None

        for photo in photos:
            if not first_photo_dimensions:
                first_photo_dimensions = (photo.size['height'], photo.size['width'])

                assert (photo.size['height'], photo.size['width']) == first_photo_dimensions, \
                    f'Photo dimensions do not match: {photos.size}'

        print('All photos have the same height and width.')

from skimage import io
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import os

class Kinopoisk:
    def __init__(self, executable_path="chromedriver"):
        options = Options()
        # options.add_argument("--headless")
        self.browser = Chrome(executable_path=executable_path, options=options)  # http://chromedriver.chromium.org/downloads
        self.folder_to_save_images = 'actors/'

    def get_num_of_files_in_dir(self,file_dir):
	    num_of_files = sum(os.path.isfile(os.path.join(file_dir, f)) for f in os.listdir(file_dir))
	    return num_of_files

    def get_actors(self):
        actor_id = self.get_num_of_files_in_dir(self.folder_to_save_images) + 1
        while True:
        	try:
	            self.browser.get('https://www.kinopoisk.ru/name/{}'.format(actor_id))
	            name = self.browser.find_element_by_class_name("moviename-big").text
	            filename = "{}{}_{}.jpg".format(self.folder_to_save_images, actor_id, name)

	            image = io.imread("https://st.kp.yandex.net/images/actor/{}.jpg".format(actor_id))
	            io.imsave(filename, image)

	            print(filename)
	        except Exception as e:
	        	print('\n', e, '\n')
	        finally:
	        	actor_id += 1


if __name__ == "__main__":
    kinopoisk = Kinopoisk("D:\\kino\\chromedriver\\chromedriver.exe")
    kinopoisk.get_actors()

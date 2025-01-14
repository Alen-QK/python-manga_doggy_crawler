import abc


class MangaSite(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def search_manga(self, search_name, CF_dict):
        pass

    @abc.abstractmethod
    def check_manga_length(self, CF_dict):
        pass

    @abc.abstractmethod
    def generate_chapters_array(
        self, start, end, download_root_folder_path, manga_name, CF_dict
    ):
        pass

    @abc.abstractmethod
    def scrape_each_chapter(
        self, chapter, manga_library, Error_dict, his_length, idx, app, CF_dict
    ):
        pass

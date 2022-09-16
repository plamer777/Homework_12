"""This unit contains a PostsManager class provides all methods to work with
posts like - saving, finding, refreshing etc."""
import json
import os
# --------------------------------------------------------------------------


class PostsManager:
    """PostsManager class serves to proceed posts"""
    def __init__(self, filename: str, allowed_files: set):
        """Initialization of PostsManager.

        :param filename: A name of JSON file with posts data
        :param  allowed_files: A set of files' extensions allowed to save
        """
        self.source = filename
        self.allowed_files = allowed_files
        self.posts = self.load_data(filename)
        self.filesize = os.path.getsize(self.source)

    @staticmethod
    def load_data(filename: str) -> list:
        """This staticmethod loads posts from a JSON file

        :param filename: A name of JSON file
        """
        try:
            with open(filename, encoding='utf-8') as fin:

                posts = json.load(fin)

            return posts

        # Extension handling
        except FileNotFoundError:
            print(f'Не удалось найти файл {filename}')

        except json.JSONDecodeError:
            print(f'Не удалось декодировать файл {filename}')

    def is_loaded(self):
        """Checking if posts were loaded"""
        if self.posts:

            return True

        return False

    def is_file_changed(self):
        """Checking if JSON file with posts was changed

        Returns:
            True of False
        """
        return os.path.getsize(self.source) != self.filesize

    def refresh_cash(self):
        """This method refresh posts field of the class"""
        self.posts = self.load_data(self.source)
        self.filesize = os.path.getsize(self.source)

    def find(self, key_word: str) -> list:
        """Finding a post in posts field by key_word provided by user

        :param key_word: A word used to search in posts
        Returns
            found_posts - A list of found posts
        """
        key_word = key_word.lower()

        found_posts = [post for post in self.posts if key_word in post.get(
            'content').lower()]

        return found_posts

    def save(self, pic_filename: str, post_text: str):
        """Saving a post data in JSON file

        :param pic_filename: A URL of an image file saved in a local storage
        :param post_text: A text content sent by user
        """
        new_post = {'pic': pic_filename, 'content': post_text}

        self.posts.append(new_post)
        self._refresh_file()

    def _refresh_file(self):
        """Closed method serves to refresh JSON file"""
        with open(self.source, 'wt', encoding='utf-8') as fout:

            json.dump(self.posts, fout, ensure_ascii=False)

    def is_allowed(self, filename: str):
        """Checking if a filename is allowed to save in the local storage"""
        extension = filename.split('.')[-1]

        if extension in self.allowed_files:

            return True

        return False



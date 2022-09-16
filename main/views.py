"""This unit contains blueprint and views for root '/' and '/search/ routes"""
from flask import Blueprint, render_template, request
from lesson12_project_source_v3.managers.posts_manager import PostsManager
from lesson12_project_source_v3.config import ALLOWED, POST_SOURCE, LOG_PATH, \
    LOG_FORMAT
from lesson12_project_source_v3.managers.logger_builder import LoggerBuilder
# -----------------------------------------------------------------------------


# Creation of blueprint, post_manager and logger_builder instances
main_blueprint = Blueprint('main_blueprint', __name__,
                           template_folder='templates',
                           static_folder='static_main')
post_manager = PostsManager(POST_SOURCE, ALLOWED)
logger_builder = LoggerBuilder()

search_logger = logger_builder.get_new(LOG_PATH, 'search', LOG_FORMAT)


@main_blueprint.route('/')
def index_page():
    """A view is for the root route. The view returns an index template

    Returns
        A template of the index page
    """
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    """This view returns all posts found by user's keyword

    Returns
        A template of a post list page
    """
    # Getting user's searched word
    key_word = request.args.get('s')

    # If JSON file was changed then refresh a data cash
    if post_manager.is_file_changed():
        post_manager.refresh_cash()

    # Getting all posts found by user's searched word
    posts = post_manager.find(key_word)

    search_logger.info(f'User is looking for "{key_word}", posts found:'
                       f' {len(posts)}')

    return render_template('post_list.html', key_word=key_word, posts=posts)

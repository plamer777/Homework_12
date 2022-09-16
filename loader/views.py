"""This unit contains all necessary views for 'post' route"""
from flask import Blueprint, render_template, request, url_for
from lesson12_project_source_v3.managers.posts_manager import PostsManager
from lesson12_project_source_v3.managers.logger_builder import LoggerBuilder
from lesson12_project_source_v3.config import ALLOWED, POST_SOURCE, UPLOADS, \
    LOG_PATH, LOG_FORMAT
# --------------------------------------------------------------------------

# Creation of blueprint, post_manager and logger_builder instances
loader_blueprint = Blueprint('loader_blueprint', __name__,
                             template_folder='templates',
                             static_folder='static_loader')
post_manager = PostsManager(POST_SOURCE, ALLOWED)
logger_builder = LoggerBuilder()

# Creation of new logger
post_logger = logger_builder.get_new(LOG_PATH, 'poster', LOG_FORMAT)


@loader_blueprint.route('/post/', methods=['GET'])
def post_page():
    """This view proceeds 'post' routes of 'GET' requests

    Returns:
        The template of a post form
    """
    return render_template('post_form.html')


@loader_blueprint.route('/post/', methods=['POST'])
def post_uploaded():
    """This view proceeds all 'POST' requests for '/post' route

    Returns
        The template of uploaded post page or a simple text with error
    """
    # Getting a picture file object and a text of a post provided by user
    picture = request.files.get('picture')
    post_text = request.form.get('content')
    pic_file = picture.filename

    # If user haven't filled a text field then provide text by default
    if not post_text:
        post_text = 'Здесь должен быть какой-то текст'

    # If the file was received and has an allowed type then save it and refresh
    # JSON file
    if picture:

        if post_manager.is_allowed(pic_file):

            pic_path = url_for('static_dir', path=pic_file)

            picture.save(UPLOADS + pic_file)
            post_manager.save(pic_path, post_text)

            return render_template('post_uploaded.html',
                                   img_file=pic_path, text=post_text)

        else:
            # If the file type is unsupported then return an error text and
            # write an info log
            post_logger.info(f'User tried to upload {pic_file}')
            return "Вы пытаетесь загрузить недопустимый формат файла"

    # If the file wasn't received or there were another problems then return
    # an error text and write error log
    post_logger.error('При загрузке файла возникла ошибка')
    return "При загрузке файла возникла ошибка, попробуйте еще раз"

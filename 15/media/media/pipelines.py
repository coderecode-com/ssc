from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes
import hashlib

class CustomFilesPipeline(FilesPipeline):
    
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = item.get('BookTitle')+'.pdf'
        return file_name

class CustomImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = item.get('BookTitle') + '.jpg'
        return image_name

    def thumb_path(self, request, thumb_id, response=None, info=None):
        thumb_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f'thumbs/{thumb_id}/{thumb_guid}.jpg'

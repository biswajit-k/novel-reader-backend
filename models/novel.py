import json
from mongoengine import *
from mongoengine import signals     # TODO: why do we need to import is separately

from datetime import datetime

from models.chapter import Chapter
from enums import NovelStatus, NovelType, NovelGenre

class Novel(Document):
    title = StringField(required=True, max_length=120, unique=True)     # title must be unique
    description = StringField(required=True, max_length=500)
    image_url = StringField(required=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    rating = DecimalField(min_value=0, max_value=5, precision=2, default=0) # 0 means unrated
    author = StringField(max_length=50)
    translator = StringField(max_length=50)
    genre = ListField(choices=[genre.value for genre in NovelGenre], required=True)
    status = StringField(choices=[status.value for status in NovelStatus], required=True)
    type = StringField(choices=[novel_type.value for novel_type in NovelType])
    chapters = ListField(EmbeddedDocumentField(Chapter))
    # _views = IntField(default=0)

    @classmethod
    def make_title_lower(cls, sender, values, **kwargs):
        values['title'] = values['title'].lower()

    # TODO: recheck requirement of this fun.
    def to_json_dict(self):
        return json.loads(self.to_json())

    def to_dict(self):
        novel_dic = self.to_mongo().to_dict()
        novel_dic.pop('_id')
        novel_dic['created_at'] = novel_dic['created_at'].isoformat()
        novel_dic['updated_at'] = novel_dic['updated_at'].isoformat()
        return novel_dic


    def to_cover(self):
        return {
            "title": self.title,
            "image_url": self.image_url,
            "rating": self.rating,
            "status": self.status,
        }

# convert title to lowercase before inserting
signals.pre_init.connect(Novel.make_title_lower, sender=Novel)
from flask import request, abort
from mongoengine import Q, DoesNotExist

from routes import router
from models.novel import Novel


##### GET /novels
@router.route('/novels')
def get_novels():
    """
        ?type=
        popular - rating DESC
        new - created DESC
        latest_updated - updated_at DESC

        ?genre=
        genre contain this word

        example- http://localhost:5000/novels?page=1&limit=2&genre=adventure&sort_by=new
    """

    # constants
    DEFAULT_LIMIT = 5
    sort_by_to_order = {
        'popular': '-rating',
        'new': '-created_at',
        'latest_updated': '-updated_at'
    }

    # pagination
    limit = request.args.get('limit', DEFAULT_LIMIT, type=int)
    page = request.args.get('page', 1, type=int)
    begin = (page - 1) * limit
    end = begin + limit

    # filter
    sort_by = request.args.get('sort_by', None)
    genre = request.args.get('genre', None)

    # query
    query = Q(genre=genre) if genre else Q()
    try:
        if sort_by:
            novels = Novel.objects[begin:end](query).order_by(sort_by_to_order[sort_by])
        else:
            novels = Novel.objects[begin:end](query)
        return {"data": [obj.to_cover() for obj in novels]}
    except IndexError:
        return {"data": []}


##### POST /novels
@router.route('/novels', methods=['POST'])
def add_novel():
    """
        Inserts single/multipe novel records to database after validating each record
        with the schema. If any record doesn't match with the schema, raise 400 Bad
        Request response.

        For single record directly provide JSON object
        For multiple records provide JSON with key as "batch": value as array of objects
    """

    data = request.get_json()

    if "batch" in data:
        novel_instances = [Novel(**novel) for novel in data['batch']]
        novels = Novel.objects.insert(novel_instances)
        return {"data": [obj.to_json_dict() for obj in novels]}
    else:
        novel = Novel(**data).save()
        return {"data": novel.to_json_dict()}


##### GET /novels/<novel-slug>
@router.route('/novels/<novel_slug>')
def get_novel(novel_slug):
    novel_slug = novel_slug.replace('-', ' ')

    try:
        novel = Novel.objects.get(title=novel_slug)
        return {"data": novel.to_dict()}
    except DoesNotExist:
        abort(404)


##### GET /heroes
@router.route('/heroes')
def get_heroes():
    from data.hero import heroes
    return {"data": heroes}
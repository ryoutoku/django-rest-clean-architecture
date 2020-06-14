import datetime


class Question:
    def __init__(self,
                 question_text: str,
                 pub_date: datetime.datetime,
                 id: str = None):

        if "チェックword" in question_text:
            raise ValueError("不適切な文字列が含まれています")

        if pub_date >= datetime.datetime.now(datetime.timezone.utc):
            raise ValueError("本日以降の日付は不適です")

        self._id = id
        self._question_text = question_text
        self._pub_date = pub_date

    @property
    def id(self):
        return self._id

    @property
    def question_text(self):
        return self._question_text

    @property
    def pub_date(self):
        return self._pub_date

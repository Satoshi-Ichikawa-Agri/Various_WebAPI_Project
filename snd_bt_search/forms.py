from django import forms


DEFAULT = -1
BROADCAST_YEAR = [
    (DEFAULT, "--選択してください--"),
    ("2010", "2010"),
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
    ("2014", "2014"),
    ("2015", "2015"),
    ("2016", "2016"),
    ("2017", "2017"),
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"),
    ("2021", "2021"),
    ("2022", "2022"),
    ("2023", "2023"),
    ]
BROADCAST_MONTH = [
    (DEFAULT, "--選択してください--"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ]


class SndBroadcastSearchForm(forms.Form):
    """ 問い合わせフォーム """

    broadcast_year = forms.ChoiceField(
        label="放送年",
        choices=BROADCAST_YEAR,
        initial=DEFAULT,
        required=False
        )
    broadcast_month = forms.ChoiceField(
        label="放送月",
        choices=BROADCAST_MONTH,
        initial=DEFAULT,
        required=False
        )
    broadcast_date = forms.CharField(
        label="放送日",
        widget=forms.TextInput(attrs={"placeholder": "例:20220401"}),
        required=False
        )
    broadcast_content = forms.CharField(
        label="放送内容",
        widget=forms.TextInput(attrs={"placeholder": "例:ゲスト回"}),
        required=False
        )
    assistant_1 = forms.CharField(
        label="アシスタント1",
        widget=forms.TextInput(attrs={"placeholder": "例:タイムマシーン3号"}),
        required=False
        )
    assistant_2 = forms.CharField(
        label="アシスタント2",
        widget=forms.TextInput(attrs={"placeholder": "例:安田"}),
        required=False
        )
    guests = forms.CharField(
        label="ゲスト",
        widget=forms.TextInput(attrs={"placeholder": "例:もう中学生"}),
        required=False
        )
    remarks = forms.CharField(
        label="備考",
        widget=forms.TextInput(attrs={"placeholder": "例:有吉さん不在"}),
        required=False
        )

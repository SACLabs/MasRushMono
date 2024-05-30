from masr.models import interface
from masr.models.graph import GML
from masr.models.task import TaskStatus, TaskItem, TaskHistory
import uuid

mock_task_id = uuid.uuid4()

mock_code = interface.SourceCode(
    tree="procoder                \
            ├── functional.py       \
            ├── __init__.py         \
            ├── prompt              \
            │   ├── base.py         \
            │   ├── __init__.py     \
            │   ├── modules.py      \
            │   ├── proxy.py        \
            │   ├── sequential.py   \
            │   └── utils.py        \
            └── utils               \
                ├── __init__.py     \
                └── my_typing.py",
    content={
        "procoder/functional.py": "mock_functional_code",
        "procoder/__init__.py": "mock_init_code",
        "procoder/prompt/base.py": "mock base code",
        "procoder/prompt/__init__.py": "mock init code",
        "procoder/prompt/modules.py": "mock modules code",
        "procoder/prompt/proxy.py": "mock proxy code",
        "procoder/prompt/sequential.py": "mock sequential code",
        "procoder/prompt/utils.py": "mock utils code",
        "procoder/utils/__init__.py": "mock utils init code",
        "procoder/utils/my_typing.py": "mock my typing code",
    },
)

mock_task = TaskItem(
    name="test task",
    description="test task description",
    status=TaskStatus.COMPLETED,
)

mock_history = TaskHistory(history=[mock_task])

mock_graph = GML(
    content="""graph [
  directed 1
  multigraph 1
  node [
    id 0
    label "0"
    text "Q7e4g1tqvb"
    timestamp "2018-05-17T16:13:44"
    vector "[0.9752010913947884, 0.34856581335589976, 0.8634797649400338, 0.7800563970100388, 0.16638089624012253]"
  ]
  node [
    id 1
    label "1"
    text "yHvU7QlgC7"
    timestamp "2020-05-25T16:23:18"
    vector "[0.8355750196544272, 0.7533356128861783, 0.12178372520647363, 0.8062625767756563, 0.34207250223887065]"
  ]
  node [
    id 2
    label "2"
    text "6811v0S1ch"
    timestamp "2020-12-29T17:42:44"
    vector "[0.6399258378889909, 0.4593960211575431, 0.9048917147248771, 0.3043908054926876, 0.9552085834991884]"
  ]
  node [
    id 3
    label "3"
    text "merx3fU1pb"
    timestamp "1992-11-23T06:20:24"
    vector "[0.3687598324161576, 0.5575436648861316, 0.6181395588387923, 0.8952594814132565, 0.8103168936274068]"
  ]
  node [
    id 4
    label "4"
    text "eCaJ8AjGEw"
    timestamp "2016-01-29T18:15:44"
    vector "[0.7928774721203862, 0.8705000776332359, 0.27576624375133774, 0.6756090927017985, 0.21945267439925986]"
  ]
  edge [
    source 0
    target 4
    key 0
    text "DGSPSfPg2h"
    timestamp "2006-02-27T16:16:35"
    vector "[0.7551078587610066, 0.07752817492553465, 0.38172931814191857, 0.7333959630430331, 0.028827148680080183]"
  ]
  edge [
    source 0
    target 2
    key 0
    text "mdU8vyEMT0"
    timestamp "2021-01-22T02:36:20"
    vector "[0.08097260085485358, 0.9730849487794317, 0.5968264658320127, 0.6793913474826738, 0.46929466616372884]"
  ]
  edge [
    source 2
    target 3
    key 0
    text "Ct1eUg4A6m"
    timestamp "1998-07-22T16:41:15"
    vector "[0.6307465080597158, 0.5482765554626802, 0.60542221700032, 0.3763150282610217, 0.5472253294357773]"
  ]
  edge [
    source 3
    target 4
    key 0
    text "dSQTdKWdGc"
    timestamp "1973-11-02T17:30:31"
    vector "[0.1091899908195122, 0.7331643505827067, 0.31948601315841485, 0.2840341593751171, 0.08240057321538263]"
  ]
  edge [
    source 3
    target 4
    key 1
    text "i3q77XyAG3"
    timestamp "2009-12-27T19:57:00"
    vector "[0.8198545762033694, 0.10159072036235584, 0.8963390267695304, 0.753661559825993, 0.6043442426070716]"
  ]
  edge [
    source 3
    target 1
    key 0
    text "py5RRhqx0G"
    timestamp "1998-10-18T18:52:49"
    vector "[0.6386797687470783, 0.24414668048658572, 0.6712126810219465, 0.6132568070855082, 0.4679866650760145]"
  ]
  edge [
    source 3
    target 1
    key 1
    text "GL3i24PdPB"
    timestamp "2011-01-27T17:56:14"
    vector "[0.747051580386023, 0.20257178565400857, 0.1350360300232588, 0.6135417751217457, 0.7494798215260531]"
  ]
  edge [
    source 4
    target 1
    key 0
    text "B0eMyYbq8R"
    timestamp "1981-09-10T10:24:28"
    vector "[0.16578617577306587, 0.6997805277909424, 0.3182990420641887, 0.8126857972243429, 0.7363629765081304]"
  ]
  edge [
    source 4
    target 1
    key 1
    text "6upAQo61Bi"
    timestamp "1999-11-24T13:31:17"
    vector "[0.894342294745374, 0.6625503464945209, 0.1507365641527214, 0.3511726842743337, 0.10395991677795047]"
  ]
  edge [
    source 4
    target 0
    key 0
    text "kmbRaRI7tO"
    timestamp "1970-11-10T17:51:01"
    vector "[0.3518526889741863, 0.6645952859277418, 0.9969294060407838, 0.11944566601822093, 0.339589587550285]"
  ]
]
"""
)


def mock_sender(x):
    return x


def test_sender_data_format():
    sender_data = interface.pack_mas_to_env_msg(
        task_id=mock_task_id,
        result=mock_code,
        history=mock_history,
        graph=mock_graph,
    )
    assert "task_id" in sender_data
    assert sender_data["task_id"] == mock_task_id

    assert "result" in sender_data["content"]
    assert sender_data["content"]["result"] == mock_code

    assert "history" in sender_data["content"]
    assert sender_data["content"]["history"] == mock_history

    assert "graph" in sender_data["content"]
    assert sender_data["content"]["graph"] == mock_graph


def test_reciever_data_format():
    sender_data = interface.pack_env_to_mas_msg(
        mock_task_id, mock_code, mock_history, mock_graph
    )
    reciever_data = mock_sender(sender_data)
    assert sender_data == reciever_data

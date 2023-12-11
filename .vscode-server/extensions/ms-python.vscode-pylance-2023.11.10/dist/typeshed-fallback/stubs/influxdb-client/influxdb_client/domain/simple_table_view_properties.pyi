from _typeshed import Incomplete

from influxdb_client.domain.view_properties import ViewProperties

class SimpleTableViewProperties(ViewProperties):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        type: Incomplete | None = None,
        show_all: Incomplete | None = None,
        queries: Incomplete | None = None,
        shape: Incomplete | None = None,
        note: Incomplete | None = None,
        show_note_when_empty: Incomplete | None = None,
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def show_all(self): ...
    @show_all.setter
    def show_all(self, show_all) -> None: ...
    @property
    def queries(self): ...
    @queries.setter
    def queries(self, queries) -> None: ...
    @property
    def shape(self): ...
    @shape.setter
    def shape(self, shape) -> None: ...
    @property
    def note(self): ...
    @note.setter
    def note(self, note) -> None: ...
    @property
    def show_note_when_empty(self): ...
    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

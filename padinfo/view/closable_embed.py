from padinfo.view.components.view_state_base import ViewStateBase


class ClosableEmbedViewState(ViewStateBase):
    def __init__(self, original_author_id, menu_type, raw_query,
                 color, view_type, props, extra_state=None):
        super().__init__(original_author_id, menu_type, raw_query, extra_state=extra_state)
        self.color = color
        self.view_type = view_type
        self.props = props

    def serialize(self):
        ret = super().serialize()
        ret.update({
            'view_type': self.view_type
        })
        return ret

    @staticmethod
    def deserialize(self, dgcog, user_config, ims):


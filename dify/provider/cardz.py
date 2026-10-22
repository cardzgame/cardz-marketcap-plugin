from dify_plugin import ToolProvider


class CardzProvider(ToolProvider):
    def _validate_credentials(self, credentials):
        if credentials:
            raise ValueError('CARDZ public market data does not require credentials.')

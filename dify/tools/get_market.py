import json

from dify_plugin import Tool

from cardz_api import call_tool


class GetMarketTool(Tool):
    def _invoke(self, tool_parameters):
        result = call_tool('get_market', tool_parameters)
        yield self.create_json_message(result)
        yield self.create_text_message(json.dumps(result, ensure_ascii=False))

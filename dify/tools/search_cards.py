import json

from dify_plugin import Tool

from cardz_api import call_tool


class SearchCardsTool(Tool):
    def _invoke(self, tool_parameters):
        result = call_tool('search_cards', tool_parameters)
        yield self.create_json_message(result)
        yield self.create_text_message(json.dumps(result, ensure_ascii=False))

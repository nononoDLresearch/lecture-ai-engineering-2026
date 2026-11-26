# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：[glossary_search_glossary]
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
                        glossary_search_glossary({'query': 'MCP'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'search_phrase': 'Amazon S3 バージョニング 概要', 'topics': ['general']}), aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Using versioning Amazon S3'})
- 気づき・疑問：3種類いずれにおいてもMCPサーバーを介してコマンドを実行できた。どの方法も何度かモデルが呼ばれていた。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：実装
- やったこと：make_quiz を、app/mcp_server.py で公開します。
- 結果：
**【第3回 確認問題】**
「構造化出力」の意味は？

（ヒント：モデルからの出力をそのまま文字列として受け取るのではなく、プログラムで扱いやすいように決まった型やルールに強制して受け取る仕組みのことです。Pydantic AIでは、`output_type`などにモデルを指定して利用します。）
考えてみてくださいね！
（関連する回：第3回）

--- trace ---
[tool call]   glossary_make_quiz({'lecture': 3})
[tool return] glossary_make_quiz -> {"question": "「構造化出力」の意味は？", "answer": "モデルの出力を、決めた型やJSONスキーマに沿った形で受け取る仕組み。プログラムで後処理しやすくなる。Pydantic AIでは output_type にPy…
[usage] 入力 5,651 tokens / 出力 115 tokens / モデル応答 2 回

###存在しない回
第8回に関連する用語集データが見つからなかったため、第8回の内容や用語集についてご案内することができません。
もし他の回（例: 第1回〜第7回など）の確認問題をご希望でしたら、該当する回を指定してお知らせください！
--- trace ---
[tool call]   glossary_make_quiz({'lecture': 8})
[tool return] glossary_make_quiz -> 第8回の用語は用語集にありません。…
[usage] 入力 5,601 tokens / 出力 76 tokens / モデル応答 2 回
- 気づき・疑問：適切に第3回の内容に則したクイズが出題された。tool callではmake_quizが呼び出されていた。まだ講義が終了していない回については、出題されなかった。
